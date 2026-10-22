#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - AI Mandate Stack."""
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

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-ai-mandate-stack-oct-2026.png"
LOGO = "/workspace/clients/eduhexa logo.png"

img = Image.new("RGB", (SIZE, SIZE), BLACK)
draw = ImageDraw.Draw(img)

for cx, cy in [(100, 140), (980, 140), (100, 940), (980, 940)]:
    for i in range(8):
        angle = i * math.pi / 4
        r = 14 + i * 6
        x = cx + int(r * math.cos(angle))
        y = cy + int(r * math.sin(angle))
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=DARK_BLUE)

cx, cy = SIZE // 2, SIZE // 2 + 50
draw.rounded_rectangle([cx - 340, cy - 230, cx + 340, cy + 230], radius=18, outline=BLUE, width=2)

labels = ["LESSON PLAN", "ASSESSMENT", "GRADING", "RIGOR CHECK"]
stack_x = cx - 300
y0 = cy - 200
for i, label in enumerate(labels):
    y = y0 + i * 52
    draw.rounded_rectangle([stack_x, y, stack_x + 260, y + 44], radius=8, outline=GRAY, width=2, fill=MUTED)
    draw.text((stack_x + 12, y + 8), label, fill=GRAY, font=ImageFont.load_default())
    draw.ellipse([stack_x + 220, y + 10, stack_x + 248, y + 38], outline=LIGHT_BLUE, width=2)
    draw.text((stack_x + 228, y + 16), "AI", fill=LIGHT_BLUE, font=ImageFont.load_default())

judgment_y = y0 + 4 * 52 + 8
draw.rounded_rectangle([stack_x, judgment_y, stack_x + 260, judgment_y + 36], radius=8, outline=BLUE, width=3, fill=(8, 25, 55))
draw.text((stack_x + 12, judgment_y + 10), "JUDGMENT", fill=BLUE, font=ImageFont.load_default())
draw.ellipse([stack_x + 200, judgment_y + 6, stack_x + 248, judgment_y + 30], outline=BLUE, width=2)

right_x = cx + 40
draw.rounded_rectangle([right_x, cy - 120, right_x + 240, cy + 80], radius=10, outline=GRAY, width=2, fill=(25, 25, 30))
draw.line([(right_x + 30, cy - 80), (right_x + 210, cy - 80)], fill=GRAY, width=2)
draw.line([(right_x + 30, cy - 50), (right_x + 180, cy - 50)], fill=GRAY, width=2)
draw.ellipse([right_x + 100, cy + 20, right_x + 200, cy + 70], outline=GRAY, width=2)
draw.text((right_x + 108, cy + 32), "Why try?", fill=GRAY, font=ImageFont.load_default())


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

line1 = "Mandates Stack."
line2 = "Judgment Shrinks."
bbox1 = draw.textbbox((0, 0), line1, font=font_head)
tw1 = bbox1[2] - bbox1[0]
draw.text(((SIZE - tw1) // 2, 72), line1, fill=WHITE, font=font_head)
bbox2 = draw.textbbox((0, 0), line2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 132), line2, fill=BLUE, font=font_head)

sub = "When adults automate faster than schools teach proof"
bbox3 = draw.textbbox((0, 0), sub, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 200), sub, fill=GRAY, font=font_sub)

small = "EduHexa — eduhexa-message"
bbox4 = draw.textbbox((0, 0), small, font=font_small)
tw4 = bbox4[2] - bbox4[0]
draw.text(((SIZE - tw4) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT, "PNG")
print(f"Saved {OUT}")
