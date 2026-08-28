#!/usr/bin/env python3
"""Generate EduHexa eduhexa-message WhatsApp image 1080x1080 - 70-30 Conversation Gap."""
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
MUTED_RED = (180, 60, 60)

OUT = "/workspace/clients/assets/eduhexa/eduhexa-message-conversation-gap-aug-2026.png"
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
hex_r = 190
hex_pts = []
for i in range(6):
    angle = math.pi / 6 + i * math.pi / 3
    hex_pts.append((cx + hex_r * math.cos(angle), cy + hex_r * math.sin(angle)))
draw.polygon(hex_pts, outline=BLUE, width=3)

left_cx = cx - 200
right_cx = cx + 200
bar_top = cy - 120
bar_bottom = cy + 120
bar_w = 90

draw.rounded_rectangle(
    [left_cx - bar_w // 2, bar_top, left_cx + bar_w // 2, bar_bottom],
    radius=16,
    outline=BLUE,
    width=3,
    fill=(15, 15, 25),
)
fill_h = int((bar_bottom - bar_top) * 0.70)
draw.rounded_rectangle(
    [left_cx - bar_w // 2 + 8, bar_bottom - fill_h, left_cx + bar_w // 2 - 8, bar_bottom - 8],
    radius=10,
    fill=BLUE,
)

draw.rounded_rectangle(
    [right_cx - bar_w // 2, bar_top, right_cx + bar_w // 2, bar_bottom],
    radius=16,
    outline=BLUE,
    width=3,
    fill=(15, 15, 25),
)
fill_h2 = int((bar_bottom - bar_top) * 0.30)
draw.rounded_rectangle(
    [right_cx - bar_w // 2 + 8, bar_bottom - fill_h2, right_cx + bar_w // 2 - 8, bar_bottom - 8],
    radius=10,
    fill=LIGHT_BLUE,
)

speech_x = cx
speech_y = cy - 10
draw.ellipse([speech_x - 55, speech_y - 40, speech_x + 55, speech_y + 40], outline=MUTED_RED, width=3)
draw.line([(speech_x - 20, speech_y + 35), (speech_x - 35, speech_y + 65)], fill=MUTED_RED, width=3)
draw.line([(speech_x - 35, speech_y + 65), (speech_x - 5, speech_y + 50)], fill=MUTED_RED, width=3)
draw.line([(speech_x - 30, speech_y - 10), (speech_x + 30, speech_y - 10)], fill=GRAY, width=2)
draw.line([(speech_x - 30, speech_y + 5), (speech_x + 20, speech_y + 5)], fill=GRAY, width=2)
draw.line([(speech_x - 30, speech_y + 20), (speech_x + 10, speech_y + 20)], fill=GRAY, width=2)


def load_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


font_head = load_font(48)
font_stat = load_font(64)
font_sub = load_font(26)
font_small = load_font(22)
font_label = load_font(30)

headline = "70% Use It."
bbox = draw.textbbox((0, 0), headline, font=font_head)
tw = bbox[2] - bbox[0]
draw.text(((SIZE - tw) // 2, 85), headline, fill=WHITE, font=font_head)

headline2 = "30% Were Told How."
bbox2 = draw.textbbox((0, 0), headline2, font=font_head)
tw2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - tw2) // 2, 145), headline2, fill=BLUE, font=font_head)

tagline = "The conversation gap schools must close"
bbox3 = draw.textbbox((0, 0), tagline, font=font_sub)
tw3 = bbox3[2] - bbox3[0]
draw.text(((SIZE - tw3) // 2, 220), tagline, fill=GRAY, font=font_sub)

stat70 = "70%"
bbox4 = draw.textbbox((0, 0), stat70, font=font_stat)
tw4 = bbox4[2] - bbox4[0]
draw.text((left_cx - tw4 // 2, bar_top - 70), stat70, fill=WHITE, font=font_stat)
label70 = "use AI"
bbox5 = draw.textbbox((0, 0), label70, font=font_label)
tw5 = bbox5[2] - bbox5[0]
draw.text((left_cx - tw5 // 2, bar_top - 30), label70, fill=GRAY, font=font_label)

stat30 = "30%"
bbox6 = draw.textbbox((0, 0), stat30, font=font_stat)
tw6 = bbox6[2] - bbox6[0]
draw.text((right_cx - tw6 // 2, bar_top - 70), stat30, fill=WHITE, font=font_stat)
label30 = "had the talk"
bbox7 = draw.textbbox((0, 0), label30, font=font_label)
tw7 = bbox7[2] - bbox7[0]
draw.text((right_cx - tw7 // 2, bar_top - 30), label30, fill=GRAY, font=font_label)

small = "EduHexa — eduhexa-message"
bbox8 = draw.textbbox((0, 0), small, font=font_small)
tw8 = bbox8[2] - bbox8[0]
draw.text(((SIZE - tw8) // 2, 920), small, fill=GRAY, font=font_small)

logo = Image.open(LOGO).convert("RGBA")
logo_w = int(SIZE * 0.20)
logo_h = int(logo_w * logo.height / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
img.paste(logo, (SIZE - logo_w - 40, SIZE - logo_h - 50), logo)

img.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({os.path.getsize(OUT)} bytes)")
