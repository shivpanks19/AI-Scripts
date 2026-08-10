"""Central logo placement presets — single source of truth for semantic positions."""

from __future__ import annotations

from typing import TypedDict


class Zone(TypedDict):
    x: float
    y: float
    width: float
    height: float


class LogoPreset(TypedDict):
    anchor: str
    margin: float
    zone: Zone
    max_width: float
    max_height: float


LOGO_POSITIONS = (
    "TOP_LEFT",
    "TOP_CENTER",
    "TOP_RIGHT",
    "CENTER_LEFT",
    "CENTER",
    "CENTER_RIGHT",
    "BOTTOM_LEFT",
    "BOTTOM_CENTER",
    "BOTTOM_RIGHT",
)

LOGO_SIZES = {
    "SMALL": 0.12,
    "MEDIUM": 0.17,
    "LARGE": 0.22,
}

DEFAULT_SAFE_MARGIN = 0.03


def _zone(x: float, y: float, width: float, height: float) -> Zone:
    return {"x": x, "y": y, "width": width, "height": height}


# Normalized safe zones per semantic position.
# Renderer converts these to pixels; AI prompts reference logoZone only.
LOGO_PRESETS: dict[str, LogoPreset] = {
    "TOP_LEFT": {
        "anchor": "top-left",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.03, 0.02, 0.24, 0.10),
        "max_width": 0.22,
        "max_height": 0.08,
    },
    "TOP_CENTER": {
        "anchor": "top-center",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.38, 0.02, 0.24, 0.10),
        "max_width": 0.22,
        "max_height": 0.08,
    },
    "TOP_RIGHT": {
        "anchor": "top-right",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.73, 0.02, 0.24, 0.10),
        "max_width": 0.22,
        "max_height": 0.08,
    },
    "CENTER_LEFT": {
        "anchor": "center-left",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.03, 0.42, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
    "CENTER": {
        "anchor": "center",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.38, 0.42, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
    "CENTER_RIGHT": {
        "anchor": "center-right",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.73, 0.42, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
    "BOTTOM_LEFT": {
        "anchor": "bottom-left",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.03, 0.88, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
    "BOTTOM_CENTER": {
        "anchor": "bottom-center",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.38, 0.88, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
    "BOTTOM_RIGHT": {
        "anchor": "bottom-right",
        "margin": DEFAULT_SAFE_MARGIN,
        "zone": _zone(0.73, 0.88, 0.24, 0.10),
        "max_width": 0.20,
        "max_height": 0.08,
    },
}


CANVAS_PRESETS = {
    "instagram_square": {"width": 1080, "height": 1080, "ratio": "1:1"},
    "instagram_portrait": {"width": 1080, "height": 1350, "ratio": "4:5"},
    "instagram_story": {"width": 1080, "height": 1920, "ratio": "9:16"},
    "linkedin_landscape": {"width": 1200, "height": 627, "ratio": "16:9"},
}


def resolve_size_fraction(size: str | None, brand_sizes: dict[str, float] | None = None) -> float:
    sizes = brand_sizes or LOGO_SIZES
    key = (size or "MEDIUM").upper()
    return sizes.get(key, LOGO_SIZES["MEDIUM"])


def get_preset(position: str) -> LogoPreset:
    key = position.upper().replace("-", "_")
    if key not in LOGO_PRESETS:
        raise ValueError(f"Unknown logo position: {position}. Allowed: {', '.join(LOGO_POSITIONS)}")
    return LOGO_PRESETS[key]
