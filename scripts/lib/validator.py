"""Validation for layout specs and composed creatives."""

from __future__ import annotations

from typing import Any

from .logo_presets import LOGO_POSITIONS, LOGO_SIZES


class CompositionValidationError(Exception):
  pass


def _in_range(value: float, name: str) -> None:
    if value < 0 or value > 1:
        raise CompositionValidationError(f"{name} must be between 0 and 1, got {value}")


def validate_zone(zone: dict[str, float], name: str) -> None:
    for key in ("x", "y", "width", "height"):
        if key not in zone:
            raise CompositionValidationError(f"{name} missing '{key}'")
        _in_range(float(zone[key]), f"{name}.{key}")
    if zone["width"] <= 0 or zone["height"] <= 0:
        raise CompositionValidationError(f"{name} width/height must be positive")


def validate_layout(layout: dict[str, Any]) -> None:
    canvas = layout.get("canvas")
    if not canvas:
        raise CompositionValidationError("layout.canvas is required")
    if int(canvas.get("width", 0)) <= 0 or int(canvas.get("height", 0)) <= 0:
        raise CompositionValidationError("layout.canvas width/height must be positive")

    logo = layout.get("logo", {})
    if logo.get("enabled", True):
        position = str(logo.get("position", "TOP_LEFT")).upper().replace("-", "_")
        if position not in LOGO_POSITIONS:
            raise CompositionValidationError(f"Invalid logo.position: {position}")
        size = str(logo.get("size", "MEDIUM")).upper()
        if size not in LOGO_SIZES:
            raise CompositionValidationError(f"Invalid logo.size: {size}")
        zone = logo.get("zone") or layout.get("logoZone")
        if zone:
            validate_zone(zone, "logo.zone")

    composition = layout.get("composition", {})
    for zone_name, zone in composition.items():
        if isinstance(zone, dict):
            validate_zone(zone, f"composition.{zone_name}")


def validate_composition_result(
    *,
    canvas_width: int,
    canvas_height: int,
    logo_x: int,
    logo_y: int,
    logo_w: int,
    logo_h: int,
    logo_source_path: str,
    zone_px: dict[str, int],
    original_aspect: float,
    render_aspect: float,
    tolerance: float = 0.05,
) -> None:
    if not logo_source_path:
        raise CompositionValidationError("Logo asset path is required")

    if logo_w <= 0 or logo_h <= 0:
        raise CompositionValidationError("Rendered logo dimensions must be positive")

    if original_aspect <= 0 or render_aspect <= 0:
        raise CompositionValidationError("Invalid logo aspect ratio")

    relative_delta = abs(original_aspect - render_aspect) / original_aspect
    if relative_delta > tolerance:
        raise CompositionValidationError(
            f"Logo aspect ratio changed: original={original_aspect:.4f}, render={render_aspect:.4f}, delta={relative_delta:.4f}"
        )

    if logo_x < 0 or logo_y < 0 or logo_x + logo_w > canvas_width or logo_y + logo_h > canvas_height:
        raise CompositionValidationError("Logo extends outside canvas bounds")

    zx, zy, zw, zh = zone_px["x"], zone_px["y"], zone_px["width"], zone_px["height"]
    if logo_x < zx - 2 or logo_y < zy - 2:
        raise CompositionValidationError("Logo placed outside safe zone (top-left)")
    if logo_x + logo_w > zx + zw + 2 or logo_y + logo_h > zy + zh + 2:
        raise CompositionValidationError("Logo placed outside safe zone (bottom-right)")
