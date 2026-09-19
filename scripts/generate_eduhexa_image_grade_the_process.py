#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Grade the Process."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-grade-the-process-sep-2026.png"
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

# Left: in-class paper draft stack
stack_x, stack_y = cx - 300, cy - 90
for i in range(4):
    off = i * 8
    draw.rounded_rectangle(
        [stack_x + off, stack_y + off, stack_x + 140 + off, stack_y + 180 + off],
        radius=6,
        outline=BLUE,
        width=2,
        fill=(8, 18, 40),
    )
draw.line([(stack_x + 20, stack_y + 40), (stack_x + 110, stack_y + 40)], fill=WHITE, width=2)
draw.line([(stack_x + 20, stack_y + 65), (stack_x + 95, stack_y + 65)], fill=LIGHT_BLUE, width=2)
draw.line([(stack_x + 20, stack_y + 90), (stack_x + 100, stack_y + 90)], fill=GRAY, width=2)

# Center: blocked paste icon
px, py = cx - 55, cy - 55
draw.rounded_rectangle([px, py, px + 110, py + 110], radius=12, outline=BLUE, width=3, fill=(12, 12, 18))
draw.line([(px + 25, py + 55), (px + 85, py + 55)], fill=WHITE, width=3)
draw.line([(px + 55, py + 25), (px + 55, py + 85)], fill=WHITE, width=3)
draw.line([(px + 22, py + 22), (px + 88, py + 88)], fill=(230, 70, 70), width=5)

# Right: oral explain-back waveform
wx, wy = cx + 130, cy - 70
draw.rounded_rectangle([wx, wy, wx + 210, wy + 140], radius=14, outline=BLUE, width=3, fill=(10, 25, 50))
for i, h in enumerate([20, 45, 30, 55, 25, 50, 35]):
    bx = wx + 25 + i * 24
    draw.line([(bx, wy + 100), (bx, wy + 100 - h)], fill=BLUE if i % 2 else LIGHT_BLUE, width=4)

draw.arc([cx - 220, cy - 40, cx + 220, cy + 160], start=210, end=330, fill=LIGHT_BLUE, width=3)


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

headline = "Grade the Process, Not the Paste."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 88), headline, fill=WHITE, font=font_head)

sub = "When AI detection becomes a second full-time job"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 158), sub, fill=BLUE, font=font_sub)

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
