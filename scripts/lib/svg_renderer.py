"""Render SVG logo assets at target resolution using CairoSVG."""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image


def svg_intrinsic_size(svg_path: Path) -> tuple[int, int]:
    """Parse viewBox or width/height from SVG for aspect ratio."""
    text = svg_path.read_text(encoding="utf-8")
    if 'viewBox="' in text:
        chunk = text.split('viewBox="', 1)[1].split('"', 1)[0]
        parts = chunk.replace(",", " ").split()
        if len(parts) == 4:
            return int(float(parts[2])), int(float(parts[3]))
    if 'width="' in text and 'height="' in text:
        w = text.split('width="', 1)[1].split('"', 1)[0].replace("px", "")
        h = text.split('height="', 1)[1].split('"', 1)[0].replace("px", "")
        return int(float(w)), int(float(h))
    raise ValueError(f"Cannot determine intrinsic size for SVG: {svg_path}")


def render_svg_to_image(svg_path: Path, width: int, height: int) -> Image.Image:
    """Rasterize SVG at exact pixel dimensions (vector → bitmap at compose time only)."""
    try:
        import cairosvg
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("cairosvg is required for SVG logo rendering. pip install cairosvg") from exc

    png_bytes = cairosvg.svg2png(url=str(svg_path.resolve()), output_width=width, output_height=height)
    return Image.open(io.BytesIO(png_bytes)).convert("RGBA")


def load_logo_raster(path: Path, render_width: int, render_height: int) -> Image.Image:
    """Load PNG/JPG directly or render SVG at target size."""
    suffix = path.suffix.lower()
    if suffix == ".svg":
        return render_svg_to_image(path, render_width, render_height)
    from .image_bounds import crop_to_visible

    img = Image.open(path).convert("RGBA")
    visible = crop_to_visible(img)
    return visible.resize((render_width, render_height), Image.Resampling.LANCZOS)
