#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - curriculum proof gap."""
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
AMBER = (255, 180, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-curriculum-proof-gap-aug-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"

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

left_cx = cx - 110
draw.rounded_rectangle([left_cx - 70, cy - 75, left_cx + 70, cy + 75], radius=8, outline=GRAY, width=2)
for i in range(7):
    y = cy - 55 + i * 16
    w = 90 - (i % 3) * 8
    draw.line([(left_cx - w // 2, y), (left_cx + w // 2, y)], fill=GRAY if i > 4 else WHITE, width=2)
draw.line([(left_cx - 50, cy + 45), (left_cx + 50, cy + 45)], fill=AMBER, width=3)
draw.text((left_cx - 28, cy + 52), "2019", fill=AMBER, font=None)

right_cx = cx + 110
draw.rounded_rectangle([right_cx - 70, cy - 75, right_cx + 70, cy + 75], radius=8, outline=BLUE, width=2)
draw.polygon([(right_cx - 45, cy - 35), (right_cx + 5, cy - 55), (right_cx + 45, cy - 35),
              (right_cx + 45, cy + 15), (right_cx - 45, cy + 15)], outline=BLUE, width=2)
draw.line([(right_cx - 30, cy - 15), (right_cx + 30, cy - 15)], fill=BLUE, width=2)
draw.line([(right_cx - 30, cy + 5), (right_cx + 15, cy + 5)], fill=LIGHT_BLUE, width=2)
draw.ellipse([right_cx + 25, cy - 50, right_cx + 40, cy - 35], fill=BLUE)
draw.text((right_cx - 12, cy + 52), "?", fill=BLUE, font=None)

draw.line([(left_cx + 75, cy), (right_cx - 75, cy)], fill=BLUE, width=3)
draw.polygon([(right_cx - 65, cy - 8), (right_cx - 50, cy), (right_cx - 65, cy + 8)], fill=BLUE)

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
font_sub = load_font(28)
font_small = load_font(22)

headline = "New Exams. Old Books."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 115), headline, fill=WHITE, font=font_head)

sub = "Close the curriculum proof gap before boards"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 195), sub, fill=BLUE, font=font_sub)

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
