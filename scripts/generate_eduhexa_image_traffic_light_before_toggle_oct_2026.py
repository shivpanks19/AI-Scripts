#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Traffic Light Before Toggle."""
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
RED = (220, 60, 60)
AMBER = (255, 180, 0)
GREEN = (0, 180, 90)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-traffic-light-before-toggle-oct-2026.png"
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

# Hex frame
hex_r = 200
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Traffic light left
tl_x, tl_y = cx - 200, cy - 30
draw.rounded_rectangle([tl_x - 55, tl_y - 120, tl_x + 55, tl_y + 120], radius=12, outline=BLUE, width=2, fill=(15, 15, 20))
for color, yoff, label in [(RED, -70, "STOP"), (AMBER, 0, "ASK"), (GREEN, 70, "GO")]:
    draw.ellipse([tl_x - 35, tl_y + yoff - 35, tl_x + 35, tl_y + yoff + 35], fill=color if color != AMBER else (80, 60, 0), outline=color, width=2)
    if color == GREEN:
        draw.ellipse([tl_x - 35, tl_y + yoff - 35, tl_x + 35, tl_y + yoff + 35], fill=(0, 50, 30), outline=GREEN, width=3)

# Toggle switch right (ON but unlabeled)
sw_x, sw_y = cx + 160, cy
draw.rounded_rectangle([sw_x - 90, sw_y - 50, sw_x + 90, sw_y + 50], radius=10, outline=GRAY, width=2, fill=(30, 30, 35))
draw.text((sw_x - 75, sw_y - 35), "GEMINI", fill=GRAY, font=ImageFont.load_default())
draw.text((sw_x - 75, sw_y - 15), "CLASSROOM", fill=GRAY, font=ImageFont.load_default())
draw.rounded_rectangle([sw_x + 10, sw_y - 25, sw_x + 70, sw_y + 25], radius=14, fill=BLUE)
draw.ellipse([sw_x + 45, sw_y - 18, sw_x + 68, sw_y + 18], fill=WHITE)
draw.text((sw_x + 20, sw_y + 35), "ON", fill=BLUE, font=ImageFont.load_default())

# Question marks where map should be
for qx, qy in [(cx + 20, cy - 80), (cx + 40, cy + 60), (cx - 80, cy + 90)]:
    draw.text((qx, qy), "?", fill=LIGHT_BLUE, font=ImageFont.load_default())

# Dashed line from light to switch without connecting labels
draw.line([(tl_x + 55, tl_y), (sw_x - 90, sw_y)], fill=DARK_BLUE, width=2)


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

line1 = "Traffic Light"
line2 = "Before Toggle"
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 72), line1, fill=WHITE, font=font_head)
bbox2 = draw.textbbox((0, 0), line2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 132), line2, fill=BLUE, font=font_head)

sub = "When AI switches on faster than schools publish permission"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 200), sub, fill=GRAY, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox4 = draw.textbbox((0, 0), small, font=font_small)
tw4 = bbox4[2] - bbox4[0]
draw.text(((SIZE - tw4) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT, "PNG")
print(f"Saved {OUT}")
