#!/usr/bin/env python3
"""
Sincap Kitap Instagram Carousel — Metin Bindirme Script

Higgsfield ile üretilmiş ham illüstrasyonların üzerine:
- Türkçe başlık (Bagel Fat One, 2 renk karışık)
- Alt metin / alıntı (Baloo 2)
- Sincap Kitap logosu (sol alt)
- Kompozisyonlu dekorasyonlar (kapakta)

Kullanım:
    python3 scripts/overlay_text.py layout.json

Gereksinimler:
    pip install Pillow
"""

import json
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random
import math

# === AYARLAR ===
CANVAS_W = 1080
CANVAS_H = 1350

ASSETS_DIR = Path("assets")
LOGO_PATH = ASSETS_DIR / "logo.png"
FONT_TITLE_PRIMARY = ASSETS_DIR / "fonts" / "BagelFatOne-Regular.ttf"
FONT_TITLE_FALLBACK = ASSETS_DIR / "fonts" / "Fredoka-Bold.ttf"
# BagelFatOne lacks glyphs for Turkish-specific chars (ğ, ı, İ, Ğ, ş, Ş).
# Auto-switch to Fredoka-Bold (chunky rounded, full Turkish support) if the
# title text needs any of those glyphs.
FONT_TITLE = FONT_TITLE_PRIMARY
FONT_BODY = ASSETS_DIR / "fonts" / "Baloo2-Regular.ttf"

_TR_SPECIAL = set("ğıİĞşŞ")


def title_font_for(text: str) -> "Path":
    return FONT_TITLE_FALLBACK if any(c in _TR_SPECIAL for c in (text or "")) else FONT_TITLE

# === YARDIMCI FONKSİYONLAR ===

def load_font(path, size):
    """Font yükle, yoksa default kullan."""
    try:
        return ImageFont.truetype(str(path), size)
    except Exception as e:
        print(f"[WARN] Font yüklenemedi ({path}): {e}. Default kullanılıyor.")
        return ImageFont.load_default()


def wrap_text(text, font, max_width, draw):
    """Metni verilen genişliğe göre satırlara böl."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_multiline_center(draw, lines, font, color, start_y, line_spacing=1.1):
    """Ortalanmış çok satırlı metin çiz."""
    cur_y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (CANVAS_W - w) // 2
        draw.text((x, cur_y), line, font=font, fill=color)
        cur_y += int(h * line_spacing)
    return cur_y


def paste_logo(img):
    """Sol alt köşeye Sincap Kitap logosu."""
    if not LOGO_PATH.exists():
        print(f"[WARN] Logo bulunamadı: {LOGO_PATH}")
        return
    logo = Image.open(LOGO_PATH).convert("RGBA")
    target_h = 140
    ratio = target_h / logo.height
    target_w = int(logo.width * ratio)
    logo = logo.resize((target_w, target_h), Image.LANCZOS)
    margin = 50
    img.paste(logo, (margin, CANVAS_H - target_h - margin), logo)


def draw_decorations(draw, palette, count=7, seed=42):
    """Kompozisyonlu dekoratif öğeler — yıldız, nokta, küçük çizgiler."""
    random.seed(seed)
    accent = palette["accent"]
    text_color = palette["text"]
    # Üst yarıda başlık etrafında
    zones = [
        (80, 80, 1000, 520),   # üst bölge
    ]
    for _ in range(count):
        x = random.randint(zones[0][0], zones[0][2])
        y = random.randint(zones[0][1], zones[0][3])
        kind = random.choice(["star", "dot", "cross"])
        color = random.choice([accent, "#FFFFFF", text_color])
        size = random.randint(8, 24)
        if kind == "star":
            # basit 4 uçlu yıldız
            draw.polygon([
                (x, y - size), (x + size // 3, y - size // 3),
                (x + size, y), (x + size // 3, y + size // 3),
                (x, y + size), (x - size // 3, y + size // 3),
                (x - size, y), (x - size // 3, y - size // 3),
            ], fill=color)
        elif kind == "dot":
            draw.ellipse([x - size // 2, y - size // 2, x + size // 2, y + size // 2], fill=color)
        elif kind == "cross":
            draw.line([(x - size, y), (x + size, y)], fill=color, width=3)
            draw.line([(x, y - size), (x, y + size)], fill=color, width=3)


# === SLIDE ÇİZİM FONKSİYONLARI ===

def render_cover(raw_path, out_path, slide_data, palette):
    """Kapak slide'ı — büyük başlık üstte, 2 renk karışık."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    # Dekorasyonlar (isteğe bağlı)
    if slide_data.get("decorations"):
        draw_decorations(draw, palette, count=8)

    title_main = slide_data.get("title_main", "")
    title_accent = slide_data.get("title_accent", "")
    subtitle = slide_data.get("subtitle", "")

    # Başlık — ana kısım
    title_font = load_font(title_font_for(title_main), 120)
    max_w = CANVAS_W - 120
    main_lines = wrap_text(title_main, title_font, max_w, draw)

    start_y = 120
    cur_y = draw_multiline_center(draw, main_lines, title_font, palette["text"], start_y, 1.0)

    # Aksan kelime (farklı renkte, biraz daha büyük)
    if title_accent:
        accent_font = load_font(title_font_for(title_accent), 140)
        accent_lines = wrap_text(title_accent, accent_font, max_w, draw)
        cur_y = draw_multiline_center(draw, accent_lines, accent_font, palette["accent"], cur_y + 10, 1.0)

    # Alt başlık
    if subtitle:
        sub_font = load_font(FONT_BODY, 40)
        sub_lines = wrap_text(subtitle, sub_font, CANVAS_W - 160, draw)
        draw_multiline_center(draw, sub_lines, sub_font, palette["text"], cur_y + 30, 1.2)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


