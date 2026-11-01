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

Layout styles (2026-11-01):
  - "overlay": the original top-overlay layout described above. Still the
    default and the most frequent pick, since it won the cited A/B test.
  - "card":    photo on the top ~58%, headline on a light panel underneath.
  - "bold":    solid green background with a large headline, photo inset below.
  Pinterest favours "fresh" pins (new images), and with every pin sharing one
  template the account looked repetitive. A pin can set "style" in its manifest;
  otherwise one is picked deterministically from the title (overlay 50%,
  card 25%, bold 25%), so regenerating a pin keeps its look. A pin can also set
  "background" to a file name in the pool so the photo matches the article.

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

# GitHub Actions (ubuntu) ships DejaVu here. PIN_FONT_DIR lets a local preview
# point at a copy of the same fonts.
FONT_DIR = os.environ.get("PIN_FONT_DIR", "/usr/share/fonts/truetype/dejavu")
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


STYLES = ("overlay", "card", "bold")


def _pick_style(seed_text):
    # Separate salt from _pick_background so style and photo vary independently.
    n = int(hashlib.sha256(("style:" + seed_text).encode("utf-8")).hexdigest(), 16) % 4
    return ("overlay", "overlay", "card", "bold")[n]


def _load_photo(bg_path, width, height):
    if not bg_path:
        return Image.new("RGB", (width, height), FALLBACK_BG)
    return _cover(Image.open(bg_path).convert("RGB"), width, height)


def generate(title, subtitle, brand, out_path, cta="Read the full guide", style=None,
             background=None):
    style = style if style in STYLES else _pick_style(title)
    # A pin may name a photo from the pool ("background": "pexels-123.jpg") so the
    # scene matches the article (e.g. a sauna photo on a sauna pin). Otherwise the
    # photo is picked from the title as before.
    named = os.path.join(BACKGROUND_DIR, background) if background else None
    bg_path = named if named and os.path.exists(named) else _pick_background(title)
    if style == "card":
        img = _render_card(title, subtitle, brand, cta, bg_path)
    elif style == "bold":
        img = _render_bold(title, subtitle, brand, cta, bg_path)
    else:
        img = _render_overlay(title, subtitle, brand, cta, bg_path)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")
    print(f"Saved pin image: {out_path} [style: {style}]"
          f"{' (bg: ' + os.path.basename(bg_path) + ')' if bg_path else ' (no background pool found)'}")
    return out_path


def _render_card(title, subtitle, brand, cta, bg_path):
    """Photo on top, headline on a light panel below (no text over the photo)."""
    photo_h = 870
    img = Image.new("RGB", (WIDTH, HEIGHT), FALLBACK_BG)
    img.paste(_load_photo(bg_path, WIDTH, photo_h), (0, 0))
    draw = ImageDraw.Draw(img)

    # brand tag sitting on the seam between photo and panel
    brand_font = ImageFont.truetype(FONT_SANS_BOLD, 28)
    label = brand.upper()
    lw = draw.textlength(label, font=brand_font)
    draw.rounded_rectangle([MARGIN, photo_h - 28, MARGIN + lw + 48, photo_h + 28],
                           radius=28, fill=ACCENT)
    draw.text((MARGIN + 24, photo_h - 17), label, font=brand_font, fill=WHITE)

    max_text_w = WIDTH - MARGIN * 2
    subtitle_font = ImageFont.truetype(FONT_SANS, 32)
    subtitle_lines = _wrap(draw, subtitle, subtitle_font, max_text_w) if subtitle else []
    subtitle_h = _block_height(subtitle_lines, subtitle_font, 1.3) if subtitle_lines else 0

    cta_h = 92
    title_top = photo_h + 64
    title_budget = HEIGHT - title_top - cta_h - 70 - (subtitle_h + 20 if subtitle_lines else 0)
    title_font, title_lines = _fit_title(draw, title, max_text_w, title_budget,
                                         size_range=(70, 40))
    y = _draw_lines(draw, title_lines, title_font, MARGIN, title_top, TEXT_DARK)
    if subtitle_lines:
        _draw_lines(draw, subtitle_lines, subtitle_font, MARGIN, y + 20,
                    (90, 100, 110), line_spacing=1.3)

    # CTA pill
    cta_font = ImageFont.truetype(FONT_SANS_BOLD, 34)
    label = cta + "  →"
    cw = draw.textlength(label, font=cta_font)
    top = HEIGHT - cta_h - 48
    draw.rounded_rectangle([MARGIN, top, MARGIN + cw + 64, top + cta_h],
                           radius=cta_h // 2, fill=ACCENT)
    draw.text((MARGIN + 32, top + 26), label, font=cta_font, fill=WHITE)
    return img


def _render_bold(title, subtitle, brand, cta, bg_path):
    """Solid green background, large headline, photo inset in the lower half."""
    img = Image.new("RGB", (WIDTH, HEIGHT), ACCENT_DEEP)
    draw = ImageDraw.Draw(img)

    brand_font = ImageFont.truetype(FONT_SANS_BOLD, 30)
    draw.text((MARGIN, 64), brand.upper(), font=brand_font, fill=(190, 214, 200))

    max_text_w = WIDTH - MARGIN * 2
    subtitle_font = ImageFont.truetype(FONT_SANS, 34)
    subtitle_lines = _wrap(draw, subtitle, subtitle_font, max_text_w) if subtitle else []
    subtitle_h = _block_height(subtitle_lines, subtitle_font, 1.3) if subtitle_lines else 0

    inset_top = 840
    title_top = 140
    title_budget = inset_top - title_top - 60 - (subtitle_h + 24 if subtitle_lines else 0)
    title_font, title_lines = _fit_title(draw, title, max_text_w, title_budget,
                                         size_range=(96, 50))
    y = _draw_lines(draw, title_lines, title_font, MARGIN, title_top, WHITE)
    if subtitle_lines:
        _draw_lines(draw, subtitle_lines, subtitle_font, MARGIN, y + 24,
                    (214, 230, 220), line_spacing=1.3)

    # photo inset with rounded corners
    inset_w, inset_h = WIDTH - MARGIN * 2, 480
    photo = _load_photo(bg_path, inset_w, inset_h)
    mask = Image.new("L", (inset_w, inset_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, inset_w, inset_h], radius=36, fill=255)
    img.paste(photo, (MARGIN, inset_top), mask)

    cta_font = ImageFont.truetype(FONT_SANS_BOLD, 38)
    label = cta + "  →"
    cw = draw.textlength(label, font=cta_font)
    draw.text(((WIDTH - cw) / 2, HEIGHT - 120), label, font=cta_font, fill=WHITE)
    return img


def _render_overlay(title, subtitle, brand, cta, bg_path):
    img = _load_photo(bg_path, WIDTH, HEIGHT)

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
    return img


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--brand", default="QuietRecover")
    parser.add_argument("--cta", default="Read the full guide")
    parser.add_argument("--style", choices=STYLES, default=None,
                        help="Layout (default: picked from the title)")
    parser.add_argument("--background", default=None,
                        help="File name in assets/pin-backgrounds/ (default: picked from the title)")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    generate(args.title, args.subtitle, args.brand, args.out, args.cta, args.style,
             args.background)
