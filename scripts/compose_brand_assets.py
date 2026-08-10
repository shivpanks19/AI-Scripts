#!/usr/bin/env python3
"""Phase 9a — deterministic brand asset composition (logo overlay).

Usage:
  python scripts/compose_brand_assets.py \\
    --background clients/cybernetyx/instagram/2026-08-11/foo-background.png \\
    --brand-dna clients/cybernetyx/BRAND_DNA.json \\
    --creative-dna clients/cybernetyx/instagram/2026-08-11/foo.CREATIVE_DNA.json \\
    --output clients/cybernetyx/instagram/2026-08-11/foo.png \\
    --debug
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow running from repo root without installing a package
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.lib.logo_compositor import compose_brand_assets  # noqa: E402
from scripts.lib.validator import CompositionValidationError  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compose brand logo onto AI-generated background")
    parser.add_argument("--background", required=True, type=Path, help="AI-generated background PNG (no logo)")
    parser.add_argument("--brand-dna", required=True, type=Path, help="Path to BRAND_DNA.json")
    parser.add_argument("--output", required=True, type=Path, help="Final composed PNG output path")
    parser.add_argument("--layout", type=Path, help="Optional layout.json (overrides creative DNA inference)")
    parser.add_argument("--creative-dna", type=Path, help="Creative DNA JSON for layout inference")
    parser.add_argument("--debug", action="store_true", help="Write debug overlay PNG")
    parser.add_argument("--debug-output", type=Path, help="Debug PNG path (default: {output_stem}-debug.png)")
    parser.add_argument("--no-write-layout", action="store_true", help="Do not write/update layout.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        result = compose_brand_assets(
            background_path=args.background,
            brand_dna_path=args.brand_dna,
            output_path=args.output,
            layout_path=args.layout,
            creative_dna_path=args.creative_dna,
            debug=args.debug,
            debug_path=args.debug_output,
            write_layout=not args.no_write_layout,
        )
    except CompositionValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 — CLI should surface unexpected failures
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    summary = {
        "output": str(result.output_path),
        "debug": str(result.debug_path) if result.debug_path else None,
        "layout": str(result.layout_path),
        "background": str(result.background_path),
        "logoAsset": str(result.logo_asset_path),
        "logoVariant": result.variant,
        "logoPixels": result.logo_pixels,
        "logoZonePixels": result.zone_pixels,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
