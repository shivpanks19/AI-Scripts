#!/usr/bin/env python3
"""Generate EduHexa WhatsApp image 1080x1080 with brand colors and logo."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
LIGHT_BLUE = (0, 80, 200)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-whatsapp-reading-depth-july-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

# Halftone dots in corners
for cx, cy in [(80, 80), (1000, 80), (80, 1000), (1000, 1000)]:
    for i in range(12):
        angle = i * math.pi / 6
        r = 20 + i * 8
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(0, 40, 100))

# Central hexagon frame
cx, cy = SIZE // 2, SIZE // 2 + 40
hex_r = 220
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Vertical split line
draw.line([(cx, cy - hex_r), (cx, cy + hex_r)], fill=BLUE, width=2)

# Left side - shortcut/AI chaos
left_cx = cx - 90
# Scrolling feed lines
for i in range(5):
    y = cy - 80 + i * 35
    w = 100 - i * 8
    draw.rounded_rectangle([left_cx - w // 2, y, left_cx + w // 2, y + 12], radius=4, fill=(40, 40, 40))
# Fading text lines
for i in range(4):
    y = cy + 30 + i * 22
    alpha_w = 80 - i * 15
    draw.line([(left_cx - alpha_w // 2, y), (left_cx + alpha_w // 2, y)], fill=GRAY, width=2)
# Sparkle icons (AI shortcuts)
for sx, sy in [(left_cx - 50, cy - 50), (left_cx + 40, cy - 30), (left_cx - 30, cy + 60)]:
    for d in [(0, -6), (6, 0), (0, 6), (-6, 0)]:
        draw.line([(sx, sy), (sx + d[0], sy + d[1])], fill=LIGHT_BLUE, width=2)

# Right side - deep reading
right_cx = cx + 90
# Open book shape
book_w, book_h = 90, 110
draw.rounded_rectangle(
    [right_cx - book_w // 2, cy - book_h // 2, right_cx + book_w // 2, cy + book_h // 2],
    radius=6, outline=BLUE, width=2
)
draw.line([(right_cx, cy - book_h // 2), (right_cx, cy + book_h // 2)], fill=BLUE, width=2)
# Clear text lines in book
for i in range(6):
    y = cy - 40 + i * 14
    lw = 55 - (i % 2) * 10
    draw.line([(right_cx - lw // 2, y), (right_cx + lw // 2, y)], fill=WHITE, width=2)
# Citation mark
draw.text((right_cx + 25, cy - 55), "†", fill=BLUE)
# Steady underline path
draw.line([(right_cx - 30, cy + 55), (right_cx + 30, cy + 55)], fill=BLUE, width=3)

# Bridging arc from left to right
arc_bbox = [cx - 160, cy - 100, cx + 160, cy + 100]
draw.arc(arc_bbox, start=200, end=-20, fill=BLUE, width=3)

# Fonts
def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

font_head = load_font(62)
font_sub = load_font(36)
font_small = load_font(24)

# Headline
headline = "Read Deep Before AI"
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 120), headline, fill=WHITE, font=font_head)

sub = "Comprehension before generation"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 200), sub, fill=BLUE, font=font_sub)

small = "Literacy is the gatekeeper — EduHexa Community Pulse, July 2026"
bbox3 = draw.textbbox((0, 0), small, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 920), small, fill=GRAY, font=font_small)

# Composite logo
logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
logo_x = SIZE - logo_w - 40
logo_y = SIZE - logo_h - 50
img.paste(logo, (logo_x, logo_y), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
