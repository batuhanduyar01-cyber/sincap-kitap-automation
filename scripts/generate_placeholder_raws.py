#!/usr/bin/env python3
"""
Higgsfield API ortamda erişilemediği durumlar için fallback.
character-reference.png'yi sıcak bir arkaplana yerleştirip 4:5 raw çıktıları üretir.
Gerçek üretimde Higgsfield ile değiştirilmeli.
"""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 1080, 1350
BG = (233, 126, 40)  # #E97E28 turuncu (ikindi paleti)
REF = Image.open("assets/character-reference.png").convert("RGBA")

OUT = Path("outputs/2026-04-22-ikindi-15/raw")
OUT.mkdir(parents=True, exist_ok=True)


def make(slide_no: int, char_height: int, x_off: int, y_off: int):
    canvas = Image.new("RGB", (W, H), BG)
    ratio = char_height / REF.height
    cw = int(REF.width * ratio)
    char = REF.resize((cw, char_height), Image.LANCZOS)
    cx = (W - cw) // 2 + x_off
    cy = (H - char_height) // 2 + y_off
    canvas.paste(char, (cx, cy), char)
    out_path = OUT / f"slide-{slide_no}-raw.png"
    canvas.save(out_path, "PNG")
    print(f"[OK] {out_path}")


# Her slide için karakter biraz farklı yerde: kompozisyon çeşitliliği
make(1, 540, 0, 250)        # KAPAK - alt yarıda
make(2, 480, 0, 320)        # ÇERÇEVE - alt
make(3, 520, 0, 280)        # KAVRAM - alt
make(4, 480, 0, 320)        # UNUTMAYIN - alt
make(5, 560, 0, 230)        # CTA - merkez-alt
