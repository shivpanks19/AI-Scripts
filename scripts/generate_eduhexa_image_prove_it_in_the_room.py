#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Prove It In the Room."""
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
AMBER = (255, 180, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-prove-it-in-the-room-sep-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

for cx, cy in [(90, 120), (990, 120), (90, 960), (990, 960)]:
    for i in range(10):
        angle = i * math.pi / 5
        r = 18 + i * 7
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

# Left: broken detector badge
det_x, det_y = cx - 230, cy - 40
draw.rounded_rectangle(
    [det_x, det_y, det_x + 150, det_y + 100],
    radius=12,
    outline=GRAY,
    width=2,
    fill=(14, 14, 18),
)
draw.text((det_x + 28, det_y + 18), "AI", fill=GRAY, font=None)
draw.text((det_x + 18, det_y + 48), "DETECTOR", fill=GRAY, font=None)
draw.line([(det_x + 10, det_y + 10), (det_x + 140, det_y + 90)], fill=AMBER, width=4)
draw.line([(det_x + 140, det_y + 10), (det_x + 10, det_y + 90)], fill=AMBER, width=4)

# Center: in-room proof (desk + speech)
desk_x, desk_y = cx - 80, cy + 20
draw.rounded_rectangle(
    [desk_x, desk_y, desk_x + 160, desk_y + 55],
    radius=8,
    outline=BLUE,
    width=3,
    fill=(8, 18, 36),
)
draw.line([(desk_x + 20, desk_y + 18), (desk_x + 140, desk_y + 18)], fill=BLUE, width=2)
draw.line([(desk_x + 20, desk_y + 32), (desk_x + 120, desk_y + 32)], fill=LIGHT_BLUE, width=2)
bubble = [cx + 50, cy - 90, cx + 200, cy - 20]
draw.rounded_rectangle(bubble, radius=14, outline=BLUE, width=3, fill=(10, 25, 50))
draw.polygon([(cx + 55, cy - 18), (cx + 75, cy - 18), (cx + 65, cy + 5)], fill=(10, 25, 50))
draw.line([(cx + 70, cy - 70), (cx + 175, cy - 70)], fill=WHITE, width=2)
draw.line([(cx + 70, cy - 52), (cx + 155, cy - 52)], fill=LIGHT_BLUE, width=2)

# Right: opaque digital marks
scr_x, scr_y = cx + 90, cy - 30
draw.rounded_rectangle(
    [scr_x, scr_y, scr_x + 150, scr_y + 110],
    radius=10,
    outline=GRAY,
    width=2,
    fill=(16, 16, 20),
)
draw.rectangle([scr_x + 15, scr_y + 15, scr_x + 135, scr_y + 75], outline=GRAY, width=2)
for row in range(3):
    draw.line(
        [(scr_x + 22, scr_y + 28 + row * 18), (scr_x + 128, scr_y + 28 + row * 18)],
        fill=GRAY,
        width=1,
    )
draw.text((scr_x + 35, scr_y + 82), "???", fill=AMBER, font=None)

draw.line([(cx - 70, cy + 10), (cx - 75, cy + 10)], fill=LIGHT_BLUE, width=5)
draw.polygon([(cx - 5, cy + 5), (cx + 15, cy + 5), (cx + 5, cy - 15)], fill=LIGHT_BLUE)
draw.line([(cx + 75, cy + 10), (cx + 85, cy + 10)], fill=LIGHT_BLUE, width=5)


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

headline = "Prove It In the Room."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 88), headline, fill=WHITE, font=font_head)

sub = "Trust learning you can see — not algorithms you cannot"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 158), sub, fill=BLUE, font=font_sub)

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
