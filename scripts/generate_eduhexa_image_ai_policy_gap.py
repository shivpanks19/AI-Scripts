#!/usr/bin/env python3
"""Generate EduHexa WhatsApp image 1080x1080 - AI Policy Gap theme."""
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

OUT = "/workspace/docs/assets/eduhexa/eduhexa-whatsapp-ai-policy-gap-july-2026.png"
LOGO = "/workspace/docs/eduhexa logo.png"

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

# LEFT: Students with document/policy (ahead)
left_cx = cx - 95
# Student figures (3 small, forward-leaning)
for dx, dy in [(-30, -30), (0, -45), (30, -30)]:
    sx, sy = left_cx + dx, cy + dy
    draw.ellipse([sx - 10, sy - 10, sx + 10, sy + 10], fill=WHITE)
    draw.line([(sx, sy + 10), (sx, sy + 35)], fill=WHITE, width=3)
# Document scroll
draw.rounded_rectangle([left_cx - 45, cy + 10, left_cx + 45, cy + 90], radius=4, outline=BLUE, width=2)
for i in range(5):
    y = cy + 25 + i * 12
    w = 60 - i * 4
    draw.line([(left_cx - w // 2, y), (left_cx + w // 2, y)], fill=LIGHT_BLUE, width=2)
# Checkmark on document
draw.line([(left_cx - 15, cy + 55), (left_cx - 5, cy + 65)], fill=BLUE, width=3)
draw.line([(left_cx - 5, cy + 65), (left_cx + 20, cy + 40)], fill=BLUE, width=3)
# Forward arrow
draw.polygon([(left_cx + 55, cy + 50), (left_cx + 75, cy + 50), (left_cx + 68, cy + 42)], fill=BLUE)
draw.polygon([(left_cx + 55, cy + 50), (left_cx + 75, cy + 50), (left_cx + 68, cy + 58)], fill=BLUE)

# RIGHT: Empty policy board / question marks (lag)
right_cx = cx + 95
# Empty clipboard
draw.rounded_rectangle([right_cx - 40, cy - 60, right_cx + 40, cy + 70], radius=6, outline=GRAY, width=2)
draw.rounded_rectangle([right_cx - 25, cy - 75, right_cx + 25, cy - 55], radius=3, fill=GRAY)
# Dashed empty lines
for i in range(6):
    y = cy - 40 + i * 18
    for x in range(right_cx - 30, right_cx + 30, 12):
        draw.line([(x, y), (x + 6, y)], fill=GRAY, width=+2)
# Question marks floating
for qx, qy in [(right_cx - 20, cy + 85), (right_cx + 15, cy + 95)]:
    draw.ellipse([qx - 8, qy - 12, qx + 8, qy + 4], outline=GRAY, width=2)
    draw.ellipse([qx - 2, qy + 8, qx + 2, qy + 12], fill=GRAY)

# Clock/waiting arc on right (lag indicator)
draw.arc([right_cx - 30, cy - 100, right_cx + 30, cy - 40], start=0, end=270, fill=GRAY, width=2)

# Bridging arc from left (students) to center
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

headline = "Rules Before Tools"
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 120), headline, fill=WHITE, font=font_head)

sub = "Students moved first — schools lag behind"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 200), sub, fill=BLUE, font=font_sub)

small = "AI governance is the gatekeeper — EduHexa Community Pulse, July 2026"
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
