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
    "XL": 0.28,
}

# Layout flows where copy sits left and the hero photo occupies the right half.
# Logo belongs in the open top-right band above the hero — not the cramped top-left strip.
HERO_RIGHT_LAYOUT_FLOWS = frozenset(
    {
        "text-left-hero-right",
        "headline-left-hero-right",
    }
)

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
        # Wider band — landscape wordmarks use the open area above a right-half hero.
        "zone": _zone(0.52, 0.02, 0.44, 0.14),
        "max_width": 0.28,
        "max_height": 0.12,
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


# Per-flow logo placement tuned to match brand-editorial-full safe zones.
LAYOUT_FLOW_LOGO_PROFILES: dict[str, dict] = {
    "text-left-hero-right": {
        "position": "TOP_RIGHT",
        "size": "LARGE",
        "zone": LOGO_PRESETS["TOP_RIGHT"]["zone"],
        "max_width": LOGO_PRESETS["TOP_RIGHT"]["max_width"],
        "max_height": LOGO_PRESETS["TOP_RIGHT"]["max_height"],
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


def infer_layout_flow_logo_profile(creative_dna: dict) -> dict | None:
    """Return a layout-aware logo profile when composition leaves top-right open."""
    structure = str(creative_dna.get("structure_type", "")).lower()
    layout_template = str(creative_dna.get("_meta", {}).get("layout_template", "")).lower()
    flow = str(creative_dna.get("composition", {}).get("layout_flow", "")).lower()
    zones = creative_dna.get("composition", {}).get("zones", {}) or {}

    is_brand_editorial = structure in ("brand-editorial-full", "student-editorial-full") or layout_template in (
        "brand-editorial-full",
        "student-editorial-full",
    )
    hero_right = flow in HERO_RIGHT_LAYOUT_FLOWS

    if not hero_right and zones:
        hero_pos = str(zones.get("hero", {}).get("position", "")).lower()
        headline_pos = str(zones.get("headline", {}).get("position", "")).lower()
        hero_right = "right" in hero_pos and "left" in headline_pos

    if not (is_brand_editorial and hero_right):
        return None

    profile_key = flow if flow in LAYOUT_FLOW_LOGO_PROFILES else "text-left-hero-right"
    return dict(LAYOUT_FLOW_LOGO_PROFILES[profile_key])
