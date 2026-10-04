#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Trust & Attention."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-trust-attention-over-detection-oct-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


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
draw.rounded_rectangle([cx - 320, cy - 200, cx + 320, cy + 200], radius=18, outline=BLUE, width=2)

# Left: detection chaos
left_cx = cx - 160
draw.rounded_rectangle([left_cx - 130, cy - 170, left_cx + 130, cy + 30], radius=10, outline=GRAY, width=2, fill=MUTED)
draw.text((left_cx - 110, cy - 155), "DETECTION WAR", fill=GRAY, font=load_font(18))
for i in range(6):
    y0 = cy - 120 + i * 18
    draw.line([(left_cx - 100, y0), (left_cx + 90, y0 + 7)], fill=(90, 90, 100), width=2)
draw.ellipse([left_cx + 70, cy - 110, left_cx + 110, cy - 70], outline=LIGHT_BLUE, width=2)
draw.line([(left_cx + 90, cy - 100), (left_cx + 105, cy - 85)], fill=LIGHT_BLUE, width=2)
draw.ellipse([left_cx + 100, cy - 105, left_cx + 112, cy - 93], outline=LIGHT_BLUE, width=2)

# Right: attention design
right_cx = cx + 160
draw.rounded_rectangle([right_cx - 130, cy - 170, right_cx + 130, cy + 30], radius=10, outline=BLUE, width=3, fill=(8, 20, 45))
draw.text((right_cx - 115, cy - 155), "ATTENTION DESIGN", fill=BLUE, font=load_font(18))
draw.rounded_rectangle([right_cx - 100, cy - 125, right_cx - 40, cy - 85], radius=6, outline=WHITE, width=2)
draw.text((right_cx - 92, cy - 118), "OFF", fill=WHITE, font=load_font(16))
draw.rectangle([right_cx - 20, cy - 120, right_cx + 40, cy - 90], outline=WHITE, width=2)
draw.line([(right_cx - 10, cy - 105), (right_cx + 30, cy - 105)], fill=WHITE, width=2)
draw.line([(right_cx + 10, cy - 115), (right_cx + 10, cy - 95)], fill=WHITE, width=2)
for i in range(3):
    px = right_cx - 80 + i * 55
    draw.rounded_rectangle([px, cy - 70, px + 45, cy - 35], radius=4, outline=BLUE, width=2)
draw.ellipse([right_cx + 75, cy - 65, right_cx + 105, cy - 35], outline=BLUE, width=2)
draw.line([(right_cx + 85, cy - 55), (right_cx + 95, cy - 45)], fill=BLUE, width=3)
draw.line([(right_cx + 85, cy - 45), (right_cx + 98, cy - 45)], fill=BLUE, width=3)

draw.line([(cx - 280, cy + 55), (cx + 280, cy + 55)], fill=WHITE, width=2)
draw.rounded_rectangle([cx - 280, cy + 70, cx + 280, cy + 175], radius=10, outline=BLUE, width=2, fill=(5, 15, 35))
draw.text((cx - 250, cy + 85), "WITNESSED PROOF IN ROOM", fill=WHITE, font=load_font(20))
for i in range(4):
    y = cy + 115 + i * 14
    draw.line([(cx - 230, y), (cx + 200, y)], fill=LIGHT_BLUE, width=2)

font_head = load_font(48)
font_sub = load_font(26)
font_small = load_font(22)

line1 = "Design Attention."
line2 = "Verify Proof."
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 78), line1, fill=WHITE, font=font_head)
bbox2 = draw.textbbox((0, 0), line2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 138), line2, fill=BLUE, font=font_head)

sub = "Trust before the next tool rollout"
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

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
