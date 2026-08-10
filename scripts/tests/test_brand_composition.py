"""Tests for deterministic brand logo composition."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.lib.image_bounds import get_visible_bbox, visible_size  # noqa: E402
from scripts.lib.layout_resolver import (  # noqa: E402
    contain_fit,
    layout_from_creative_dna,
    normalized_to_pixels,
    resolve_logo_zone,
)
from scripts.lib.logo_compositor import compose_brand_assets  # noqa: E402
from scripts.lib.logo_presets import CANVAS_PRESETS, LOGO_PRESETS, get_preset  # noqa: E402
from scripts.lib.validator import CompositionValidationError, validate_layout  # noqa: E402


def _make_logo(path: Path, size: tuple[int, int] = (400, 120), padding: int = 40) -> None:
    canvas = Image.new("RGBA", (size[0] + padding * 2, size[1] + padding * 2), (0, 0, 0, 0))
    mark = Image.new("RGBA", size, (255, 255, 255, 255))
    canvas.paste(mark, (padding, padding), mark)
    canvas.save(path)


def _make_background(path: Path, size: tuple[int, int] = (1080, 1080), color=(2, 11, 45)) -> None:
    Image.new("RGB", size, color).save(path)


class TestLogoPresets(unittest.TestCase):
    def test_all_positions_have_zones(self) -> None:
        for name, preset in LOGO_PRESETS.items():
            zone = preset["zone"]
            self.assertGreater(zone["width"], 0)
            self.assertGreater(zone["height"], 0)
            self.assertLessEqual(zone["x"] + zone["width"], 1.01)
            self.assertLessEqual(zone["y"] + zone["height"], 1.01)
            self.assertEqual(preset["anchor"], get_preset(name)["anchor"])

    def test_canvas_presets(self) -> None:
        self.assertEqual(CANVAS_PRESETS["instagram_square"]["width"], 1080)


class TestImageBounds(unittest.TestCase):
    def test_visible_bbox_strips_padding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            logo_path = Path(tmp) / "logo.png"
            _make_logo(logo_path, size=(200, 80), padding=50)
            img = Image.open(logo_path)
            bbox = get_visible_bbox(img)
            vis_w, vis_h = visible_size(img)
            self.assertEqual(vis_w, 200)
            self.assertEqual(vis_h, 80)
            self.assertGreater(bbox[0], 0)
            self.assertGreater(bbox[1], 0)


class TestLayoutResolver(unittest.TestCase):
    def test_normalized_to_pixels(self) -> None:
        px = normalized_to_pixels({"x": 0.5, "y": 0.1, "width": 0.2, "height": 0.1}, 1080, 1350)
        self.assertEqual(px["x"], 540)
        self.assertEqual(px["y"], 135)
        self.assertEqual(px["width"], 216)
        self.assertEqual(px["height"], 135)

    def test_contain_fit_preserves_aspect(self) -> None:
        w, h, scale = contain_fit(400, 100, 180, 72)
        self.assertAlmostEqual(w / h, 4.0, places=2)
        self.assertLessEqual(w, 180)
        self.assertLessEqual(h, 72)

    def test_layout_from_creative_dna(self) -> None:
        creative = {
            "_meta": {"creative_id": "test-editorial"},
            "canvas": {"width": 1080, "height": 1080, "ratio": "1:1"},
            "composition": {"zones": {"header": {"position": "top-left"}}},
        }
        brand = {
            "_meta": {"brand_id": "test"},
            "logo": {"composition": {"enabled": True, "defaultPosition": "TOP_LEFT", "defaultSize": "MEDIUM"}},
        }
        layout = layout_from_creative_dna(creative, brand)
        self.assertEqual(layout["logo"]["position"], "TOP_LEFT")
        validate_layout(layout)


class TestComposition(unittest.TestCase):
    def test_compose_end_to_end(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            logo_path = tmp_path / "logo-white.png"
            bg_path = tmp_path / "background.png"
            out_path = tmp_path / "final.png"
            brand_path = tmp_path / "BRAND_DNA.json"
            creative_path = tmp_path / "creative.CREATIVE_DNA.json"

            _make_logo(logo_path)
            _make_background(bg_path)

            brand = {
                "_meta": {"brand_id": "test", "brand_name": "Test"},
                "logo": {
                    "assets": {"light": "logo-white.png", "wordmark": "logo-white.png"},
                    "composition": {
                        "enabled": True,
                        "defaultPosition": "TOP_LEFT",
                        "defaultSize": "MEDIUM",
                        "safeMargin": 0.03,
                        "autoVariant": True,
                    },
                },
            }
            creative = {
                "_meta": {"creative_id": "test-editorial"},
                "canvas": {"width": 1080, "height": 1080, "ratio": "1:1"},
                "composition": {"zones": {"header": {"position": "top-left"}}},
            }
            brand_path.write_text(json.dumps(brand), encoding="utf-8")
            creative_path.write_text(json.dumps(creative), encoding="utf-8")

            result = compose_brand_assets(
                background_path=bg_path,
                brand_dna_path=brand_path,
                creative_dna_path=creative_path,
                output_path=out_path,
                debug=True,
            )

            self.assertTrue(out_path.exists())
            self.assertTrue(result.debug_path and result.debug_path.exists())
            self.assertTrue(result.layout_path.exists())
            self.assertEqual(result.variant, "LIGHT")

            final = Image.open(out_path)
            self.assertEqual(final.size, (1080, 1080))

    def test_multiple_canvas_formats(self) -> None:
        for preset_name, preset in CANVAS_PRESETS.items():
            with self.subTest(preset=preset_name):
                with tempfile.TemporaryDirectory() as tmp:
                    tmp_path = Path(tmp)
                    logo_path = tmp_path / "logo-white.png"
                    bg_path = tmp_path / "background.png"
                    out_path = tmp_path / "final.png"
                    brand_path = tmp_path / "BRAND_DNA.json"

                    _make_logo(logo_path)
                    _make_background(bg_path, size=(preset["width"], preset["height"]))

                    brand = {
                        "_meta": {"brand_id": "test"},
                        "logo": {
                            "assets": {"light": "logo-white.png"},
                            "composition": {
                                "enabled": True,
                                "defaultPosition": "TOP_RIGHT",
                                "defaultSize": "MEDIUM",
                            },
                        },
                    }
                    brand_path.write_text(json.dumps(brand), encoding="utf-8")
                    layout = {
                        "canvas": preset,
                        "logo": {"enabled": True, "position": "TOP_RIGHT", "size": "MEDIUM"},
                    }

                    result = compose_brand_assets(
                        background_path=bg_path,
                        brand_dna_path=brand_path,
                        output_path=out_path,
                        layout=layout,
                        write_layout=False,
                    )
                    self.assertEqual(Image.open(out_path).size, (preset["width"], preset["height"]))
                    zone = result.zone_pixels
                    self.assertGreater(zone["x"], 0)

    def test_validation_fails_on_bad_zone(self) -> None:
        with self.assertRaises(CompositionValidationError):
            validate_layout({"canvas": {"width": 1080, "height": 1080}, "logo": {"enabled": True, "position": "TOP_LEFT", "size": "MEDIUM", "zone": {"x": 2, "y": 0, "width": 0.1, "height": 0.1}}})


if __name__ == "__main__":
    unittest.main()
