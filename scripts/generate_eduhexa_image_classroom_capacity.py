#!/usr/bin/env python3
"""Generate EduHexa WhatsApp image 1080x1080 - Classroom Capacity theme."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-whatsapp-classroom-capacity-july-2026.png"
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
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=DARK_BLUE)

# Central hexagon frame
cx, cy = SIZE // 2, SIZE // 2 + 40
hex_r = 220
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Vertical divider
draw.line([(cx, cy - hex_r), (cx, cy + hex_r)], fill=BLUE, width=2)

# LEFT: Overloaded human classroom - clustered figures
left_cx = cx - 95
# Teacher figure (small, at top)
draw.ellipse([left_cx - 12, cy - 100, left_cx + 12, cy - 76], fill=WHITE)
draw.rounded_rectangle([left_cx - 18, cy - 74, left_cx + 18, cy - 30], radius=6, fill=BLUE)

# Clustered student figures (many small circles)
positions = [
    (-50, -20), (-25, -10), (0, -25), (25, -10), (50, -20),
    (-40, 15), (-15, 25), (10, 10), (35, 20), (55, 5),
    (-30, 50), (5, 55), (30, 45), (-10, 70), (20, 75),
]
for dx, dy in positions:
    sx, sy = left_cx + dx, cy + dy
    draw.ellipse([sx - 8, sy - 8, sx + 8, sy + 8], fill=GRAY)
    draw.line([(sx, sy + 8), (sx, sy + 22)], fill=GRAY, width=2)

# Label/tag icons above some students (support load)
for tx, ty in [(-40, -35), (10, -40), (35, 5), (-10, 40)]:
    draw.rounded_rectangle([left_cx + tx - 6, cy + ty - 18, left_cx + tx + 6, cy + ty - 8], radius=2, fill=LIGHT_BLUE)

# RIGHT: AI-school - single student + screen
right_cx = cx + 95
# Screen rectangle
draw.rounded_rectangle([right_cx - 55, cy - 70, right_cx + 55, cy + 50], radius=6, outline=BLUE, width=2)
# Screen glow lines
for i in range(5):
    y = cy - 55 + i * 22
    w = 70 - i * 8
    draw.line([(right_cx - w // 2, y), (right_cx + w // 2, y)], fill=LIGHT_BLUE, width=2)
# AI nodes on screen
for nx, ny in [(right_cx - 20, cy - 40), (right_cx + 15, cy - 20), (right_cx, cy + 10)]:
    draw.ellipse([nx - 4, ny - 4, nx + 4, ny + 4], fill=BLUE)
    for d in [(0, -8), (8, 0), (0, 8), (-8, 0)]:
        draw.line([(nx, ny), (nx + d[0], ny + d[1])], fill=BLUE, width=1)

# Single student facing screen
draw.ellipse([right_cx - 10, cy + 65, right_cx + 10, cy + 85], fill=GRAY)
draw.line([(right_cx, cy + 85), (right_cx, cy + 105)], fill=GRAY, width=2)

# No teacher on right - empty guide space (dashed outline)
draw.rounded_rectangle([right_cx - 25, cy + 110, right_cx + 25, cy + 130], radius=4, outline=GRAY, width=1)

# Bridging arc emphasizing human side
arc_bbox = [cx - 160, cy - 100, cx + 160, cy + 100]
draw.arc(arc_bbox, start=200, end=-20, fill=BLUE, width=3)

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
font_sub = load_font(34)
font_small = load_font(24)

headline = "Human First, Then AI"
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 120), headline, fill=WHITE, font=font_head)

sub = "Classrooms buckle before automation scales"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 200), sub, fill=BLUE, font=font_sub)

small = "Human capacity is the gatekeeper — EduHexa Community Pulse, July 2026"
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
