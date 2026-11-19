#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme (v2): Leon & Lucia dialogue.

Art: AI illustration of Lucia driving and Leon riding shotgun in a Vice City
convertible at sunset, with make.fun's ghost mascot on the dashboard.
Layout: illustration cropped to the top band (keeps both faces + the ghost),
dialogue panel below it, game-dialogue style: speaker chips + speech text.

Dialogue (original):
  LUCIA: 13 years we've waited for this job.
  LEON:  Chill. My AI agent didn't wait — it already made real money on make.fun.
  LUCIA: Real money? Doing what?
  LEON:  Winning bounties. Get your agent one too.

All text is PIL (DejaVu Sans Bold), no text inside the illustration itself.
Deterministic output."""
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/hatch/workspace/makefun/gta6-meme-x-entry/assets/media-generation-leon-lucia-dialogue-art-0-16fe5670-b99e-426d-a2e5-13ffd75a635f.webp"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-entry/meme.png"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W, H = 1920, 1280
ART_H = 800          # illustration band on top
PANEL_Y = ART_H      # dialogue panel below

# Crop the art's bottom band: keeps both faces and the ghost on the dashboard,
# cuts mostly sky at the top.
CROP_TOP = 440
CROP_BOTTOM = CROP_TOP + ART_H

DIALOGUE = [
    ("LUCIA", "13 years we've waited for this job.", (232, 62, 140)),
    ("LEON", "Chill. My AI agent didn't wait \u2014 it already made real money on make.fun.", (43, 179, 230)),
    ("LUCIA", "Real money? Doing what?", (232, 62, 140)),
    ("LEON", "Winning bounties. Get your agent one too.", (43, 179, 230)),
]

PANEL_BG = (11, 11, 18)
PANEL_RULE = (230, 0, 126)   # make.fun magenta
CHIP_PAD_X = 22
CHIP_PAD_Y = 12
MARGIN_X = 90
ROW_GAP = 22
PANEL_PAD_TOP = 26
PANEL_PAD_BOTTOM = 20


def wrap(draw, text, font, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    art = Image.open(SRC).convert("RGB")
    assert art.size == (1920, 1280), f"unexpected art size {art.size}"
    art_band = art.crop((0, CROP_TOP, W, CROP_BOTTOM))

    img = Image.new("RGB", (W, H), PANEL_BG)
    img.paste(art_band, (0, 0))
    draw = ImageDraw.Draw(img)
    # magenta rule between art and panel
    draw.rectangle([0, PANEL_Y - 3, W, PANEL_Y + 3], fill=PANEL_RULE)

    # Fit the speech font so all rows fit the panel.
    text_area_w = W - 2 * MARGIN_X
    size = 58
    while size >= 36:
        font = ImageFont.truetype(FONT_BOLD, size)
        chip_font = ImageFont.truetype(FONT_BOLD, 40)
        line_h = int(size * 1.28)
        total = PANEL_PAD_TOP + PANEL_PAD_BOTTOM
        rows = []
        for name, text, color in DIALOGUE:
            chip_w = int(draw.textlength(name, font=chip_font)) + 2 * CHIP_PAD_X
            chip_h = 40 + 2 * CHIP_PAD_Y
            max_w = text_area_w - chip_w - 28
            lines = wrap(draw, text, font, max_w)
            row_h = max(chip_h, len(lines) * line_h)
            rows.append((name, text, color, chip_w, chip_h, lines))
            total += row_h
        total += ROW_GAP * (len(DIALOGUE) - 1)
        if total <= H - PANEL_Y:
            break
        size -= 2

    print(f"speech font {size}px, total rows height {total}px, panel {H - PANEL_Y}px")
    y = PANEL_Y + PANEL_PAD_TOP
    for name, text, color, chip_w, chip_h, lines in rows:
        # speaker chip (rounded rect)
        draw.rounded_rectangle(
            [MARGIN_X, y, MARGIN_X + chip_w, y + chip_h],
            radius=chip_h // 2, fill=color,
        )
        name_w = draw.textlength(name, font=chip_font)
        name_x = MARGIN_X + (chip_w - name_w) / 2
        name_y = y + (chip_h - 40) / 2 - 2
        draw.text((name_x, name_y), name, font=chip_font, fill="white")
        # speech lines, vertically centered on the row
        row_h = max(chip_h, len(lines) * line_h)
        tx = MARGIN_X + chip_w + 28
        ty = y + (row_h - len(lines) * line_h) / 2
        for line in lines:
            draw.text((tx, ty), line, font=font, fill="white")
            ty += line_h
        y += row_h + ROW_GAP

    img.save(OUT, "PNG")
    print(f"saved {OUT} {img.size}")


if __name__ == "__main__":
    main()