def render_inner(raw_path, out_path, slide_data, palette):
    """İç sayfa — üstte metin, alt büyük illüstrasyon."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    body = slide_data.get("body", "")
    body_font = load_font(FONT_BODY, 52)
    lines = wrap_text(body, body_font, CANVAS_W - 140, draw)
    draw_multiline_center(draw, lines, body_font, palette["text"], 120, 1.3)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


def render_quote(raw_path, out_path, slide_data, palette):
    """Alıntı slide — büyük beyaz alıntı üstte."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    quote = slide_data.get("quote", "")
    quote_font = load_font(FONT_BODY, 60)
    lines = wrap_text(quote, quote_font, CANVAS_W - 140, draw)
    draw_multiline_center(draw, lines, quote_font, "#FFFFFF", 140, 1.25)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


def render_tip(raw_path, out_path, slide_data, palette):
    """UNUTMAYIN! veya Ebeveyn Notu — aksan başlık + paragraf."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    title = slide_data.get("title_accent", "UNUTMAYIN!")
    body = slide_data.get("body", "")

    # Başlık
    title_font = load_font(title_font_for(title), 80)
    tlines = wrap_text(title, title_font, CANVAS_W - 120, draw)
    cur_y = draw_multiline_center(draw, tlines, title_font, palette["accent"], 110, 1.05)

    # Paragraf
    body_font = load_font(FONT_BODY, 42)
    blines = wrap_text(body, body_font, CANVAS_W - 140, draw)
    draw_multiline_center(draw, blines, body_font, palette["text"], cur_y + 30, 1.3)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


def render_concept(raw_path, out_path, slide_data, palette):
    """Anahtar kavram — tek kelime başlık + 1-2 cümle."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    title = slide_data.get("title_accent", "")
    body = slide_data.get("body", "")

    title_font = load_font(title_font_for(title), 110)
    tlines = wrap_text(title, title_font, CANVAS_W - 120, draw)
    cur_y = draw_multiline_center(draw, tlines, title_font, palette["text"], 120, 1.05)

    body_font = load_font(FONT_BODY, 44)
    blines = wrap_text(body, body_font, CANVAS_W - 160, draw)
    draw_multiline_center(draw, blines, body_font, palette["text"], cur_y + 20, 1.3)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


def render_cta(raw_path, out_path, slide_data, palette):
    """Kapanış + Sincap Kitap CTA."""
    img = Image.open(raw_path).convert("RGBA").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    body = slide_data.get("body", "")
    body_font = load_font(FONT_BODY, 52)
    lines = wrap_text(body, body_font, CANVAS_W - 160, draw)
    draw_multiline_center(draw, lines, body_font, palette["text"], 130, 1.3)

    paste_logo(img)
    img.convert("RGB").save(out_path, "PNG")
    print(f"[OK] {out_path}")


# === ANA AKIŞ ===

RENDERERS = {
    "cover": render_cover,
    "inner": render_inner,
    "quote": render_quote,
    "tip": render_tip,
    "concept": render_concept,
    "cta": render_cta,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 overlay_text.py <layout.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        config = json.load(f)

    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    palette = config["palette"]
    slides = config["slides"]

    for slide in slides:
        renderer = RENDERERS.get(slide["type"])
        if not renderer:
            print(f"[ERR] Bilinmeyen slide type: {slide['type']}")
            continue
        renderer(slide["raw_image"], slide["output"], slide, palette)

    print(f"\n[DONE] {len(slides)} slide işlendi → {output_dir}")


if __name__ == "__main__":
    main()
