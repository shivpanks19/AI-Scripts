#!/usr/bin/env python3
"""Render a 1080x1080 Swayam WhatsApp poster locally with exact on-poster copy.

Run this BEFORE calling image-function. The cloud function should receive the
locally rendered PNG URL for upload/polish — not a template thumbnail with baked text.
"""
from __future__ import annotations

import argparse
import math
import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = 1080
NAVY = (12, 42, 92)
BLUE = (0, 102, 255)
SKY = (135, 206, 250)
WHITE = (255, 255, 255)
GRAY = (120, 130, 145)
LIGHT = (232, 242, 255)


def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = (
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
        if bold
        else [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    )
    for path in names:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textlength(trial, font=font) <= width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines or [text]


def draw_centered(
    draw: ImageDraw.ImageDraw,
    y: int,
    text: str,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    max_width: int = 920,
) -> int:
    lines = wrap(draw, text, font, max_width)
    line_height = int(font.size * 1.25)
    for line in lines:
        tw = draw.textlength(line, font=font)
        draw.text(((SIZE - tw) // 2, y), line, fill=fill, font=font)
        y += line_height
    return y


def render_poster(
    headline: str,
    subline: str,
    stat: str,
    cta: str,
    footer: str = "Swayam · Infisoft Tech",
) -> Image.Image:
    img = Image.new("RGB", (SIZE, SIZE), LIGHT)
    draw = ImageDraw.Draw(img)

    # Soft gradient bands
    for y in range(SIZE):
        t = y / SIZE
        color = (
            int(LIGHT[0] * (1 - t) + 210 * t),
            int(LIGHT[1] * (1 - t) + 230 * t),
            int(LIGHT[2] * (1 - t) + 255 * t),
        )
        draw.line([(0, y), (SIZE, y)], fill=color)

    # Corner dots
    for cx, cy in [(70, 70), (1010, 70), (70, 1010), (1010, 1010)]:
        for i in range(10):
            angle = i * math.pi / 5
            r = 18 + i * 7
            x = cx + int(r * math.cos(angle))
            y = cy + int(r * math.sin(angle))
            draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(180, 210, 245))

    # Top label strip
    draw.rounded_rectangle([60, 48, SIZE - 60, 118], radius=18, fill=WHITE, outline=BLUE, width=2)
    label_font = load_font(28)
    label = "Admissions ops insight"
    lw = draw.textlength(label, font=label_font)
    draw.text(((SIZE - lw) // 2, 72), label, fill=NAVY, font=label_font)

    # Headline
    y = 150
    y = draw_centered(draw, y, headline, load_font(62), NAVY)

    # Stat block
    stat_top = 300
    draw.rounded_rectangle([80, stat_top, SIZE - 80, stat_top + 250], radius=28, fill=NAVY)
    draw.rounded_rectangle([88, stat_top + 8, SIZE - 88, stat_top + 242], radius=24, outline=SKY, width=2)
    stat_font = load_font(46)
    stat_lines = wrap(draw, stat, stat_font, 860)
    sy = stat_top + 55
    for line in stat_lines:
        tw = draw.textlength(line, font=stat_font)
        draw.text(((SIZE - tw) // 2, sy), line, fill=WHITE, font=stat_font)
        sy += int(stat_font.size * 1.2)

    # Subline
    y = draw_centered(draw, 590, subline, load_font(34, bold=False), BLUE)

    # Pipeline motif
    cx, cy = SIZE // 2, 760
    for i, alpha in enumerate([40, 70, 100, 130, 160]):
        x = cx - 180 + i * 90
        draw.ellipse([x - 18, cy - 18, x + 18, cy + 18], fill=(0, 102, 255, alpha) if False else (200, 220, 245))
        draw.ellipse([x - 12, cy - 12, x + 12, cy + 12], fill=BLUE if i >= 3 else (150, 185, 230))
        if i < 4:
            draw.line([(x + 18, cy), (x + 72, cy)], fill=BLUE, width=4)

    # CTA pill
    cta_font = load_font(34)
    cta_w = draw.textlength(cta, font=cta_font) + 80
    cta_x1 = (SIZE - cta_w) // 2
    cta_y1 = 860
    draw.rounded_rectangle([cta_x1, cta_y1, cta_x1 + cta_w, cta_y1 + 72], radius=36, fill=BLUE)
    draw.text((cta_x1 + 40, cta_y1 + 16), cta, fill=WHITE, font=cta_font)

    # Footer
    footer_font = load_font(22, bold=False)
    fw = draw.textlength(footer, font=footer_font)
    draw.text(((SIZE - fw) // 2, 980), footer, fill=GRAY, font=footer_font)

    return img


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Swayam weekly poster locally (1080x1080).")
    parser.add_argument("--headline", required=True)
    parser.add_argument("--subline", required=True)
    parser.add_argument("--stat", required=True)
    parser.add_argument("--cta", required=True)
    parser.add_argument("--slug", required=True, help="URL-safe slug used for output filename")
    parser.add_argument(
        "--out",
        default="",
        help="Output PNG path (default: docs/assets/swayam/{slug}.png)",
    )
    parser.add_argument("--footer", default="Swayam · Infisoft Tech")
    args = parser.parse_args()

    out = Path(args.out or f"docs/assets/swayam/{args.slug}.png")
    out.parent.mkdir(parents=True, exist_ok=True)

    img = render_poster(args.headline, args.subline, args.stat, args.cta, args.footer)
    img.save(out, "PNG", optimize=True)
    print(out.resolve())


if __name__ == "__main__":
    main()
