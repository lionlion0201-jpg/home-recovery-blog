#!/usr/bin/env python3
"""
Generate a Pinterest-ready pin image (1000x1500, 2:3 ratio) from a title/subtitle.
Text-based template pin -- no product photography required.

Usage:
  python3 generate_pin_image.py \
    --title "Best Red Light Therapy Devices for Home Use" \
    --subtitle "Buyer's guide by budget" \
    --brand "QuietRecover" \
    --out ../assets/pins/red-light-therapy.png
"""
import argparse
import textwrap
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1000, 1500

# Colors pulled from src/assets/style.css so pins match the site's brand
BG = (250, 248, 245)       # --bg
ACCENT = (47, 111, 79)     # --accent
TEXT = (31, 41, 55)        # --text
MUTED = (107, 114, 128)    # --muted
CARD = (255, 255, 255)     # --card

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
FONT_REGULAR = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def wrap_and_draw(draw, text, font, max_width, start_y, fill, line_spacing=1.25, align="left", canvas_width=WIDTH, margin=70):
    words = text.split()
    lines, current = [], ""
    for w in words:
        test = (current + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = w
        else:
            current = test
    if current:
        lines.append(current)

    y = start_y
    line_height = None
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_height = (bbox[3] - bbox[1]) * line_spacing
        x = margin
        if align == "center":
            text_w = bbox[2] - bbox[0]
            x = (canvas_width - text_w) / 2
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y


def generate(title, subtitle, brand, out_path, cta="Read the full guide"):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # top accent bar
    draw.rectangle([0, 0, WIDTH, 18], fill=ACCENT)

    # brand name
    brand_font = ImageFont.truetype(FONT_REGULAR, 34)
    draw.text((70, 70), brand.upper(), font=brand_font, fill=ACCENT)

    # title
    title_font = ImageFont.truetype(FONT_BOLD, 64)
    y = wrap_and_draw(draw, title, title_font, WIDTH - 140, 180, TEXT, line_spacing=1.15)

    # subtitle
    if subtitle:
        subtitle_font = ImageFont.truetype(FONT_REGULAR, 36)
        y = wrap_and_draw(draw, subtitle, subtitle_font, WIDTH - 140, y + 40, MUTED, line_spacing=1.3)

    # CTA card near the bottom
    card_top = HEIGHT - 220
    draw.rounded_rectangle([70, card_top, WIDTH - 70, HEIGHT - 100], radius=16, fill=ACCENT)
    cta_font = ImageFont.truetype(FONT_BOLD, 40)
    bbox = draw.textbbox((0, 0), cta, font=cta_font)
    text_w = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_w) / 2, card_top + 45), cta, font=cta_font, fill=(255, 255, 255))

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")
    print(f"Saved pin image: {out_path}")
    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--brand", default="QuietRecover")
    parser.add_argument("--cta", default="Read the full guide")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    generate(args.title, args.subtitle, args.brand, args.out, args.cta)
