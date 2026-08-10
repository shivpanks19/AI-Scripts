"""Experimental SVG logo layer — extends Phase 9a compositor without replacing production path."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw

from .image_bounds import crop_to_visible
from .layout_resolver import (
    anchor_position,
    apply_smart_logo_layout,
    contain_fit,
    layout_from_creative_dna,
    normalized_to_pixels,
    resolve_canvas,
    resolve_logo_zone,
)
from .logo_compositor import CompositionResult
from .logo_presets import get_preset, resolve_size_fraction
from .logo_treatment import apply_logo_treatment
from .svg_renderer import render_svg_to_image, svg_intrinsic_size
from .validator import CompositionValidationError, validate_composition_result, validate_layout


MAX_ROTATION_DEG = 15.0


@dataclass
class SvgLayerResult(CompositionResult):
    logo_rotation: float = 0.0
    logo_opacity: float = 1.0
    logo_treatment: dict[str, Any] | None = None
    logo_asset_format: str = "png"
    debug_metadata: dict[str, Any] | None = None


def _clamp_rotation(value: float) -> float:
    return max(-MAX_ROTATION_DEG, min(MAX_ROTATION_DEG, float(value)))


def _load_logo_asset(path: Path, max_w: int, max_h: int) -> tuple[Image.Image, float, str]:
    if path.suffix.lower() == ".svg":
        intrinsic_w, intrinsic_h = svg_intrinsic_size(path)
        aspect = intrinsic_w / intrinsic_h
        fit_w, fit_h, _ = contain_fit(intrinsic_w, intrinsic_h, max_w, max_h)
        # Render SVG at final pixel size — vector quality until this point
        rendered = render_svg_to_image(path, fit_w, fit_h)
        return rendered, aspect, "svg"
    visible = crop_to_visible(Image.open(path).convert("RGBA"))
    aspect = visible.width / visible.height
    fit_w, fit_h, _ = contain_fit(visible.width, visible.height, max_w, max_h)
    return visible.resize((fit_w, fit_h), Image.Resampling.LANCZOS), aspect, "png"


def compose_svg_logo_layer(
    background: Image.Image,
    logo_path: Path,
    *,
    canvas_width: int,
    canvas_height: int,
    zone: dict[str, float],
    anchor: str,
    max_width_fraction: float,
    max_height_fraction: float,
    rotation: float = 0.0,
    opacity: float = 1.0,
    treatment: dict[str, Any] | None = None,
) -> tuple[Image.Image, dict[str, int], dict[str, int], float, float, Image.Image]:
    if background.size != (canvas_width, canvas_height):
        background = background.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)

    zone_px = normalized_to_pixels(zone, canvas_width, canvas_height)
    max_w = max(1, round(max_width_fraction * canvas_width))
    max_h = max(1, round(max_height_fraction * canvas_height))

    logo_image, original_aspect, _fmt = _load_logo_asset(logo_path, max_w, max_h)
    pre_treatment_w, pre_treatment_h = logo_image.size
    pre_treatment_aspect = pre_treatment_w / pre_treatment_h

    treatment_cfg = copy.deepcopy(treatment) if treatment else None
    if treatment_cfg is not None:
        treatment_cfg.setdefault("opacity", opacity)
    logo_image = apply_logo_treatment(logo_image, treatment_cfg)

    if opacity < 1.0 and (not treatment_cfg or treatment_cfg.get("type", "none") == "none"):
        alpha = logo_image.getchannel("A")
        alpha = alpha.point(lambda p: int(p * opacity))
        logo_image.putalpha(alpha)

    rotation = _clamp_rotation(rotation)
    if rotation != 0:
        logo_image = logo_image.rotate(rotation, expand=True, resample=Image.Resampling.BICUBIC)

    render_w, render_h = logo_image.size
    render_aspect = render_w / render_h
    x, y = anchor_position(zone_px, render_w, render_h, anchor)

    composed = background.convert("RGBA")
    composed.alpha_composite(logo_image, dest=(x, y))

    return (
        composed,
        {"x": x, "y": y, "width": render_w, "height": render_h},
        zone_px,
        pre_treatment_aspect,
        pre_treatment_aspect,
        logo_image,
    )


def render_svg_debug_overlay(
    base: Image.Image,
    layout: dict[str, Any],
    logo_pixels: dict[str, int],
    zone_pixels: dict[str, int],
    metadata: dict[str, Any],
) -> Image.Image:
    img = base.copy().convert("RGBA")
    draw = ImageDraw.Draw(img)

    def rect(zone: dict[str, int], outline: str, label: str) -> None:
        box = [zone["x"], zone["y"], zone["x"] + zone["width"], zone["y"] + zone["height"]]
        draw.rectangle(box, outline=outline, width=3)
        draw.text((zone["x"] + 4, zone["y"] + 4), label, fill=outline)

    canvas = layout.get("canvas", {})
    y = 10
    lines = [
        f"Canvas: {canvas.get('width')}x{canvas.get('height')}",
        f"Position: {metadata.get('position')}",
        f"Size: {metadata.get('size')}",
        f"Zone: x={zone_pixels['x']} y={zone_pixels['y']} w={zone_pixels['width']} h={zone_pixels['height']}",
        f"Logo: x={logo_pixels['x']} y={logo_pixels['y']} w={logo_pixels['width']} h={logo_pixels['height']}",
        f"Rotation: {metadata.get('rotation', 0)}°",
        f"Treatment: {metadata.get('treatment', {}).get('type', 'none')}",
        f"Asset: {metadata.get('asset_format')} — {metadata.get('asset_path')}",
    ]
    for line in lines:
        draw.text((10, y), line, fill="#00FF88")
        y += 16

    rect(zone_pixels, "#00BFFF", "LOGO ZONE")
    rect(logo_pixels, "#FFD700", "LOGO BBOX")

    return img


def compose_svg_experiment(
    *,
    background_path: Path,
    logo_asset_path: Path,
    output_path: Path,
    layout: dict[str, Any],
    creative_dna: dict[str, Any] | None = None,
    brand_dna: dict[str, Any] | None = None,
    debug: bool = False,
    debug_path: Path | None = None,
) -> SvgLayerResult:
    layout = apply_smart_logo_layout(dict(layout), creative_dna, brand_dna)
    validate_layout(layout)

    background = Image.open(background_path).convert("RGBA")
    canvas = resolve_canvas(layout, background.width, background.height)
    cw, ch = canvas["width"], canvas["height"]

    if brand_dna:
        logo_cfg = resolve_logo_zone(layout, brand_dna)
    else:
        logo_block = layout.get("logo", {})
        position = logo_block.get("position", "TOP_LEFT")
        preset = get_preset(position)
        size_key = logo_block.get("size", "MEDIUM")
        logo_cfg = {
            "position": position,
            "anchor": preset["anchor"],
            "zone": dict(logo_block.get("zone") or layout.get("logoZone") or preset["zone"]),
            "max_width": float(logo_block.get("maxWidth") or resolve_size_fraction(size_key)),
            "max_height": float(logo_block.get("maxHeight", preset["max_height"])),
            "size": str(size_key).upper(),
        }

    logo_block = layout.get("logo", {})
    zone = logo_cfg["zone"]
    position = logo_cfg["position"]
    size_key = logo_cfg["size"]

    rotation = _clamp_rotation(logo_block.get("rotation", 0))
    opacity = float(logo_block.get("opacity", 1.0))
    treatment = logo_block.get("treatment")

    if not logo_asset_path.exists():
        raise CompositionValidationError(f"Logo asset not found: {logo_asset_path}")

    composed, logo_pixels, zone_pixels, orig_aspect, render_aspect, _ = compose_svg_logo_layer(
        background,
        logo_asset_path,
        canvas_width=cw,
        canvas_height=ch,
        zone=zone,
        anchor=logo_cfg["anchor"],
        max_width_fraction=logo_cfg["max_width"],
        max_height_fraction=logo_cfg["max_height"],
        rotation=rotation,
        opacity=opacity,
        treatment=treatment,
    )

    validate_composition_result(
        canvas_width=cw,
        canvas_height=ch,
        logo_x=logo_pixels["x"],
        logo_y=logo_pixels["y"],
        logo_w=logo_pixels["width"],
        logo_h=logo_pixels["height"],
        logo_source_path=str(logo_asset_path),
        zone_px=zone_pixels,
        original_aspect=orig_aspect,
        render_aspect=render_aspect,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    composed.convert("RGB").save(output_path, "PNG")

    layout_path = output_path.with_suffix(".layout.json")
    metadata = {
        "position": position,
        "size": size_key,
        "rotation": rotation,
        "opacity": opacity,
        "treatment": treatment or {"type": "none"},
        "asset_format": logo_asset_path.suffix.lower().lstrip("."),
        "asset_path": str(logo_asset_path),
    }
    layout_out = dict(layout)
    layout_out["resolved"] = {
        **metadata,
        "logoPixels": logo_pixels,
        "logoZonePixels": zone_pixels,
    }
    layout_path.write_text(json.dumps(layout_out, indent=2), encoding="utf-8")

    dbg_path = None
    if debug:
        dbg_path = debug_path or output_path.with_name(output_path.stem + "-debug.png")
        debug_img = render_svg_debug_overlay(composed, layout, logo_pixels, zone_pixels, metadata)
        debug_img.convert("RGB").save(dbg_path, "PNG")

    return SvgLayerResult(
        output_path=output_path,
        debug_path=dbg_path,
        layout_path=layout_path,
        background_path=background_path,
        logo_asset_path=logo_asset_path,
        logo_pixels=logo_pixels,
        zone_pixels=zone_pixels,
        variant="SVG",
        logo_rotation=rotation,
        logo_opacity=opacity,
        logo_treatment=treatment,
        logo_asset_format=logo_asset_path.suffix.lower().lstrip("."),
        debug_metadata=metadata,
    )
