#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Syllabus-First Era."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-syllabus-first-aug-2026.png"
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
hex_r = 200
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

doc_x, doc_y = cx - 120, cy - 60
doc_w, doc_h = 240, 300
draw.rounded_rectangle(
    [doc_x, doc_y, doc_x + doc_w, doc_y + doc_h],
    radius=12,
    outline=BLUE,
    width=3,
    fill=(12, 12, 18),
)
draw.line([(doc_x + 30, doc_y + 50), (doc_x + doc_w - 30, doc_y + 50)], fill=GRAY, width=2)
draw.line([(doc_x + 30, doc_y + 85), (doc_x + doc_w - 30, doc_y + 85)], fill=GRAY, width=2)
draw.line([(doc_x + 30, doc_y + 120), (doc_x + doc_w - 50, doc_y + 120)], fill=GRAY, width=2)

ai_line_y = doc_y + 155
draw.rounded_rectangle(
    [doc_x + 25, ai_line_y, doc_x + doc_w - 25, ai_line_y + 55],
    radius=8,
    outline=BLUE,
    width=2,
    fill=(0, 30, 70),
)
draw.line([(doc_x + 40, ai_line_y + 18), (doc_x + doc_w - 40, ai_line_y + 18)], fill=BLUE, width=3)
draw.line([(doc_x + 40, ai_line_y + 35), (doc_x + doc_w - 70, ai_line_y + 35)], fill=LIGHT_BLUE, width=2)

shield_x = cx + 170
shield_y = cy - 20
draw.polygon(
    [
        (shield_x, shield_y - 50),
        (shield_x + 45, shield_y - 30),
        (shield_x + 45, shield_y + 20),
        (shield_x, shield_y + 55),
        (shield_x - 45, shield_y + 20),
        (shield_x - 45, shield_y - 30),
    ],
    outline=GRAY,
    width=2,
)
draw.line([(shield_x - 20, shield_y), (shield_x - 5, shield_y + 15), (shield_x + 22, shield_y - 18)], fill=GRAY, width=3)

pen_x = cx + 155
pen_y = cy + 100
draw.line([(pen_x, pen_y), (pen_x + 60, pen_y - 40)], fill=BLUE, width=4)
draw.ellipse([pen_x + 52, pen_y - 48, pen_x + 68, pen_y - 32], fill=BLUE)


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
font_sub = load_font(28)
font_small = load_font(22)
font_tag = load_font(24)

headline = "Write the Line."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 85), headline, fill=WHITE, font=font_head)

headline2 = "Not the Lecture."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 145), headline2, fill=BLUE, font=font_head)

tagline = "Syllabus-first AI governance for school leaders"
bbox3 = draw.textbbox((0, 0), tagline, font=font_tag)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 215), tagline, fill=GRAY, font=font_tag)

doc_label = "SYLLABUS"
bbox4 = draw.textbbox((0, 0), doc_label, font=font_sub)
tw4 = bbox4[2] - bbox4[0]
draw.text((doc_x + (doc_w - tw4) // 2, doc_y + 12), doc_label, fill=BLUE, font=font_sub)

ai_label = "AI permissions"
bbox5 = draw.textbbox((0, 0), ai_label, font=font_small)
tw5 = bbox5[2] - bbox5[0]
draw.text((doc_x + (doc_w - tw5) // 2, ai_line_y + 38), ai_label, fill=WHITE, font=font_small)

small = "EduHexa — eduhexa-message"
bbox6 = draw.textbbox((0, 0), small, font=font_small)
tw6 = bbox6[2] - bbox6[0]
draw.text(((SIZE - tw6) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
