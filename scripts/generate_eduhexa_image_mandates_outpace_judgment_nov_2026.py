#!/usr/bin/env python3
"""Generate EduHexa WhatsApp image 1080x1080 — Mandates Outpace Judgment (Nov 2026)."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
LIGHT_BLUE = (0, 80, 200)
DARK_GRAY = (40, 40, 40)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(
    REPO, "clients/assets/eduhexa/eduhexa-message-mandates-outpace-judgment-nov-2026.png"
)
LOGO = os.path.join(REPO, "clients/eduhexa logo.png")

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

# Corner halftone
for cx, cy in [(80, 80), (1000, 80), (80, 1000), (1000, 1000)]:
    for i in range(12):
        angle = i * math.pi / 6
        r = 20 + i * 8
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(0, 40, 100))

# Central hexagon
cx, cy = SIZE // 2, SIZE // 2 + 40
hex_r = 220
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)
draw.line([(cx - hex_r, cy), (cx + hex_r, cy)], fill=BLUE, width=2)

# Left: phone in bin (attention win) — simple icon
left_cx = cx - 95
draw.rounded_rectangle([left_cx - 28, cy - 50, left_cx + 28, cy + 30], radius=8, outline=BLUE, width=2)
draw.ellipse([left_cx - 8, cy + 35, left_cx + 8, cy + 42], fill=BLUE)
# bin below
draw.polygon(
    [(left_cx - 40, cy + 55), (left_cx + 40, cy + 55), (left_cx + 32, cy + 100), (left_cx - 32, cy + 100)],
    outline=LIGHT_BLUE,
    width=2,
)
draw.line([(left_cx - 25, cy + 55), (left_cx + 25, cy + 55)], fill=LIGHT_BLUE, width=2)
draw.text((left_cx - 52, cy + 108), "ATTENTION", fill=GRAY)

# Right: AI mandate stack — layered cards
right_cx = cx + 95
for i, w in enumerate([120, 105, 90, 75]):
    y = cy - 70 + i * 38
    h = 28
    draw.rounded_rectangle(
        [right_cx - w // 2, y, right_cx + w // 2, y + h],
        radius=5,
        fill=DARK_GRAY if i % 2 else (25, 25, 25),
        outline=BLUE if i == 0 else GRAY,
        width=1,
    )
    # sparkle on top card
    if i == 0:
        for sx, sy in [(right_cx + 35, y + 8), (right_cx - 40, y + 12)]:
            for d in [(0, -5), (5, 0), (0, 5), (-5, 0)]:
                draw.line([(sx, sy), (sx + d[0], sy + d[1])], fill=LIGHT_BLUE, width=2)
draw.text((right_cx - 42, cy + 95), "MANDATES", fill=GRAY)

# Center: human figure outline (judgment)
draw.ellipse([cx - 18, cy - 95, cx + 18, cy - 60], outline=WHITE, width=2)
draw.line([(cx, cy - 58), (cx, cy + 5)], fill=WHITE, width=3)
draw.line([(cx - 35, cy - 35), (cx + 35, cy - 35)], fill=WHITE, width=2)
draw.line([(cx, cy + 5), (cx - 28, cy + 55)], fill=WHITE, width=2)
draw.line([(cx, cy + 5), (cx + 28, cy + 55)], fill=WHITE, width=2)

# Scale imbalance: mandates heavier
draw.line([(cx, cy + 60), (cx - 60, cy + 85)], fill=BLUE, width=2)
draw.line([(cx, cy + 60), (cx + 60, cy + 75)], fill=BLUE, width=2)
draw.ellipse([cx - 75, cy + 80, cx - 45, cy + 95], outline=BLUE, width=2)
draw.ellipse([cx + 35, cy + 68, cx + 85, cy + 88], fill=BLUE)

arc_bbox = [cx - 160, cy - 100, cx + 160, cy + 100]
draw.arc(arc_bbox, start=200, end=-20, fill=BLUE, width=3)


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
font_sub = load_font(32)
font_small = load_font(22)

headline = "Mandates Outpace Judgment"
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 115), headline, fill=WHITE, font=font_head)

sub = "Win attention first — then bound AI with human proof"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 195), sub, fill=BLUE, font=font_sub)

small = "EduHexa Community Pulse · Nov 2026"
bbox3 = draw.textbbox((0, 0), small, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 925), small, fill=GRAY, font=font_small)

if os.path.exists(LOGO):
    logo = Image.open(LOGO).convert("RGBA")
    logo_w = int(SIZE * 0.20)
    logo_h = int(logo_w * logo.height / logo.width)
    logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    logo_x = SIZE - logo_w - 40
    logo_y = SIZE - logo_h - 50
    img.paste(logo, (logo_x, logo_y), logo)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")