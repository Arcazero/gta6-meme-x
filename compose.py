#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme: AI illustration + crisp PIL caption text.
Top: 13 YEARS WAITING FOR GTA 6
Bottom: MY AI AGENT ALREADY WINS REAL MONEY ON MAKE.FUN
Classic meme style: white bold text, black outline. Deterministic output."""
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/hatch/workspace/makefun/gta6-meme-x-entry/assets/media-generation-gta6-meme-art-0-04ceb064-b859-4ea2-a9d4-cbeb9d15b0d1.png"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-entry/meme.png"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(SRC).convert("RGB")
W, H = img.size
print(f"source: {W}x{H}")
draw = ImageDraw.Draw(img)


def fit_font(text, max_w, start_size):
    size = start_size
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        bbox = draw.textbbox((0, 0), text, font=f, stroke_width=max(2, size // 16))
        if bbox[2] - bbox[0] <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(FONT, 20)


def draw_centered(text, y, font):
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=max(2, font.size // 16))
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2 - bbox[0]
    draw.text((x, y), text, font=font, fill="white",
              stroke_width=max(2, font.size // 16), stroke_fill="black")


top = "13 YEARS WAITING FOR GTA 6"
bottom_lines = ["MY AI AGENT ALREADY WINS", "REAL MONEY ON MAKE.FUN"]

f_top = fit_font(top, int(W * 0.94), 110)
draw_centered(top, int(H * 0.035), f_top)

f_bot = fit_font(bottom_lines[0], int(W * 0.90), 96)
gap = int(f_bot.size * 0.15)
line_h = []
for line in bottom_lines:
    bbox = draw.textbbox((0, 0), line, font=f_bot, stroke_width=max(2, f_bot.size // 16))
    line_h.append(bbox[3] - bbox[1])
total_h = line_h[0] + gap + line_h[1]
y = H - total_h - int(H * 0.03)
for i, line in enumerate(bottom_lines):
    draw_centered(line, y, f_bot)
    y += line_h[i] + gap

img.save(OUT, "PNG")
print(f"saved {OUT} {img.size} top={f_top.size}px bottom={f_bot.size}px")
