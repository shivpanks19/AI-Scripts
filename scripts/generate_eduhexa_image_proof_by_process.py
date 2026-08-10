#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - proof-by-process-aug-2026."""
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
RED_DIM = (180, 60, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-proof-by-process-aug-2026.png"
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

def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

font_tiny = load_font(18)
font_small = load_font(22)
font_sub = load_font(30)
font_head = load_font(56)
font_label = load_font(28)

# Left: broken detector
left_cx = cx - 200
draw.rounded_rectangle([left_cx - 90, cy - 100, left_cx + 90, cy + 100], radius=10, outline=GRAY, width=2)
draw.text((left_cx - 72, cy - 85), "AI DETECTOR", fill=GRAY, font=font_tiny)
draw.line([(left_cx - 60, cy - 20), (left_cx + 60, cy + 40)], fill=RED_DIM, width=4)
draw.line([(left_cx + 60, cy - 20), (left_cx - 60, cy + 40)], fill=RED_DIM, width=4)
for i, (dx, dy) in enumerate([(-40, -50), (30, -30), (-20, 40), (45, 55)]):
    draw.polygon([(left_cx + dx, cy + dy - 8), (left_cx + dx + 6, cy + dy + 4), (left_cx + dx - 6, cy + dy + 4)], fill=RED_DIM)

# Arrow
draw.polygon([(cx - 30, cy), (cx + 30, cy - 20), (cx + 30, cy + 20)], fill=BLUE)
draw.line([(cx - 80, cy), (cx - 30, cy)], fill=BLUE, width=4)

# Right: process proof hexagon
right_cx = cx + 200
hex_r = 110
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((right_cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Draft doc
draw.rounded_rectangle([right_cx - 55, cy - 70, right_cx + 15, cy - 10], radius=4, outline=BLUE, width=2)
for i in range(3):
    draw.line([(right_cx - 48, cy - 58 + i * 14), (right_cx + 8, cy - 58 + i * 14)], fill=LIGHT_BLUE, width=2)

# Pencil edit marks
draw.line([(right_cx + 25, cy - 50), (right_cx + 45, cy - 30)], fill=BLUE, width=3)
draw.ellipse([right_cx + 40, cy - 35, right_cx + 50, cy - 25], fill=BLUE)

# Speech bubble
draw.rounded_rectangle([right_cx - 50, cy + 5, right_cx + 55, cy + 55], radius=8, outline=BLUE, width=2)
draw.text((right_cx - 42, cy + 15), "Explain", fill=WHITE, font=font_tiny)
draw.text((right_cx - 42, cy + 32), "thinking", fill=BLUE, font=font_tiny)

# Supervised desk
draw.rectangle([right_cx - 30, cy + 65, right_cx + 30, cy + 78], fill=DARK_BLUE, outline=BLUE, width=1)

headline = "Proof by Process."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 110), headline, fill=WHITE, font=font_head)

headline2 = "Not Detection."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 175), headline2, fill=BLUE, font=font_head)

sub = "When surveillance fails, thinking must be visible"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 250), sub, fill=GRAY, font=font_sub)

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
