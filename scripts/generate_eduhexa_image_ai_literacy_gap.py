#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - AI Literacy Gap."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-ai-literacy-gap-sep-2026.png"
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

access_x, access_y = cx - 260, cy - 50
draw.rounded_rectangle(
    [access_x, access_y, access_x + 200, access_y + 140],
    radius=10,
    outline=BLUE,
    width=3,
    fill=(12, 12, 18),
)
for i in range(3):
    draw.ellipse(
        [access_x + 30 + i * 50, access_y + 25, access_x + 60 + i * 50, access_y + 55],
        outline=BLUE,
        width=2,
    )
draw.line([(access_x + 40, access_y + 70), (access_x + 160, access_y + 70)], fill=BLUE, width=2)
draw.line([(access_x + 40, access_y + 90), (access_x + 130, access_y + 90)], fill=GRAY, width=2)
draw.text((access_x + 35, access_y + 105), "AI ACCESS", fill=BLUE, font=None)

gap_x = cx - 35
for i in range(6):
    y = cy - 50 + i * 16
    draw.line([(gap_x, y), (gap_x + 70, y)], fill=GRAY if i % 2 else BLUE, width=2)

literacy_x, literacy_y = cx + 60, cy - 50
draw.rounded_rectangle(
    [literacy_x, literacy_y, literacy_x + 200, literacy_y + 140],
    radius=10,
    outline=GRAY,
    width=2,
    fill=(18, 18, 22),
)
draw.rectangle(
    [literacy_x + 25, literacy_y + 20, literacy_x + 175, literacy_y + 45],
    outline=GRAY,
    width=1,
)
draw.line([(literacy_x + 35, literacy_y + 60), (literacy_x + 165, literacy_y + 60)], fill=GRAY, width=2)
draw.line([(literacy_x + 35, literacy_y + 78), (literacy_x + 140, literacy_y + 78)], fill=GRAY, width=2)
draw.line([(literacy_x + 35, literacy_y + 96), (literacy_x + 155, literacy_y + 96)], fill=GRAY, width=1)
draw.text((literacy_x + 20, literacy_y + 105), "AI LITERACY?", fill=GRAY, font=None)

arrow_y = cy + 90
draw.line([(access_x + 100, arrow_y), (literacy_x + 100, arrow_y)], fill=BLUE, width=4)
draw.polygon(
    [(literacy_x + 85, arrow_y - 12), (literacy_x + 85, arrow_y + 12), (literacy_x + 115, arrow_y)],
    fill=BLUE,
)
draw.text((cx - 70, arrow_y + 18), "THE GAP", fill=LIGHT_BLUE, font=None)

pen_x, pen_y = cx - 40, cy + 130
draw.line([(pen_x, pen_y + 40), (pen_x + 8, pen_y)], fill=WHITE, width=3)
draw.line([(pen_x + 8, pen_y), (pen_x + 20, pen_y + 5)], fill=BLUE, width=2)
draw.line([(pen_x + 20, pen_y + 5), (pen_x + 15, pen_y + 45)], fill=WHITE, width=2)
draw.line([(pen_x + 15, pen_y + 45), (pen_x, pen_y + 40)], fill=WHITE, width=2)
draw.line([(pen_x + 30, pen_y + 50), (pen_x + 90, pen_y + 55)], fill=GRAY, width=2)
draw.text((pen_x + 95, pen_y + 42), "Prove thinking", fill=GRAY, font=None)


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

headline = "AI Access Outpaced AI Literacy."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 95), headline, fill=WHITE, font=font_head)

sub = "Prove thinking, not polished output"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 168), sub, fill=BLUE, font=font_sub)

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
