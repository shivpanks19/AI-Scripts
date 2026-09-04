#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Coaching-School Reckoning."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-coaching-school-reckoning-sep-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 20
hex_r = 210
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

school_x, school_y = cx - 230, cy - 60
draw.rounded_rectangle(
    [school_x, school_y, school_x + 180, school_y + 160],
    radius=10,
    outline=BLUE,
    width=2,
    fill=(12, 12, 18),
)
draw.polygon(
    [
        (school_x + 20, school_y + 10),
        (school_x + 90, school_y - 35),
        (school_x + 160, school_y + 10),
    ],
    outline=BLUE,
    width=2,
)
for i in range(4):
    draw.rectangle(
        [school_x + 30 + i * 35, school_y + 50, school_x + 55 + i * 35, school_y + 90],
        outline=GRAY,
        width=1,
    )
draw.text((school_x + 45, school_y + 110), "SCHOOL", fill=GRAY, font=None)

gap_x = cx - 30
for i in range(5):
    y = cy - 40 + i * 18
    draw.line([(gap_x, y), (gap_x + 60, y)], fill=GRAY if i % 2 else BLUE, width=2)

coaching_x, coaching_y = cx + 50, cy - 60
draw.rounded_rectangle(
    [coaching_x, coaching_y, coaching_x + 180, coaching_y + 160],
    radius=10,
    outline=GRAY,
    width=2,
    fill=(18, 18, 22),
)
for i, lw in enumerate([120, 140, 100, 130, 110]):
    draw.line(
        [(coaching_x + 20, coaching_y + 35 + i * 24), (coaching_x + 20 + lw, coaching_y + 35 + i * 24)],
        fill=GRAY,
        width=3,
    )
draw.text((coaching_x + 25, coaching_y + 120), "COACHING", fill=GRAY, font=None)

bridge_y = cy + 100
draw.line([(school_x + 90, bridge_y), (coaching_x + 90, bridge_y)], fill=BLUE, width=4)
draw.polygon(
    [(cx - 15, bridge_y - 12), (cx + 15, bridge_y - 12), (cx, bridge_y + 8)],
    fill=BLUE,
)
draw.text((cx - 55, bridge_y + 20), "ALIGN", fill=LIGHT_BLUE, font=None)

arc_bbox = [cx - 170, cy - 120, cx + 170, cy + 80]
draw.arc(arc_bbox, start=210, end=-30, fill=BLUE, width=3)


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
font_sub = load_font(28)
font_small = load_font(22)

headline = "Close the Coaching Gap."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 100), headline, fill=WHITE, font=font_head)

sub = "When classrooms must own what entrance exams test"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 175), sub, fill=BLUE, font=font_sub)

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
