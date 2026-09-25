#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Teacher Tools. Student Proof."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-teacher-tools-student-proof-sep-2026.png"
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
draw.rounded_rectangle([cx - 380, cy - 160, cx + 380, cy + 200], radius=16, outline=DARK_BLUE, width=2)

# Left: teacher prep + AI assist
tx, ty = cx - 340, cy - 110
draw.rounded_rectangle([tx, ty, tx + 200, ty + 180], radius=10, outline=BLUE, width=2, fill=(8, 18, 35))
draw.ellipse([tx + 75, ty + 18, tx + 125, ty + 68], outline=BLUE, width=2)
draw.line([(tx + 100, ty + 68), (tx + 100, ty + 95)], fill=BLUE, width=3)
for i, w in enumerate([120, 90, 110]):
    draw.line([(tx + 20, ty + 110 + i * 22), (tx + 20 + w, ty + 110 + i * 22)], fill=LIGHT_BLUE, width=2)
draw.text((tx + 68, ty + 155), "PREP", fill=BLUE, font=ImageFont.load_default())
draw.ellipse([tx + 155, ty + 8, tx + 195, ty + 48], outline=LIGHT_BLUE, width=2)
draw.text((tx + 168, ty + 18), "AI", fill=LIGHT_BLUE, font=ImageFont.load_default())

# Center divider
draw.line([(cx - 8, cy - 130), (cx - 8, cy + 170)], fill=GRAY, width=4)

# Right: student proof at board
bx, by = cx + 120, cy - 110
draw.rounded_rectangle([bx, by, bx + 210, by + 180], radius=10, outline=WHITE, width=2, fill=(12, 12, 16))
draw.rectangle([bx + 25, by + 25, bx + 185, by + 115], outline=BLUE, width=2)
for i, w in enumerate([100, 130, 80]):
    draw.line([(bx + 40, by + 45 + i * 22), (bx + 40 + w, by + 45 + i * 22)], fill=WHITE, width=2)
for i, h in enumerate([12, 28, 18, 32]):
    wx = bx + 30 + i * 12
    draw.line([(wx, by + 145), (wx, by + 145 - h)], fill=BLUE, width=3)
draw.text((bx + 78, by + 155), "PROOF", fill=WHITE, font=ImageFont.load_default())

# Crossed student shortcut laptop
lx, ly = cx - 55, cy + 215
draw.rounded_rectangle([lx, ly, lx + 110, ly + 70], radius=6, outline=GRAY, width=2, fill=(20, 20, 20))
draw.line([(lx + 10, ly + 10), (lx + 100, ly + 60)], fill=GRAY, width=4)
draw.text((lx + 38, ly + 28), "AI", fill=GRAY, font=ImageFont.load_default())


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
font_sub = load_font(26)
font_small = load_font(22)

headline = "Teacher Tools."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 82), headline, fill=WHITE, font=font_head)

headline2 = "Student Proof."
bbox_h2 = draw.textbbox((0, 0), headline2, font=font_head)
tw_h2 = bbox_h2[2] - bbox_h2[0]
draw.text(((SIZE - tw_h2) // 2, 142), headline2, fill=BLUE, font=font_head)

sub = "When AI stays behind the teacher, not in the shortcut"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 210), sub, fill=GRAY, font=font_sub)

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
