#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Focus Before Features."""
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
RED = (220, 60, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-focus-before-features-sep-2026.png"
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

cx, cy = SIZE // 2, SIZE // 2 + 40
hex_r = 210
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

# Layer 1: phone distraction (bottom)
phone_x, phone_y = cx - 55, cy + 90
draw.rounded_rectangle(
    [phone_x, phone_y, phone_x + 110, phone_y + 170],
    radius=12,
    outline=GRAY,
    width=+2,
    fill=(18, 18, 22),
)
draw.rectangle([phone_x + 20, phone_y + 20, phone_x + 90, phone_y + 120], outline=GRAY, width=2)
for i in range(4):
    draw.ellipse(
        [phone_x + 95 + i * 18, phone_y + 15 + i * 12, phone_x + 107 + i * 18, phone_y + 27 + i * 12],
        fill=GRAY,
    )
draw.text((phone_x - 10, phone_y + 178), "1  DISTRACTION", fill=GRAY, font=None)

# Layer 2: focus tray (middle)
tray_x, tray_y = cx - 120, cy - 30
draw.rounded_rectangle(
    [tray_x, tray_y, tray_x + 240, tray_y + 70],
    radius=10,
    outline=BLUE,
    width=3,
    fill=(10, 20, 40),
)
draw.rectangle([tray_x + 20, tray_y + 18, tray_x + 60, tray_y + 52], outline=BLUE, width=2)
draw.line([(tray_x + 80, tray_y + 35), (tray_x + 210, tray_y + 35)], fill=BLUE, width=3)
draw.polygon(
    [(tray_x + 195, tray_y + 22), (tray_x + 195, tray_y + 48), (tray_x + 220, tray_y + 35)],
    fill=BLUE,
)
draw.text((tray_x + 5, tray_y + 78), "2  FOCUS POLICY", fill=BLUE, font=None)

# Layer 3: deferred AI mandate (top)
ai_x, ai_y = cx - 70, cy - 160
draw.rounded_rectangle(
    [ai_x, ai_y, ai_x + 140, ai_y + 90],
    radius=10,
    outline=GRAY,
    width=2,
    fill=(16, 16, 20),
)
draw.ellipse([ai_x + 45, ai_y + 15, ai_x + 95, ai_y + 55], outline=GRAY, width=2)
draw.line([(ai_x + 25, ai_y + 65), (ai_x + 115, ai_y + 65)], fill=GRAY, width=2)
draw.line([(ai_x + 30, ai_y + 78), (ai_x + 100, ai_y + 78)], fill=GRAY, width=1)
draw.line([(ai_x + 10, ai_y + 10), (ai_x + 130, ai_y + 80)], fill=RED, width=3)
draw.line([(ai_x + 130, ai_y + 10), (ai_x + 10, ai_y + 80)], fill=RED, width=3)
draw.text((ai_x - 25, ai_y - 28), "3  AI MANDATE (LATER)", fill=GRAY, font=None)

# Sequencing arrows
draw.line([(cx, cy + 85), (cx, cy - 5)], fill=LIGHT_BLUE, width=4)
draw.polygon([(cx - 10, cy - 5), (cx + 10, cy - 5), (cx, cy - 25)], fill=LIGHT_BLUE)
draw.line([(cx, cy - 75), (cx, cy - 145)], fill=LIGHT_BLUE, width=4)
draw.polygon([(cx - 10, cy - 145), (cx + 10, cy - 145), (cx, cy - 165)], fill=LIGHT_BLUE)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(52)
font_sub = load_font(28)
font_small = load_font(22)

headline = "Focus Before Features."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 90), headline, fill=WHITE, font=font_head)

sub = "Rebuild attention before AI mandates"
bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 162), sub, fill=BLUE, font=font_sub)

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
