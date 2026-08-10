"""Programmatic logo container treatments — SVG asset unchanged."""

from __future__ import annotations

from typing import Any

from PIL import Image, ImageDraw


def apply_logo_treatment(logo: Image.Image, treatment: dict[str, Any] | None) -> Image.Image:
    if not treatment or treatment.get("type", "none") == "none":
        return logo

    t_type = treatment.get("type", "none")
    padding = int(treatment.get("padding", 16))
    corner_radius = int(treatment.get("cornerRadius", treatment.get("corner_radius", 12)))
    opacity = float(treatment.get("opacity", 1.0))

    pad_logo = logo.copy()
    if opacity < 1.0:
        alpha = pad_logo.getchannel("A")
        alpha = alpha.point(lambda p: int(p * opacity))
        pad_logo.putalpha(alpha)

    lw, lh = pad_logo.size
    canvas = Image.new("RGBA", (lw + padding * 2, lh + padding * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    box = [0, 0, canvas.width - 1, canvas.height - 1]
    if t_type == "white_container":
        fill = (255, 255, 255, int(255 * opacity))
    elif t_type == "dark_container":
        fill = (2, 11, 45, int(220 * opacity))
    elif t_type == "rounded_container":
        fill = (7, 22, 66, int(200 * opacity))
    else:
        fill = None

    if fill:
        draw.rounded_rectangle(box, radius=corner_radius, fill=fill)

    canvas.alpha_composite(pad_logo, dest=(padding, padding))
    return canvas
