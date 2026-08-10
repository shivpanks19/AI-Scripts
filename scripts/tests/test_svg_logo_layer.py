"""SVG logo layer experiment tests."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from scripts.lib.svg_logo_layer import compose_svg_experiment  # noqa: E402


class TestSvgLogoLayer(unittest.TestCase):
    def test_compose_svg_from_file(self) -> None:
        svg = _REPO / "clients/cybernetyx/references/brand-assets/cybernetyx-logo-white.svg"
        if not svg.exists():
            self.skipTest("SVG asset missing")

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bg = tmp_path / "bg.png"
            out = tmp_path / "out.png"
            Image.new("RGB", (1080, 1080), (2, 11, 45)).save(bg)

            layout = {
                "canvas": {"width": 1080, "height": 1080, "ratio": "1:1"},
                "logo": {
                    "enabled": True,
                    "position": "TOP_RIGHT",
                    "size": "MEDIUM",
                    "zone": {"x": 0.73, "y": 0.02, "width": 0.24, "height": 0.10},
                    "maxWidth": 0.17,
                    "maxHeight": 0.08,
                    "treatment": {"type": "rounded_container", "padding": 12, "cornerRadius": 10},
                },
            }

            result = compose_svg_experiment(
                background_path=bg,
                logo_asset_path=svg,
                output_path=out,
                layout=layout,
                debug=True,
            )
            self.assertTrue(out.exists())
            self.assertEqual(result.logo_asset_format, "svg")
            self.assertGreater(result.logo_pixels["width"], 0)


if __name__ == "__main__":
    unittest.main()
