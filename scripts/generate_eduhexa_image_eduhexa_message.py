#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - API test."""
from PIL import Image, ImageDraw, ImageFont
import math
import os
import random

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
LIGHT_BLUE = (0, 80, 200)
DARK_BLUE = (0, 40, 100)

OUT = "/workspace/docs/assets/eduhexa/eduhexa-message-neet-rank-compression-aug-2026.png"
LOGO = "/workspace/docs/eduhexa logo.png"

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

for cx, cy in [(80, 80), (1000, 80), (80, 1000), (1000, 1000)]:
    for i in range(12):
        angle = i * math.pi / 6
        r = 20 + i * 8
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=DARK_BLUE)

cx, cy = SIZE // 2, SIZE // 2 + 40
hex_r = 220
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)
draw.line([(cx, cy - hex_r), (cx, cy + hex_r)], fill=BLUE, width=2)

left_cx = cx - 95
draw.rounded_rectangle([left_cx - 70, cy - 80, left_cx + 70, cy + 90], radius=8, outline=BLUE, width=2)
draw.polygon([(left_cx + 55, cy - 40), (left_cx + 70, cy - 10), (left_cx + 40, cy - 10)], fill=BLUE)
draw.line([(left_cx + 55, cy - 10), (left_cx + 55, cy + 20)], fill=BLUE, width=3)

right_cx = cx + 95
for i in range(8):
    y = cy - 70 + i * 18
    width = 80 - i * 4
    draw.line([(right_cx - width // 2, y), (right_cx + width // 2, y)], fill=GRAY if i < 5 else BLUE, width=2)

random.seed(42)
for _ in range(35):
    dx = random.randint(-50, 50)
    dy = random.randint(-30, 50)
    draw.ellipse([right_cx + dx - 3, cy + dy - 3, right_cx + dx + 3, cy + dy + 3],
                 fill=BLUE if random.random() > 0.5 else LIGHT_BLUE)

arc_bbox = [cx - 160, cy - 100, cx + 160, cy + 100]
draw.arc(arc_bbox, start=200, end=-20, fill=BLUE, width=3)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(58)
font_sub = load_font(30)
font_small = load_font(22)
font_label = load_font(36)

headline = "Marks Lie. Ranks Decide."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 115), headline, fill=WHITE, font=font_head)

sub = "Counsel on ranks before August counselling opens"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 195), sub, fill=BLUE, font=font_sub)

draw.text((left_cx - 28, cy - 20), "650", fill=WHITE, font=font_label)
draw.text((right_cx - 28, cy + 70), "AIR", fill=GRAY, font=font_small)

small = "EduHexa — eduhexa-message"
bbox3 = draw.textbbox((0, 0), small, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
