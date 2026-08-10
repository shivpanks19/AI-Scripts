#!/usr/bin/env python3
"""Experimental runner — SVG logo as first-class design layer.

Isolated from production Phase 9a. Does not modify the main pipeline flow.

Usage:
  .venv/bin/python experiments/svg-logo-layer/run_svg_logo_experiment.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from scripts.lib.layout_resolver import layout_from_creative_dna  # noqa: E402
from scripts.lib.logo_presets import LOGO_PRESETS, LOGO_SIZES  # noqa: E402
from scripts.lib.svg_logo_layer import compose_svg_experiment  # noqa: E402

CLIENT = "cybernetyx"
RUN_DATE = "2026-08-11"
SLUG = "teacher-most-important-technology-editorial"
BACKGROUND = _REPO / f"clients/{CLIENT}/instagram/{RUN_DATE}/{SLUG}-background.png"
CREATIVE_DNA = _REPO / f"clients/{CLIENT}/instagram/{RUN_DATE}/{SLUG}.CREATIVE_DNA.json"
BRAND_DNA = _REPO / f"clients/{CLIENT}/BRAND_DNA.json"
SVG_LOGO = _REPO / f"clients/{CLIENT}/references/brand-assets/cnx-white-logo.svg"
OUT_DIR = _REPO / f"clients/{CLIENT}/experiments/svg-logo-layer/{RUN_DATE}/{SLUG}"
AI_LOGO_GIT_REF = "1b424bd:clients/cybernetyx/instagram/2026-08-11/teacher-most-important-technology-editorial.png"

POSITIONS = ["TOP_LEFT", "TOP_RIGHT", "CENTER", "BOTTOM_LEFT", "BOTTOM_RIGHT"]
SIZES = ["SMALL", "MEDIUM", "LARGE"]


def _base_layout(position: str, size: str, treatment: dict | None = None) -> dict:
    preset = LOGO_PRESETS[position]
    return {
        "canvas": {"width": 1080, "height": 1080, "ratio": "1:1"},
        "logo": {
            "enabled": True,
            "asset": str(SVG_LOGO.relative_to(_REPO)),
            "position": position,
            "size": size,
            "rotation": 0,
            "opacity": 1,
            "zone": preset["zone"],
            "maxWidth": LOGO_SIZES[size],
            "maxHeight": preset["max_height"],
            "fit": "contain",
            "treatment": treatment or {"type": "none"},
        },
        "logoZone": preset["zone"],
        "composition": {
            "subjectZone": {"x": 0.45, "y": 0.12, "width": 0.52, "height": 0.75},
            "headlineZone": {"x": 0.05, "y": 0.12, "width": 0.55, "height": 0.22},
        },
    }


def _export_ai_logo_baseline(dest: Path) -> None:
    proc = subprocess.run(
        ["git", "show", AI_LOGO_GIT_REF],
        cwd=_REPO,
        capture_output=True,
        check=False,
    )
    if proc.returncode == 0:
        dest.write_bytes(proc.stdout)
    else:
        # fallback: current PNG if git ref unavailable
        shutil.copy2(_REPO / f"clients/{CLIENT}/instagram/{RUN_DATE}/{SLUG}.png", dest)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if not BACKGROUND.exists():
        print(f"Missing background: {BACKGROUND}", file=sys.stderr)
        return 1
    if not SVG_LOGO.exists():
        print(f"Missing SVG logo: {SVG_LOGO}", file=sys.stderr)
        return 1
    if not CREATIVE_DNA.exists():
        print(f"Missing creative DNA: {CREATIVE_DNA}", file=sys.stderr)
        return 1
    if not BRAND_DNA.exists():
        print(f"Missing brand DNA: {BRAND_DNA}", file=sys.stderr)
        return 1

    creative_dna = json.loads(CREATIVE_DNA.read_text(encoding="utf-8"))
    brand_dna = json.loads(BRAND_DNA.read_text(encoding="utf-8"))
    smart_layout = layout_from_creative_dna(creative_dna, brand_dna)
    smart_layout.setdefault("logo", {})["asset"] = str(SVG_LOGO.relative_to(_REPO))

    shutil.copy2(BACKGROUND, OUT_DIR / "background.png")
    _export_ai_logo_baseline(OUT_DIR / "existing-ai-logo.png")

    manifest: dict = {
        "experiment": "svg-logo-layer",
        "client": CLIENT,
        "slug": SLUG,
        "background": str(BACKGROUND.relative_to(_REPO)),
        "svg_asset": str(SVG_LOGO.relative_to(_REPO)),
        "outputs": [],
    }

    # Primary comparison: layout-aware defaults from Creative DNA (TOP_RIGHT + LARGE for hero-right flows)
    primary_out = OUT_DIR / "svg-composited-logo.png"
    primary = compose_svg_experiment(
        background_path=BACKGROUND,
        logo_asset_path=SVG_LOGO,
        output_path=primary_out,
        layout=smart_layout,
        creative_dna=creative_dna,
        brand_dna=brand_dna,
        debug=True,
        debug_path=OUT_DIR / "svg-composited-logo-debug.png",
    )
    manifest["primary"] = {
        "output": str(primary_out.relative_to(_REPO)),
        "layout": json.loads(primary.layout_path.read_text()),
        "logoPixels": primary.logo_pixels,
        "logoZonePixels": primary.zone_pixels,
    }

    # Placement grid
    for position in POSITIONS:
        for size in SIZES:
            name = f"svg-{position.lower()}-{size.lower()}.png"
            out = OUT_DIR / name
            result = compose_svg_experiment(
                background_path=BACKGROUND,
                logo_asset_path=SVG_LOGO,
                output_path=out,
                layout=_base_layout(position, size),
                debug=False,
            )
            manifest["outputs"].append(
                {
                    "file": name,
                    "position": position,
                    "size": size,
                    "logoPixels": result.logo_pixels,
                    "zonePixels": result.zone_pixels,
                }
            )

    # Treatment tests on TOP_RIGHT MEDIUM
    for treatment_type in ["white_container", "dark_container", "rounded_container"]:
        tname = f"svg-top_right-medium-{treatment_type}.png"
        layout = _base_layout(
            "TOP_RIGHT",
            "MEDIUM",
            treatment={"type": treatment_type, "padding": 18, "cornerRadius": 16, "opacity": 0.92},
        )
        result = compose_svg_experiment(
            background_path=BACKGROUND,
            logo_asset_path=SVG_LOGO,
            output_path=OUT_DIR / tname,
            layout=layout,
            debug=True,
            debug_path=OUT_DIR / tname.replace(".png", "-debug.png"),
        )
        manifest["outputs"].append(
            {
                "file": tname,
                "position": "TOP_RIGHT",
                "size": "MEDIUM",
                "treatment": treatment_type,
                "logoPixels": result.logo_pixels,
            }
        )

    manifest_path = OUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(json.dumps({"outDir": str(OUT_DIR.relative_to(_REPO)), "manifest": str(manifest_path.relative_to(_REPO))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
