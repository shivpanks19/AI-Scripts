#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Explain It Aloud."""
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
RED_GRAY = (180, 70, 70)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-explain-it-aloud-sep-2026.png"
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

# Left: polished document
doc_x, doc_y = cx - 320, cy - 85
draw.rounded_rectangle(
    [doc_x, doc_y, doc_x + 130, doc_y + 170],
    radius=8,
    outline=GRAY,
    width=2,
    fill=(18, 18, 22),
)
for i, w in enumerate([90, 70, 100, 60]):
    draw.line([(doc_x + 15, doc_y + 35 + i * 22), (doc_x + 15 + w, doc_y + 35 + i * 22)], fill=GRAY, width=2)
draw.text((doc_x + 38, doc_y + 145), "✦", fill=LIGHT_BLUE)

# Center: microphone + waveform
mx, my = cx - 55, cy - 75
draw.ellipse([mx + 30, my, mx + 80, my + 70], outline=BLUE, width=3, fill=(10, 25, 50))
draw.rectangle([mx + 48, my + 68, mx + 62, my + 95], fill=BLUE)
draw.arc([mx + 35, my + 88, mx + 75, my + 118], start=0, end=180, fill=BLUE, width=3)
for i, h in enumerate([18, 42, 28, 50, 22, 45, 32]):
    bx = mx - 35 + i * 14
    draw.line([(bx, my + 115), (bx, my + 115 - h)], fill=BLUE if i % 2 else LIGHT_BLUE, width=3)

# Right: auto-grade crossed out
bx, by = cx + 170, cy - 70
draw.rounded_rectangle([bx, by, bx + 150, by + 130], radius=10, outline=GRAY, width=2, fill=(22, 12, 12))
draw.text((bx + 18, by + 42), "AUTO", fill=GRAY, font=ImageFont.load_default())
draw.text((bx + 18, by + 62), "GRADE", fill=GRAY, font=ImageFont.load_default())
draw.line([(bx + 12, by + 18), (bx + 138, by + 112)], fill=RED_GRAY, width=5)

draw.arc([cx - 240, cy - 30, cx + 240, cy + 170], start=200, end=340, fill=LIGHT_BLUE, width=3)


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
font_sub = load_font(26)
font_small = load_font(22)

headline = "Explain It Aloud."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 88), headline, fill=WHITE, font=font_head)

sub = "When written proof stops working"
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
