#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Learning Back in the Room."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
DARK_BLUE = (0, 40, 100)
PAPER = (245, 245, 250)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-learning-back-in-the-room-nov-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 30

hex_r = 210
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Desk / notebook inside hex
nb_x, nb_y = cx - 120, cy - 90
draw.rounded_rectangle([nb_x, nb_y, nb_x + 240, nb_y + 180], radius=8, fill=PAPER, outline=BLUE, width=2)
for i in range(6):
    ly = nb_y + 30 + i * 22
    draw.line([(nb_x + 20, ly), (nb_x + 200, ly)], fill=(200, 200, 210), width=2)
draw.line([(nb_x + 20, nb_y + 20), (nb_x + 20, nb_y + 160)], fill=(220, 60, 60), width=3)

# Pencil
draw.polygon(
    [(nb_x + 210, nb_y + 140), (nb_x + 250, nb_y + 120), (nb_x + 245, nb_y + 155)],
    fill=(255, 200, 80),
)
draw.line([(nb_x + 210, nb_y + 140), (nb_x + 250, nb_y + 120)], fill=BLUE, width=2)

# Speech bubble (oral proof)
bx, by = cx + 60, cy - 130
draw.ellipse([bx, by, bx + 90, by + 60], outline=BLUE, width=2, fill=(15, 20, 35))
draw.polygon([(bx + 25, by + 58), (bx + 15, by + 85), (bx + 45, by + 58)], fill=(15, 20, 35))
draw.text((bx + 18, by + 18), "?", fill=BLUE, font=ImageFont.load_default())

# Clock arc for in-class time
draw.arc([cx - 280, cy - 40, cx - 160, cy + 80], start=200, end=340, fill=BLUE, width=4)
draw.text((cx - 250, cy + 10), "IN-CLASS", fill=GRAY, font=ImageFont.load_default())


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
font_sub = load_font(24)
font_small = load_font(22)

line1 = "Back to the Room"
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 68), line1, fill=WHITE, font=font_head)

sub = "Witness thinking before you grade the upload"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 138), sub, fill=BLUE, font=font_sub)

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
