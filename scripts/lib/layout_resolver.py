"""Convert normalized layout coordinates to pixel geometry."""

from __future__ import annotations

from typing import Any

from .logo_presets import LOGO_PRESETS, get_preset, infer_layout_flow_logo_profile, resolve_size_fraction


def normalized_to_pixels(zone: dict[str, float], canvas_width: int, canvas_height: int) -> dict[str, int]:
    return {
        "x": round(zone["x"] * canvas_width),
        "y": round(zone["y"] * canvas_height),
        "width": round(zone["width"] * canvas_width),
        "height": round(zone["height"] * canvas_height),
    }


def contain_fit(
    content_width: int,
    content_height: int,
    max_width: int,
    max_height: int,
) -> tuple[int, int, float]:
    """Return render width, height, and scale using contain-fit."""
    if content_width <= 0 or content_height <= 0:
        raise ValueError("Logo visible dimensions must be positive")

    scale = min(max_width / content_width, max_height / content_height)
    render_w = max(1, round(content_width * scale))
    render_h = max(1, round(content_height * scale))
    return render_w, render_h, scale


def anchor_position(
    zone_px: dict[str, int],
    render_width: int,
    render_height: int,
    anchor: str,
) -> tuple[int, int]:
    """Place logo inside zone using anchor alignment."""
    anchor = anchor.lower()
    zx, zy, zw, zh = zone_px["x"], zone_px["y"], zone_px["width"], zone_px["height"]

    if anchor == "top-left":
        return zx, zy
    if anchor == "top-center":
        return zx + (zw - render_width) // 2, zy
    if anchor == "top-right":
        return zx + zw - render_width, zy
    if anchor == "center-left":
        return zx, zy + (zh - render_height) // 2
    if anchor == "center":
        return zx + (zw - render_width) // 2, zy + (zh - render_height) // 2
    if anchor == "center-right":
        return zx + zw - render_width, zy + (zh - render_height) // 2
    if anchor == "bottom-left":
        return zx, zy + zh - render_height
    if anchor == "bottom-center":
        return zx + (zw - render_width) // 2, zy + zh - render_height
    if anchor == "bottom-right":
        return zx + zw - render_width, zy + zh - render_height
    raise ValueError(f"Unknown anchor: {anchor}")


