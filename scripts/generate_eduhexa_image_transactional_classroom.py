#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - transactional classroom."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
LIGHT_BLUE = (0, 80, 200)
DARK_BLUE = (0, 40, 100)

OUT = "/workspace/docs/assets/eduhexa/eduhexa-message-transactional-classroom-aug-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 30

left_x = cx - 200
draw.rounded_rectangle([left_x - 90, cy - 110, left_x + 90, cy + 110], radius=10, outline=BLUE, width=3)
draw.line([(left_x - 60, cy - 50), (left_x + 60, cy - 50)], fill=GRAY, width=2)
draw.line([(left_x - 60, cy - 15), (left_x + 40, cy - 15)], fill=GRAY, width=2)
draw.line([(left_x - 60, cy + 20), (left_x + 55, cy + 20)], fill=GRAY, width=2)
draw.line([(left_x - 60, cy + 55), (left_x + 25, cy + 55)], fill=GRAY, width=2)
draw.text((left_x - 35, cy + 75), "DEAL?", fill=BLUE, font=None)

right_x = cx + 200
hex_r = 75
for i in range(3):
    offset_y = cy - 80 + i * 80
    hex_pts = []
    for j in range(6):
        angle = math.pi / 6 + j * math.pi / 3
        hex_pts.append((right_x + hex_r * math.cos(angle), offset_y + hex_r * 0.5 * math.sin(angle)))
    draw.polygon(hex_pts, outline=BLUE if i == 1 else DARK_BLUE, width=2)
    if i == 1:
        draw.line([(right_x - 30, offset_y), (right_x + 30, offset_y)], fill=BLUE, width=3)

draw.line([(left_x + 95, cy), (right_x - 95, cy)], fill=BLUE, width=2)
for t in [0.3, 0.5, 0.7]:
    px = left_x + 95 + int((right_x - left_x - 190) * t)
    draw.polygon([(px, cy - 8), (px + 14, cy), (px, cy + 8)], fill=BLUE)

arc_bbox = [cx - 280, cy - 180, cx + 280, cy + 180]
draw.arc(arc_bbox, start=210, end=-30, fill=DARK_BLUE, width=2)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(48)
font_sub = load_font(28)
font_small = load_font(22)

headline = "Learning Is Supported."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 100), headline, fill=WHITE, font=font_head)

headline2 = "Not Negotiable."
bbox_h2 = draw.textbbox((0, 0), headline2, font=font_head)
tw_h2 = bbox_h2[2] - bbox_h2[0]
draw.text(((SIZE - tw_h2) // 2, 165), headline2, fill=BLUE, font=font_head)

sub = "Rebuild classroom culture before standards erode"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 245), sub, fill=GRAY, font=font_sub)

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
