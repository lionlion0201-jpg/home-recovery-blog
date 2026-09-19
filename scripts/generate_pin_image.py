#!/usr/bin/env python3
"""
Generate a Pinterest-ready pin image (1000x1500, 2:3 ratio).

Design rationale (2026-09-19):
  - Photo background rather than flat colour. Multiple sources report lifestyle
    photography outperforming plain/product-on-white for saves and clicks in
    home/wellness categories.
  - Headline overlaid on the TOP of the image. In a paid A/B test of identical
    pins differing only in layout (madpinmedia.com/pin-layout-case-study), top
    overlay on a single photo beat bottom overlay (31 vs 24 outbound clicks) and
    beat a 4-photo grid (31 vs 14). The stated reason is that the top of a pin
    enters the viewport first while scrolling on mobile.
  - One photo, never a collage, for the same reason plus cleaner object
    recognition by Pinterest's own visual search.

Backgrounds come from assets/pin-backgrounds/, a pool of human-approved Pexels
photos (see fetch_pin_photo_candidates.py for why approval is manual). The photo
is chosen deterministically from the title, so regenerating a given pin always
produces the same image, while different pins vary.

Usage:
  python3 generate_pin_image.py \
    --title "Best Red Light Therapy Devices for Home Use" \
    --subtitle "Buyer's guide by budget" \
    --out ../assets/pins/red-light-therapy.png
"""
import argparse
import glob
import hashlib
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH, HEIGHT = 1000, 1500

ACCENT = (47, 111, 79)
ACCENT_DEEP = (26, 64, 45)
TEXT_DARK = (31, 41, 55)
WHITE = (255, 255, 255)
FALLBACK_BG = (250, 248, 245)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
FONT_SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

BACKGROUND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "..", "assets", "pin-backgrounds")

MARGIN = 72
OVERLAY_H = 760      # dark panel holding the headline, anchored to the top
FOOTER_H = 150       # CTA strip at the bottom


def _pick_background(seed_text):
    paths = sorted(glob.glob(os.path.join(BACKGROUND_DIR, "*.jpg")) +
                   glob.glob(os.path.join(BACKGROUND_DIR, "*.jpeg")) +
                   glob.glob(os.path.join(BACKGROUND_DIR, "*.png")))
    if not paths:
        return None
    digest = hashlib.sha256(seed_text.encode("utf-8")).hexdigest()
    return paths[int(digest, 16) % len(paths)]


def _cover(img, width, height):
    """Resize + centre-crop so the photo fills the canvas without distortion."""
    scale = max(width / img.width, height / img.height)
    img = img.resize((max(int(img.width * scale), width),
                      max(int(img.height * scale), height)), Image.LANCZOS)
    left = (img.width - width) // 2
    top = (img.height - height) // 2
    return img.crop((left, top, left + width, top + height))


def _wrap(draw, text, font, max_width):
    words, lines, current = text.split(), [], ""
    for w in words:
        test = (current + " " + w).strip()
        if draw.textlength(test, font=font) > max_width and current:
            lines.append(current)
            current = w
        else:
            current = test
    if current:
        lines.append(current)
    return lines


def _block_height(lines, font, line_spacing):
    ascent, descent = font.getmetrics()
    return len(lines) * int((ascent + descent) * line_spacing)


def _fit_title(draw, text, max_width, max_height, line_spacing=1.16,
               size_range=(92, 46)):
    largest, smallest = size_range
    for size in range(largest, smallest - 1, -2):
        font = ImageFont.truetype(FONT_BOLD, size)
        lines = _wrap(draw, text, font, max_width)
        if _block_height(lines, font, line_spacing) <= max_height:
            return font, lines
    font = ImageFont.truetype(FONT_BOLD, smallest)
    return font, _wrap(draw, text, font, max_width)


def _draw_lines(draw, lines, font, x, start_y, fill, line_spacing=1.16):
    ascent, descent = font.getmetrics()
    step = int((ascent + descent) * line_spacing)
    y = start_y
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += step
    return y


def generate(title, subtitle, brand, out_path, cta="Read the full guide"):
    bg_path = _pick_background(title)
    if bg_path:
        photo = Image.open(bg_path).convert("RGB")
        img = _cover(photo, WIDTH, HEIGHT)
    else:
        img = Image.new("RGB", (WIDTH, HEIGHT), FALLBACK_BG)

    measure = ImageDraw.Draw(img)

    # --- measure the text block first ------------------------------------
    # The scrim is then sized to whatever the text actually occupies. With a
    # fixed gradient, a long headline pushes the subtitle into the faded region
    # and it stops being legible against a bright photo.
    max_text_w = WIDTH - MARGIN * 2
    title_top = 168
    subtitle_font = ImageFont.truetype(FONT_SANS, 34)
    subtitle_lines = _wrap(measure, subtitle, subtitle_font, max_text_w) if subtitle else []
    subtitle_h = _block_height(subtitle_lines, subtitle_font, 1.3) if subtitle_lines else 0

    title_budget = OVERLAY_H - title_top - subtitle_h - 80
    title_font, title_lines = _fit_title(measure, title, max_text_w, title_budget)
    title_h = _block_height(title_lines, title_font, 1.16)

    text_bottom = title_top + title_h + (26 + subtitle_h if subtitle_lines else 0)

    # --- scrim: solid down past the text, then fades into the photo -------
    plateau = min(text_bottom + 48, HEIGHT - FOOTER_H)
    fade = 240
    scrim = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scrim)
    sdraw.rectangle([0, 0, WIDTH, plateau], fill=ACCENT_DEEP + (207,))
    for i in range(fade):
        y = plateau + i
        if y >= HEIGHT:
            break
        alpha = int(207 * (1 - i / fade) ** 1.6)
        sdraw.line([(0, y), (WIDTH, y)], fill=ACCENT_DEEP + (alpha,))
    img = Image.alpha_composite(img.convert("RGBA"), scrim).convert("RGB")
    draw = ImageDraw.Draw(img)

    # --- brand label ------------------------------------------------------
    brand_font = ImageFont.truetype(FONT_SANS_BOLD, 30)
    draw.text((MARGIN, 60), brand.upper(), font=brand_font, fill=WHITE)
    draw.rounded_rectangle([MARGIN, 108, MARGIN + 92, 116], radius=4, fill=WHITE)

    # --- headline ---------------------------------------------------------
    y = _draw_lines(draw, title_lines, title_font, MARGIN, title_top, WHITE)

    if subtitle_lines:
        _draw_lines(draw, subtitle_lines, subtitle_font, MARGIN, y + 26,
                    (235, 238, 236), line_spacing=1.3)

    # --- CTA strip --------------------------------------------------------
    draw.rectangle([0, HEIGHT - FOOTER_H, WIDTH, HEIGHT], fill=ACCENT)
    cta_font = ImageFont.truetype(FONT_SANS_BOLD, 38)
    cta_w = draw.textlength(cta, font=cta_font)
    draw.text(((WIDTH - cta_w) / 2, HEIGHT - FOOTER_H + 40), cta,
              font=cta_font, fill=WHITE)
    draw.rounded_rectangle(
        [(WIDTH - cta_w) / 2, HEIGHT - FOOTER_H + 96,
         (WIDTH + cta_w) / 2, HEIGHT - FOOTER_H + 102],
        radius=3, fill=WHITE)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")
    print(f"Saved pin image: {out_path}"
          f"{' (bg: ' + os.path.basename(bg_path) + ')' if bg_path else ' (no background pool found)'}")
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
