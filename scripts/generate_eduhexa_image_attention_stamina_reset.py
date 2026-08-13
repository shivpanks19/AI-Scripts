#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - attention stamina reset."""
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
RED_DIM = (180, 60, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-attention-stamina-reset-aug-2026.png"
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
draw.rounded_rectangle([left_cx - 75, cy - 55, left_cx + 75, cy + 45], radius=8, outline=GRAY, width=2)
draw.line([left_cx - 55, cy - 25, left_cx + 55, cy + 25], fill=RED_DIM, width=4)
draw.line([left_cx + 55, cy - 25, left_cx - 55, cy + 25], fill=RED_DIM, width=4)
for i, dy in enumerate([-35, -10, 15]):
    draw.ellipse([left_cx + 60 + i * 12, cy - 50 + dy, left_cx + 68 + i * 12, cy - 42 + dy], fill=BLUE)
draw.rounded_rectangle([left_cx - 30, cy + 55, left_cx + 30, cy + 75], radius=4, outline=GRAY, width=1)
draw.text((left_cx - 22, cy + 58), "AI", fill=GRAY, font=None)

right_cx = cx + 110
draw.rectangle([right_cx - 65, cy - 70, right_cx + 65, cy + 80], outline=BLUE, width=2)
for i in range(6):
    y = cy - 55 + i * 18
    w = 50 + (i % 3) * 10
    draw.line([(right_cx - w // 2, y), (right_cx + w // 2, y)], fill=WHITE if i < 4 else GRAY, width=2)
draw.line([(right_cx - 40, cy + 55), (right_cx + 20, cy + 70)], fill=BLUE, width=2)
draw.ellipse([right_cx + 15, cy + 62, right_cx + 25, cy + 72], fill=BLUE)

clock_r = 35
for i in range(12):
    angle = i * math.pi / 6 - math.pi / 2
    x1 = right_cx + int((clock_r - 5) * math.cos(angle))
    y1 = cy - 85 + int((clock_r - 5) * math.sin(angle))
    x2 = right_cx + int(clock_r * math.cos(angle))
    y2 = cy - 85 + int(clock_r * math.sin(angle))
    draw.line([(x1, y1), (x2, y2)], fill=BLUE, width=2)
draw.ellipse([right_cx - clock_r, cy - 85 - clock_r, right_cx + clock_r, cy - 85 + clock_r], outline=BLUE, width=2)
draw.line([(right_cx, cy - 85), (right_cx, cy - 85 - 20)], fill=WHITE, width=3)
draw.line([(right_cx, cy - 85), (right_cx + 15, cy - 85)], fill=BLUE, width=2)

draw.line([(left_cx + 80, cy), (right_cx - 80, cy)], fill=BLUE, width=3)
draw.polygon([(right_cx - 70, cy - 8), (right_cx - 55, cy), (right_cx - 70, cy + 8)], fill=BLUE)

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


font_head = load_font(56)
font_sub = load_font(28)
font_small = load_font(22)

headline1 = "Build Stamina."
bbox = draw.textbbox((0, 0), headline1, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 115), headline1, fill=WHITE, font=font_head)

headline2 = "Not Just Ban Screens."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 180), headline2, fill=BLUE, font=font_head)

sub = "Device rules reduce noise — depth must be designed"
bbox3 = draw.textbbox((0, 0), sub, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 255), sub, fill=GRAY, font=font_small)

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