def apply_smart_logo_layout(
    layout: dict[str, Any],
    creative_dna: dict[str, Any] | None = None,
    brand_dna: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Adjust logo position/size/zone for layout flows with open top-right space."""
    if not creative_dna:
        return layout

    logo = layout.setdefault("logo", {})
    if logo.get("lock") or logo.get("lockPosition"):
        return layout

    profile = infer_layout_flow_logo_profile(creative_dna)
    if not profile:
        return layout

    position = str(profile["position"]).upper().replace("-", "_")
    preset = get_preset(position)
    size_key = str(profile.get("size", "LARGE")).upper()
    brand_sizes = None
    if brand_dna:
        brand_sizes = brand_dna.get("logo", {}).get("composition", {}).get("sizes")

    zone = dict(profile.get("zone") or preset["zone"])
    max_width = float(profile.get("max_width", resolve_size_fraction(size_key, brand_sizes)))
    max_height = float(profile.get("max_height", preset["max_height"]))

    logo.update(
        {
            "position": position,
            "size": size_key,
            "zone": zone,
            "maxWidth": max_width,
            "maxHeight": max_height,
            "inferred": True,
            "inferredFrom": creative_dna.get("composition", {}).get("layout_flow")
            or creative_dna.get("structure_type"),
        }
    )
    layout["logoZone"] = zone
    return layout


def resolve_logo_zone(layout: dict[str, Any], brand_dna: dict[str, Any]) -> dict[str, float]:
    """Merge layout spec logo fields with brand defaults and presets."""
    logo = layout.get("logo", {})
    if not logo.get("enabled", True):
        raise ValueError("Logo composition disabled in layout spec")

    position = (
        logo.get("position")
        or brand_dna.get("logo", {}).get("composition", {}).get("defaultPosition")
        or brand_dna.get("logo", {}).get("overlay", {}).get("placement", "TOP_RIGHT")
    )
    position = str(position).upper().replace("-", "_")

    preset = get_preset(position)
    zone = dict(logo.get("zone") or layout.get("logoZone") or preset["zone"])

    size_key = logo.get("size") or brand_dna.get("logo", {}).get("composition", {}).get("defaultSize", "MEDIUM")
    brand_sizes = brand_dna.get("logo", {}).get("composition", {}).get("sizes")
    size_fraction = resolve_size_fraction(size_key, brand_sizes)

    margin = float(
        logo.get("margin")
        or brand_dna.get("logo", {}).get("composition", {}).get("safeMargin")
        or preset["margin"]
    )

    max_width = float(logo.get("maxWidth", size_fraction))
    max_height = float(logo.get("maxHeight", preset["max_height"]))

    return {
        "position": position,
        "anchor": preset["anchor"],
        "zone": zone,
        "max_width": max_width,
        "max_height": max_height,
        "margin": margin,
        "size": str(size_key).upper(),
    }


def resolve_canvas(layout: dict[str, Any], background_width: int, background_height: int) -> dict[str, Any]:
    canvas = layout.get("canvas") or {}
    width = int(canvas.get("width") or background_width)
    height = int(canvas.get("height") or background_height)
    ratio = canvas.get("ratio")
    return {"width": width, "height": height, "ratio": ratio}


def layout_from_creative_dna(creative_dna: dict[str, Any], brand_dna: dict[str, Any]) -> dict[str, Any]:
    """Build or merge layout spec from Creative DNA + Brand DNA."""
    if "layout_spec" in creative_dna:
        layout = dict(creative_dna["layout_spec"])
        return apply_smart_logo_layout(layout, creative_dna, brand_dna)

    canvas = creative_dna.get("canvas", {})
    composition = creative_dna.get("composition", {})
    zones = composition.get("zones", {})

    brand_logo = brand_dna.get("logo", {})
    comp_rules = brand_logo.get("composition", {})

    profile = infer_layout_flow_logo_profile(creative_dna)
    if profile:
        position = str(profile["position"]).upper().replace("-", "_")
        size_key = str(profile.get("size", "LARGE")).upper()
    else:
        # Infer position from composition header zone or brand default
        position = comp_rules.get("defaultPosition", "TOP_LEFT")
        size_key = str(comp_rules.get("defaultSize", "MEDIUM")).upper()
        if zones.get("header", {}).get("position", "").startswith("top-left"):
            position = "TOP_LEFT"
        elif zones.get("header", {}).get("position", "").startswith("top-right"):
            position = "TOP_RIGHT"
        elif zones.get("footer", {}).get("position", "").startswith("bottom-right"):
            position = "BOTTOM_RIGHT"

    preset = LOGO_PRESETS[position.upper().replace("-", "_")]
    zone = dict(profile.get("zone") if profile else preset["zone"])
    max_width = float(
        profile.get("max_width", comp_rules.get("sizes", {}).get(size_key, preset["max_width"]))
        if profile
        else comp_rules.get("sizes", {}).get(size_key, preset["max_width"])
    )
    max_height = float(profile.get("max_height", preset["max_height"]) if profile else preset["max_height"])

    layout = {
        "_meta": {
            "creative_id": creative_dna.get("_meta", {}).get("creative_id"),
            "brand_id": brand_dna.get("_meta", {}).get("brand_id"),
            "source": "creative_dna",
        },
        "canvas": {
            "width": canvas.get("width", 1080),
            "height": canvas.get("height", 1080),
            "ratio": canvas.get("ratio", "1:1"),
        },
        "logo": {
            "enabled": comp_rules.get("enabled", True),
            "position": position,
            "size": size_key,
            "variant": comp_rules.get("defaultVariant", "AUTO"),
            "zone": zone,
            "maxWidth": max_width,
            "maxHeight": max_height,
            "fit": "contain",
            "margin": comp_rules.get("safeMargin", preset["margin"]),
            "inferred": bool(profile),
        },
        "logoZone": zone,
    }

    # Map known zones when present
    if zones:
        if "hero" in zones:
            layout.setdefault("composition", {})["subjectZone"] = {
                "x": 0.45,
                "y": 0.12,
                "width": 0.52,
                "height": 0.75,
            }
        if "headline" in zones:
            layout.setdefault("composition", {})["headlineZone"] = {
                "x": 0.05,
                "y": 0.12,
                "width": 0.55,
                "height": 0.20,
            }
        if "body" in zones:
            layout.setdefault("composition", {})["bodyZone"] = {
                "x": 0.05,
                "y": 0.34,
                "width": 0.55,
                "height": 0.18,
            }

    return layout
