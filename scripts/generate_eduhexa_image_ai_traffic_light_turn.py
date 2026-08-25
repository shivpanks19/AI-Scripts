#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - AI Traffic Light Turn."""
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
GREEN = (0, 180, 80)
YELLOW = (255, 200, 0)
RED = (220, 50, 50)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-ai-traffic-light-turn-aug-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 60
hex_r = 200
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

light_cx = cx
light_top = cy - 130
box_w, box_h = 100, 280
draw.rounded_rectangle(
    [light_cx - box_w // 2, light_top, light_cx + box_w // 2, light_top + box_h],
    radius=20,
    outline=BLUE,
    width=3,
    fill=(15, 15, 25),
)

for idx, color in enumerate([GREEN, YELLOW, RED]):
    ly = light_top + 35 + idx * 85
    draw.ellipse([light_cx - 32, ly - 32, light_cx + 32, ly + 32], fill=color)
    if idx == 1:
        draw.ellipse([light_cx - 38, ly - 38, light_cx + 38, ly + 38], outline=WHITE, width=3)

left_x = cx - 220
for i, label in enumerate(["G", "Y", "R"]):
    y = cy - 60 + i * 55
    colors = [GREEN, YELLOW, RED]
    draw.rounded_rectangle([left_x - 30, y - 18, left_x + 30, y + 18], radius=6, fill=colors[i])
    draw.text((left_x - 8, y - 14), label, fill=BLACK if i == 1 else WHITE)

right_x = cx + 200
lines = ["AI OK", "Tools", "Prove"]
for i, line in enumerate(lines):
    y = cy - 60 + i * 55
    draw.line([(right_x - 60, y), (right_x + 60, y)], fill=BLUE, width=2)
    draw.text((right_x - 35, y - 12), line, fill=GRAY)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(52)
font_sub = load_font(28)
font_small = load_font(22)

headline = "Green. Yellow. Red."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 95), headline, fill=WHITE, font=font_head)

sub = "Finally Clear."
bbox2 = draw.textbbox((0, 0), sub, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 160), sub, fill=BLUE, font=font_head)

tagline = "Label AI before you lecture"
bbox3 = draw.textbbox((0, 0), tagline, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 235), tagline, fill=GRAY, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox4 = draw.textbbox((0, 0), small, font=font_small)
tw4 = bbox4[2] - bbox4[0]
draw.text(((SIZE - tw4) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
