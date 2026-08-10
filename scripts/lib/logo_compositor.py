"""Deterministic brand logo compositor — Phase 9a renderer."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

from .image_bounds import crop_to_visible, visible_size
from .layout_resolver import (
    anchor_position,
    contain_fit,
    layout_from_creative_dna,
    normalized_to_pixels,
    resolve_canvas,
    resolve_logo_zone,
)
from .validator import CompositionValidationError, validate_composition_result, validate_layout


@dataclass
class CompositionResult:
    output_path: Path
    debug_path: Path | None
    layout_path: Path
    background_path: Path
    logo_asset_path: Path
    logo_pixels: dict[str, int]
    zone_pixels: dict[str, int]
    variant: str


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _resolve_brand_root(brand_dna_path: Path) -> Path:
    return brand_dna_path.parent


def _relative_asset_path(brand_root: Path, asset_path: str) -> Path:
    path = Path(asset_path)
    if path.is_absolute():
        return path
    return (brand_root / path).resolve()


def _average_luminance(image: Image.Image, box: tuple[int, int, int, int]) -> float:
    region = image.crop(box).convert("RGB")
    pixels = list(region.getdata())
    if not pixels:
        return 0.0
    total = 0.0
    for r, g, b in pixels:
        total += 0.2126 * r + 0.7152 * g + 0.0722 * b
    return total / len(pixels)


def select_logo_variant(
    background: Image.Image,
    zone_px: dict[str, int],
    brand_dna: dict[str, Any],
    requested: str | None = None,
) -> tuple[str, Path]:
    brand_root = Path(brand_dna.get("_brand_root", "."))
    assets = brand_dna.get("logo", {}).get("assets", {})

    light = assets.get("light") or assets.get("wordmark") or assets.get("mark")
    dark = assets.get("dark")
    primary = assets.get("primary") or assets.get("wordmark") or assets.get("mark")

    if requested and requested.upper() != "AUTO":
        key = requested.lower()
        path = assets.get(key) or assets.get(requested)
        if not path:
            raise CompositionValidationError(f"Requested logo variant '{requested}' not found in brand assets")
        return requested.upper(), _relative_asset_path(brand_root, path)

    auto = brand_dna.get("logo", {}).get("composition", {}).get("autoVariant", True)
    if not auto:
        if not primary:
            raise CompositionValidationError("No primary logo asset configured")
        return "PRIMARY", _relative_asset_path(brand_root, primary)

    box = (
        zone_px["x"],
        zone_px["y"],
        zone_px["x"] + zone_px["width"],
        zone_px["y"] + zone_px["height"],
    )
    lum = _average_luminance(background, box)
    # Dark background → light logo
    if lum < 128:
        chosen = "LIGHT"
        path = light or primary
    else:
        chosen = "DARK"
        path = dark or primary
    if not path:
        raise CompositionValidationError("No suitable logo asset for background luminance")
    return chosen, _relative_asset_path(brand_root, path)


def compose_logo(
    background: Image.Image,
    logo_image: Image.Image,
    *,
    canvas_width: int,
    canvas_height: int,
    zone: dict[str, float],
    anchor: str,
    max_width_fraction: float,
    max_height_fraction: float,
) -> tuple[Image.Image, dict[str, int], dict[str, int], float, float]:
    if background.size != (canvas_width, canvas_height):
        background = background.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)

    zone_px = normalized_to_pixels(zone, canvas_width, canvas_height)
    max_w = max(1, round(max_width_fraction * canvas_width))
    max_h = max(1, round(max_height_fraction * canvas_height))

    visible = crop_to_visible(logo_image)
    vis_w, vis_h = visible.size
    original_aspect = vis_w / vis_h

    render_w, render_h, _ = contain_fit(vis_w, vis_h, max_w, max_h)
    render_aspect = render_w / render_h
    logo_resized = visible.resize((render_w, render_h), Image.Resampling.LANCZOS)

    x, y = anchor_position(zone_px, render_w, render_h, anchor)

    composed = background.convert("RGBA")
    composed.alpha_composite(logo_resized, dest=(x, y))

    # Use post-resize dimensions for aspect validation (integer rounding can drift slightly)
    final_aspect = logo_resized.width / logo_resized.height

    return composed, {"x": x, "y": y, "width": render_w, "height": render_h}, zone_px, original_aspect, final_aspect


def render_debug_overlay(
    base: Image.Image,
    layout: dict[str, Any],
    logo_pixels: dict[str, int],
    zone_pixels: dict[str, int],
) -> Image.Image:
    img = base.copy().convert("RGBA")
    draw = ImageDraw.Draw(img)

    def rect(zone: dict[str, int], outline: str, label: str) -> None:
        box = [zone["x"], zone["y"], zone["x"] + zone["width"], zone["y"] + zone["height"]]
        draw.rectangle(box, outline=outline, width=3)
        draw.text((zone["x"] + 4, zone["y"] + 4), label, fill=outline)

    canvas = layout.get("canvas", {})
    draw.text((10, 10), f"{canvas.get('width')}x{canvas.get('height')}", fill="#00FF88")

    rect(zone_pixels, "#00BFFF", "LOGO ZONE")
    rect(logo_pixels, "#FFD700", "LOGO BBOX")

    composition = layout.get("composition", {})
    cw, ch = int(canvas.get("width", img.width)), int(canvas.get("height", img.height))
    for name, zone in composition.items():
        if isinstance(zone, dict):
            rect(normalized_to_pixels(zone, cw, ch), "#FF66CC", name.upper())

    return img


def compose_brand_assets(
    *,
    background_path: Path,
    brand_dna_path: Path,
    output_path: Path,
    layout_path: Path | None = None,
    creative_dna_path: Path | None = None,
    layout: dict[str, Any] | None = None,
    debug: bool = False,
    debug_path: Path | None = None,
    write_layout: bool = True,
) -> CompositionResult:
    brand_dna = _load_json(brand_dna_path)
    brand_dna["_brand_root"] = str(_resolve_brand_root(brand_dna_path))

    if layout is None and layout_path and layout_path.exists():
        layout = _load_json(layout_path)
    elif layout is None and creative_dna_path:
        creative_dna = _load_json(creative_dna_path)
        layout = layout_from_creative_dna(creative_dna, brand_dna)
    elif layout is None:
        raise CompositionValidationError("layout, layout_path, or creative_dna_path is required")

    validate_layout(layout)

    background = Image.open(background_path).convert("RGBA")
    canvas = resolve_canvas(layout, background.width, background.height)
    cw, ch = canvas["width"], canvas["height"]

    logo_cfg = resolve_logo_zone(layout, brand_dna)
    zone_px = normalized_to_pixels(logo_cfg["zone"], cw, ch)
    variant, logo_path = select_logo_variant(
        background,
        zone_px,
        brand_dna,
        requested=layout.get("logo", {}).get("variant"),
    )

    if not logo_path.exists():
        raise CompositionValidationError(f"Logo asset not found: {logo_path}")

    logo_image = Image.open(logo_path)
    composed, logo_pixels, zone_pixels, orig_aspect, render_aspect = compose_logo(
        background,
        logo_image,
        canvas_width=cw,
        canvas_height=ch,
        zone=logo_cfg["zone"],
        anchor=logo_cfg["anchor"],
        max_width_fraction=logo_cfg["max_width"],
        max_height_fraction=logo_cfg["max_height"],
    )

    validate_composition_result(
        canvas_width=cw,
        canvas_height=ch,
        logo_x=logo_pixels["x"],
        logo_y=logo_pixels["y"],
        logo_w=logo_pixels["width"],
        logo_h=logo_pixels["height"],
        logo_source_path=str(logo_path),
        zone_px=zone_pixels,
        original_aspect=orig_aspect,
        render_aspect=render_aspect,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    composed.convert("RGB").save(output_path, "PNG")

    resolved_layout_path = layout_path or output_path.with_suffix(".layout.json")
    if write_layout:
        layout_out = dict(layout)
        layout_out.setdefault("layers", {})
        layout_out["layers"].update(
            {
                "background": str(background_path.name),
                "logo": str(logo_path.relative_to(brand_dna_path.parent))
                if logo_path.is_relative_to(brand_dna_path.parent)
                else str(logo_path),
                "export": str(output_path.name),
            }
        )
        layout_out["resolved"] = {
            "logoVariant": variant,
            "logoPixels": logo_pixels,
            "logoZonePixels": zone_pixels,
        }
        with resolved_layout_path.open("w", encoding="utf-8") as f:
            json.dump(layout_out, f, indent=2)

    dbg_path = None
    if debug:
        dbg_path = debug_path or output_path.with_name(output_path.stem + "-debug.png")
        debug_img = render_debug_overlay(composed, layout, logo_pixels, zone_pixels)
        debug_img.convert("RGB").save(dbg_path, "PNG")

    return CompositionResult(
        output_path=output_path,
        debug_path=dbg_path,
        layout_path=resolved_layout_path,
        background_path=background_path,
        logo_asset_path=logo_path,
        logo_pixels=logo_pixels,
        zone_pixels=zone_pixels,
        variant=variant,
    )
