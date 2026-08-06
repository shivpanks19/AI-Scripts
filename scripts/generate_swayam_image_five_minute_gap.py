#!/usr/bin/env python3
"""Generate Swayam swayam-message WhatsApp image 1080x1080 - five-minute gap."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

SIZE = 1080
BG = (10, 15, 28)
TEAL = (0, 201, 167)
AMBER = (245, 158, 11)
WHITE = (255, 255, 255)
GRAY = (140, 150, 165)
DARK_TEAL = (0, 120, 100)

OUT = "/workspace/docs/assets/swayam/swayam-message-five-minute-gap-aug-2026.png"


def load_font(size, bold=True):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new("RGB", (SIZE, SIZE), BG)
draw = ImageDraw.Draw(img)

for cx, cy in [(70, 70), (1010, 70), (70, 1010), (1010, 1010)]:
    for i in range(10):
        angle = i * math.pi / 5
        r = 18 + i * 7
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=DARK_TEAL)

cx, cy = SIZE // 2, SIZE // 2 + 20

# Left: phone + message stack
phone_x = cx - 260
draw.rounded_rectangle([phone_x - 70, cy - 120, phone_x + 70, cy + 120], radius=16, outline=TEAL, width=3)
for i, w in enumerate([100, 80, 110]):
    y = cy - 70 + i * 42
    draw.rounded_rectangle([phone_x - 50, y, phone_x - 50 + w, y + 22], radius=8, fill=(30, 40, 60))
draw.ellipse([phone_x + 35, cy - 95, phone_x + 55, cy - 75], fill=AMBER)

# Center: 5:00 timer ring
timer_r = 95
draw.ellipse([cx - timer_r, cy - timer_r, cx + timer_r, cy + timer_r], outline=TEAL, width=5)
draw.arc([cx - timer_r, cy - timer_r, cx + timer_r, cy + timer_r], start=90, end=-90, fill=AMBER, width=8)
font_timer = load_font(52)
draw.text((cx - 42, cy - 32), "5:00", fill=WHITE, font=font_timer)

# Right: mini pipeline
pipe_x = cx + 220
stages = ["Enquiry", "Demo", "Enrolled"]
for i, label in enumerate(stages):
    y = cy - 70 + i * 70
    draw.rounded_rectangle([pipe_x - 75, y, pipe_x + 75, y + 40], radius=8, outline=TEAL if i == 2 else DARK_TEAL, width=2)
    f = load_font(18, bold=False)
    bbox = draw.textbbox((0, 0), label, font=f)
    tw = bbox[2] - bbox[0]
    draw.text((pipe_x - tw // 2, y + 10), label, fill=WHITE if i == 2 else GRAY, font=f)
    if i < 2:
        draw.line([(pipe_x, y + 42), (pipe_x, y + 68)], fill=TEAL, width=2)
        draw.polygon([(pipe_x - 6, y + 62), (pipe_x + 6, y + 62), (pipe_x, y + 72)], fill=TEAL)

# Connecting flow lines
draw.line([(phone_x + 72, cy), (cx - timer_r - 10, cy)], fill=TEAL, width=2)
draw.line([(cx + timer_r + 10, cy), (pipe_x - 78, cy)], fill=TEAL, width=2)

font_head = load_font(46)
font_sub = load_font(28)
font_small = load_font(22)

headline = "Reply in 5 Minutes."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 95), headline, fill=WHITE, font=font_head)

headline2 = "Or Lose the Seat."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 158), headline2, fill=TEAL, font=font_head)

sub = "Fix admissions ownership before the next enquiry wave"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 235), sub, fill=GRAY, font=font_sub)

small = "Swayam — swayam-message"
bbox4 = draw.textbbox((0, 0), small, font=font_small)
tw4 = bbox4[2] - bbox4[0]
draw.text(((SIZE - tw4) // 2, 920), small, fill=GRAY, font=font_small)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
