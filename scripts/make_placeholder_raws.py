#!/usr/bin/env python3
"""Sandbox fallback — Higgsfield API bloke olduğunda solid-color placeholder üret.

Kullanım:
    python3 scripts/make_placeholder_raws.py \
        --dir outputs/2026-04-23-sabah-9/raw \
        --bg "#C9DDEC" --count 5
"""
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dir", required=True)
    p.add_argument("--bg", required=True)
    p.add_argument("--count", type=int, default=5)
    p.add_argument("--w", type=int, default=1080)
    p.add_argument("--h", type=int, default=1350)
    args = p.parse_args()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        font = ImageFont.truetype("assets/fonts/Baloo2-Regular.ttf", 28)
    except Exception:
        font = ImageFont.load_default()

    for i in range(1, args.count + 1):
        img = Image.new("RGB", (args.w, args.h), args.bg)
        draw = ImageDraw.Draw(img)
        label = f"[placeholder] slide-{i} — Higgsfield bloke (sandbox allowlist)"
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((args.w - tw) // 2, args.h // 2 + 420), label, fill="#4A2E1A", font=font)
        out = out_dir / f"slide-{i}-raw.png"
        img.save(out, "PNG")
        print(f"[OK] {out}")


if __name__ == "__main__":
    main()
