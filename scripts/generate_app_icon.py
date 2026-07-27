#!/usr/bin/env python3
"""
Generate a square app icon (for Pinterest/X developer app registration, etc.)
matching the site's brand colors. Outputs a 1024x1024 PNG, which safely
covers any platform's icon size requirement (they can downscale as needed).

Usage:
  python3 generate_app_icon.py --out ../assets/app_icon.png [--initials QR]
"""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024

BG = (47, 111, 79)      # --accent
RING = (250, 248, 245)  # --bg (cream ring)
TEXT = (250, 248, 245)  # cream text on green

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")


def generate(initials, out_path):
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    # thin inset ring for a bit of polish
    margin = 48
    draw.rounded_rectangle(
        [margin, margin, SIZE - margin, SIZE - margin],
        radius=90,
        outline=RING,
        width=10,
    )

    font = ImageFont.truetype(FONT_BOLD, 380)
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (SIZE - text_w) / 2 - bbox[0]
    y = (SIZE - text_h) / 2 - bbox[1]
    draw.text((x, y), initials, font=font, fill=TEXT)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")
    print(f"Saved app icon: {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--initials", default="QR")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    generate(args.initials, args.out)
