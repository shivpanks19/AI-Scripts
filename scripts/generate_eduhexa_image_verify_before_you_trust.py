#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Verify Before You Trust."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
DARK_BLUE = (0, 40, 100)
LIGHT_BLUE = (0, 80, 200)
GREEN = (40, 200, 120)
YELLOW = (255, 200, 60)
RED = (230, 70, 70)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-verify-before-you-trust-sep-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

for cx, cy in [(100, 140), (980, 140), (100, 940), (980, 940)]:
    for i in range(8):
        angle = i * math.pi / 4
        r = 14 + i * 6
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=DARK_BLUE)

cx, cy = SIZE // 2, SIZE // 2 + 40

# Stoplight column (left)
sl_x, sl_y = cx - 280, cy - 120
draw.rounded_rectangle([sl_x, sl_y, sl_x + 70, sl_y + 200], radius=16, outline=BLUE, width=2, fill=(12, 12, 18))
for color, off in [(RED, 25), (YELLOW, 85), (GREEN, 145)]:
    draw.ellipse([sl_x + 15, sl_y + off, sl_x + 55, sl_y + off + 40], fill=color, outline=WHITE, width=1)

# Center: magnifying glass over "AI output"
mg_x, mg_y = cx - 40, cy - 80
draw.ellipse([mg_x, mg_y, mg_x + 120, mg_y + 120], outline=BLUE, width=4)
draw.line([(mg_x + 95, mg_y + 95), (mg_x + 155, mg_y + 155)], fill=BLUE, width=6)
draw.rounded_rectangle(
    [mg_x + 25, mg_y + 35, mg_x + 95, mg_y + 95],
    radius=6,
    outline=LIGHT_BLUE,
    width=2,
    fill=(8, 20, 45),
)
draw.line([(mg_x + 32, mg_y + 50), (mg_x + 88, mg_y + 50)], fill=WHITE, width=2)
draw.line([(mg_x + 32, mg_y + 65), (mg_x + 75, mg_y + 65)], fill=GRAY, width=2)
draw.text((mg_x + 38, mg_y + 72), "?", fill=YELLOW, font=None)

# Right: student explain-back bubble
bb_x, bb_y = cx + 120, cy - 100
draw.rounded_rectangle([bb_x, bb_y, bb_x + 200, bb_y + 110], radius=14, outline=BLUE, width=3, fill=(10, 25, 50))
draw.polygon([(bb_x + 30, bb_y + 108), (bb_x + 55, bb_y + 108), (bb_x + 40, bb_y + 130)], fill=(10, 25, 50))
draw.line([(bb_x + 22, bb_y + 35), (bb_x + 175, bb_y + 35)], fill=WHITE, width=2)
draw.line([(bb_x + 22, bb_y + 55), (bb_x + 160, bb_y + 55)], fill=LIGHT_BLUE, width=2)
draw.line([(bb_x + 22, bb_y + 75), (bb_x + 140, bb_y + 75)], fill=LIGHT_BLUE, width=2)

# Connecting arc
draw.arc([cx - 200, cy - 30, cx + 200, cy + 170], start=200, end=340, fill=LIGHT_BLUE, width=3)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(50)
font_sub = load_font(26)
font_small = load_font(22)

headline = "Verify Before You Trust."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 88), headline, fill=WHITE, font=font_head)

sub = "Stoplight rules need verification pedagogy"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 158), sub, fill=BLUE, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox3 = draw.textbbox((0, 0), small, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 918), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 48), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
