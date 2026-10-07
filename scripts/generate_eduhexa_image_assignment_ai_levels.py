#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Assignment AI Levels."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
DARK_BLUE = (0, 40, 100)
MUTED = (45, 45, 55)
BAND_COLORS = [
    ((90, 30, 30), "L0", "No AI"),
    ((40, 55, 90), "L1", "Prep only"),
    ((20, 70, 120), "L2", "Disclose"),
    ((8, 45, 110), "L3", "Integrated"),
]

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-assignment-ai-levels-oct-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 55
draw.rounded_rectangle([cx - 330, cy - 230, cx + 330, cy + 230], radius=20, outline=BLUE, width=2)

band_h = 95
start_y = cy - 200
for i, (fill, label, desc) in enumerate(BAND_COLORS):
    y0 = start_y + i * (band_h + 8)
    draw.rounded_rectangle([cx - 290, y0, cx + 290, y0 + band_h], radius=10, outline=BLUE if i == 3 else GRAY, width=2 if i == 3 else 1, fill=fill)
    draw.ellipse([cx - 270, y0 + 28, cx - 220, y0 + 78], outline=WHITE, width=2)
    draw.text((cx - 255, y0 + 42), label, fill=WHITE, font=ImageFont.load_default())
    draw.text((cx - 190, y0 + 32), desc, fill=WHITE, font=ImageFont.load_default())
    draw.line([(cx - 40, y0 + 48), (cx + 250, y0 + 48)], fill=(200, 200, 210), width=2)
    draw.line([(cx - 40, y0 + 62), (cx + 200, y0 + 62)], fill=(140, 140, 150), width=2)

draw.rounded_rectangle([cx - 290, cy + 175, cx + 290, cy + 215], radius=8, outline=GRAY, width=1, fill=MUTED)
draw.text((cx - 260, cy + 188), "DEFAULT LEVEL IF UNLABELED →", fill=GRAY, font=ImageFont.load_default())
draw.text((cx + 40, cy + 188), "L0 / L1", fill=BLUE, font=ImageFont.load_default())


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(48)
font_sub = load_font(26)
font_small = load_font(22)

line1 = "State the AI Level."
line2 = "Every Assignment."
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 72), line1, fill=WHITE, font=font_head)
bbox2 = draw.textbbox((0, 0), line2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 128), line2, fill=BLUE, font=font_head)

sub = "Label the task before the browser opens"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 188), sub, fill=GRAY, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox4 = draw.textbbox((0, 0), small, font=font_small)
tw4 = bbox4[2] - bbox4[0]
draw.text(((SIZE - tw4) // 2, 918), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 48), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
