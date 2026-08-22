#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - process proof shift."""
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
RED_MUTED = (180, 60, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-process-proof-shift-aug-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 30

left_cx = cx - 130
draw.rounded_rectangle([left_cx - 85, cy - 90, left_cx + 85, cy + 90], radius=10, outline=RED_MUTED, width=2)
draw.rectangle([left_cx - 60, cy - 70, left_cx + 60, cy - 45], fill=RED_MUTED)
draw.text((left_cx - 38, cy - 68), "AI DETECTOR", fill=WHITE, font=None)
for i in range(5):
    y = cy - 30 + i * 18
    w = 70 - i * 5
    draw.line([(left_cx - w, y), (left_cx + w, y)], fill=GRAY, width=2)
draw.line([(left_cx - 50, cy + 55), (left_cx - 10, cy + 55)], fill=RED_MUTED, width=3)
draw.line([(left_cx + 10, cy + 55), (left_cx + 50, cy + 55)], fill=RED_MUTED, width=3)
draw.text((left_cx - 22, cy + 62), "96%", fill=RED_MUTED, font=None)

right_cx = cx + 130
draw.rounded_rectangle([right_cx - 85, cy - 90, right_cx + 85, cy + 90], radius=10, outline=BLUE, width=2)
draw.ellipse([right_cx - 35, cy - 65, right_cx + 35, cy + 5], outline=BLUE, width=2)
draw.arc([right_cx - 25, cy - 55, right_cx + 25, cy - 5], start=200, end=340, fill=BLUE, width=2)
draw.ellipse([right_cx - 8, cy - 40, right_cx + 8, cy - 24], fill=BLUE)
draw.line([(right_cx - 30, cy + 25), (right_cx + 30, cy + 25)], fill=LIGHT_BLUE, width=2)
draw.line([(right_cx - 20, cy + 40), (right_cx + 20, cy + 40)], fill=LIGHT_BLUE, width=2)
draw.line([(right_cx - 10, cy + 55), (right_cx + 10, cy + 55)], fill=BLUE, width=2)
draw.text((right_cx - 42, cy + 62), "5-min proof", fill=BLUE, font=None)

draw.line([(left_cx + 90, cy), (right_cx - 90, cy)], fill=BLUE, width=3)
draw.polygon([(right_cx - 80, cy - 8), (right_cx - 65, cy), (right_cx - 80, cy + 8)], fill=BLUE)

hex_r = 200
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle) + 20))
draw.polygon(hex_pts, outline=DARK_BLUE, width=2)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(54)
font_sub = load_font(26)
font_small = load_font(22)

headline = "Stop Policing. Start Proving."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 115), headline, fill=WHITE, font=font_head)

sub = "Process proof replaces AI detection in classrooms"
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
