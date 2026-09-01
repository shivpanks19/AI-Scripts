#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - Proof Over Polish."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-proof-over-polish-sep-2026.png"
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

polish_x, polish_y = cx - 200, cy - 80
polish_w, polish_h = 160, 200
draw.rounded_rectangle(
    [polish_x, polish_y, polish_x + polish_w, polish_y + polish_h],
    radius=12,
    outline=GRAY,
    width=2,
    fill=(18, 18, 22),
)
for i, lw in enumerate([100, 120, 90, 110]):
    draw.line(
        [(polish_x + 20, polish_y + 35 + i * 28), (polish_x + 20 + lw, polish_y + 35 + i * 28)],
        fill=GRAY,
        width=3,
    )
draw.ellipse([polish_x + polish_w - 35, polish_y + 10, polish_x + polish_w - 10, polish_y + 35], fill=BLUE)

proof_x, proof_y = cx + 40, cy - 60
proof_w, proof_h = 160, 220
draw.rounded_rectangle(
    [proof_x, proof_y, proof_x + proof_w, proof_y + proof_h],
    radius=12,
    outline=BLUE,
    width=3,
    fill=(0, 30, 70),
)
draw.line([(proof_x + 20, proof_y + 40), (proof_x + proof_w - 20, proof_y + 40)], fill=BLUE, width=2)
draw.line([(proof_x + 20, proof_y + 75), (proof_x + proof_w - 40, proof_y + 75)], fill=LIGHT_BLUE, width=2)
draw.line([(proof_x + 20, proof_y + 110), (proof_x + proof_w - 30, proof_y + 110)], fill=LIGHT_BLUE, width=2)

mic_x = proof_x + proof_w // 2
mic_y = proof_y + 145
draw.rounded_rectangle(
    [mic_x - 18, mic_y, mic_x + 18, mic_y + 45],
    radius=9,
    outline=BLUE,
    width=2,
    fill=(12, 12, 18),
)
draw.arc([mic_x - 28, mic_y + 30, mic_x + 28, mic_y + 70], 0, 180, fill=BLUE, width=3)
draw.line([(mic_x, mic_y + 70), (mic_x, mic_y + 82)], fill=BLUE, width=3)
draw.line([(mic_x - 15, mic_y + 82), (mic_x + 15, mic_y + 82)], fill=BLUE, width=3)

arrow_y = cy + 10
draw.line([(polish_x + polish_w + 15, arrow_y), (proof_x - 15, arrow_y)], fill=WHITE, width=3)
draw.polygon(
    [(proof_x - 15, arrow_y), (proof_x - 35, arrow_y - 10), (proof_x - 35, arrow_y + 10)],
    fill=WHITE,
)

pen_x = cx - 30
pen_y = cy + 120
draw.line([(pen_x, pen_y), (pen_x + 50, pen_y - 35)], fill=BLUE, width=4)
draw.ellipse([pen_x + 42, pen_y - 43, pen_x + 56, pen_y - 29], fill=BLUE)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(46)
font_sub = load_font(28)
font_small = load_font(22)
font_tag = load_font(24)

headline = "Proof Over"
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 85), headline, fill=WHITE, font=font_head)

headline2 = "Polish."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 145), headline2, fill=BLUE, font=font_head)

tagline = "When AI finishes the work, classrooms must prove the learning"
bbox3 = draw.textbbox((0, 0), tagline, font=font_tag)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 215), tagline, fill=GRAY, font=font_tag)

polish_label = "POLISH"
bbox4 = draw.textbbox((0, 0), polish_label, font=font_sub)
tw4 = bbox4[2] - bbox4[0]
draw.text((polish_x + (polish_w - tw4) // 2, polish_y + 8), polish_label, fill=GRAY, font=font_sub)

proof_label = "PROOF"
bbox5 = draw.textbbox((0, 0), proof_label, font=font_sub)
tw5 = bbox5[2] - bbox5[0]
draw.text((proof_x + (proof_w - tw5) // 2, proof_y + 8), proof_label, fill=BLUE, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox6 = draw.textbbox((0, 0), small, font=font_small)
tw6 = bbox6[2] - bbox6[0]
draw.text(((SIZE - tw6) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
