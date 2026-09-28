#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Students Push Back. Paper Proves It."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-student-pushback-paper-proof-sep-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 50

draw.rounded_rectangle([cx - 400, cy - 170, cx + 400, cy + 210], radius=16, outline=DARK_BLUE, width=2)

# Left: district mandate slide with AI badge
lx, ly = cx - 360, cy - 130
draw.rounded_rectangle([lx, ly, lx + 220, ly + 200], radius=10, outline=GRAY, width=2, fill=(10, 10, 14))
for i, w in enumerate([160, 140, 170]):
    draw.line([(lx + 25, ly + 35 + i * 28), (lx + 25 + w, ly + 35 + i * 28)], fill=GRAY, width=2)
draw.ellipse([lx + 155, ly + 145, lx + 205, ly + 175], outline=BLUE, width=2)
draw.text((lx + 168, ly + 150), "AI", fill=BLUE, font=ImageFont.load_default())
draw.text((lx + 55, ly + 178), "MANDATE", fill=GRAY, font=ImageFont.load_default())

# Center: student pushback speech bubble
bx, by = cx - 30, cy - 150
draw.ellipse([bx, by, bx + 120, by + 80], outline=WHITE, width=2, fill=(18, 18, 22))
draw.polygon([(bx + 40, by + 78), (bx + 55, by + 105), (bx + 70, by + 78)], fill=(18, 18, 22), outline=WHITE)
draw.text((bx + 28, by + 28), "NO", fill=WHITE, font=ImageFont.load_default())

# Right: paper notebook proof
rx, ry = cx + 140, cy - 130
draw.rounded_rectangle([rx, ry, rx + 220, ry + 200], radius=10, outline=WHITE, width=2, fill=(245, 245, 248))
draw.line([(rx + 30, ry + 25), (rx + 190, ry + 25)], fill=BLUE, width=3)
for i, w in enumerate([130, 150, 110, 140]):
    draw.line([(rx + 30, ry + 55 + i * 32), (rx + 30 + w, ry + 55 + i * 32)], fill=(40, 40, 45), width=2)
draw.line([(rx + 15, ry + 20), (rx + 15, ry + 185)], fill=LIGHT_BLUE, width=2)
draw.text((rx + 72, ry + 168), "PROOF", fill=BLUE, font=ImageFont.load_default())

# Crossed phone shortcut
px, py = cx - 70, cy + 230
draw.rounded_rectangle([px, py, px + 90, py + 55], radius=8, outline=GRAY, width=2, fill=(15, 15, 15))
draw.line([(px + 8, py + 8), (px + 82, py + 47)], fill=GRAY, width=4)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(46)
font_sub = load_font(24)
font_small = load_font(22)

headline = "Students Push Back."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 78), headline, fill=WHITE, font=font_head)

headline2 = "Paper Proves It."
bbox_h2 = draw.textbbox((0, 0), headline2, font=font_head)
tw_h2 = bbox_h2[2] - bbox_h2[0]
draw.text(((SIZE - tw_h2) // 2, 132), headline2, fill=BLUE, font=font_head)

sub = "When mandates outrun classroom trust"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 198), sub, fill=GRAY, font=font_sub)

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
