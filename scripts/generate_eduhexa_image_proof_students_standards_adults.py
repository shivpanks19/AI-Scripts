#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Proof for Students, Standards for Adults."""
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
MUTED = (45, 45, 55)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-proof-students-standards-adults-oct-2026.png"
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
draw.rounded_rectangle([cx - 320, cy - 200, cx + 320, cy + 200], radius=18, outline=BLUE, width=2)

# Top: adult AI slop panel
top_y = cy - 175
draw.rounded_rectangle([cx - 280, top_y, cx + 280, top_y + 150], radius=10, outline=GRAY, width=2, fill=MUTED)
draw.text((cx - 250, top_y + 12), "ADULT OUTPUT", fill=GRAY, font=ImageFont.load_default())
for row in range(4):
    y = top_y + 45 + row * 22
    draw.line([(cx - 240, y), (cx + 200, y)], fill=(90, 90, 100), width=2)
draw.ellipse([cx + 210, top_y + 50, cx + 250, top_y + 90], outline=LIGHT_BLUE, width=2)
draw.text((cx + 218, top_y + 62), "AI", fill=LIGHT_BLUE, font=ImageFont.load_default())

# Divider
draw.line([(cx - 280, cy - 10), (cx + 280, cy - 10)], fill=WHITE, width=3)

# Bottom: student in-class proof
bot_y = cy + 15
draw.rounded_rectangle([cx - 280, bot_y, cx + 280, bot_y + 160], radius=10, outline=BLUE, width=3, fill=(8, 20, 45))
draw.text((cx - 250, bot_y + 12), "STUDENT PROOF", fill=BLUE, font=ImageFont.load_default())
for i, w in enumerate([80, 110, 95]):
    px = cx - 220 + i * 75
    draw.rounded_rectangle([px, bot_y + 50, px + 60, bot_y + 95], radius=4, outline=WHITE, width=2)
draw.ellipse([cx + 195, bot_y + 55, cx + 245, bot_y + 105], outline=BLUE, width=2)
draw.line([(cx + 220, bot_y + 70), (cx + 220, bot_y + 90)], fill=BLUE, width=2)
draw.line([(cx + 210, bot_y + 80), (cx + 230, bot_y + 80)], fill=BLUE, width=2)


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

line1 = "Proof for Students."
line2 = "Standards for Adults."
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 78), line1, fill=WHITE, font=font_head)
bbox2 = draw.textbbox((0, 0), line2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 138), line2, fill=BLUE, font=font_head)

sub = "When AI slop and in-class integrity collide"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 198), sub, fill=GRAY, font=font_sub)

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
