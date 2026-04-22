#!/usr/bin/env bash
# Sincap Kitap IG — 2026-04-22 Öğle 12:00
# Konu: Öfke patlaması | Karakter: Ayı yavrusu | Palette: MERCAN #F08A7B
#
# NOT: Bu ortamda (Claude Code cloud harness) platform.higgsfield.ai egress allowlist'te
# olmadığı için bu komutları yerel makinenizde ya da Higgsfield erişimi olan bir
# ortamda çalıştırın. Çıktılar outputs/2026-04-22-ogle-12/raw/ altına kaydedilecek.

set -euo pipefail

export HIGGSFIELD_API_KEY="b0ce4df9-80ac-44a3-8f9d-be0869a428e1"
export HIGGSFIELD_API_SECRET="be73a38e07e4faebd09666eb51d1fe04eea7feea96d83b81ca4640d33531e35c"

REF="https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"
OUT_DIR="outputs/2026-04-22-ogle-12/raw"
BASE="Children's book illustration, watercolor gouache painting, textured brush strokes, cute fluffy bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F08A7B coral background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation"

mkdir -p "$OUT_DIR"

# --- Slide 1 — KAPAK (dynamic expressive pose) ---
python3 scripts/higgsfield_api.py \
  --prompt "$BASE, bear cub with big emotional expression, tiny stylized volcano puff above head, tearful but adorable, small fists clenched, 5-8 decorative elements around: floating hearts, small sparkles, soft clouds, tiny stars" \
  --output "$OUT_DIR/slide-1-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "$REF"

# --- Slide 2 — SEVGİ (warm loving interaction) ---
python3 scripts/higgsfield_api.py \
  --prompt "$BASE, bear cub being hugged warmly by a loving parent bear, tender embrace, calm soothing mood, eyes closing peacefully, tiny soft clouds around, warm loving interaction" \
  --output "$OUT_DIR/slide-2-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "$REF"

# --- Slide 3 — İHTİYAÇ (isolated, vulnerable) ---
python3 scripts/higgsfield_api.py \
  --prompt "$BASE, small bear cub alone in vast empty space, tiny scale against big background, sitting on floor with knees pulled up, vulnerable lonely pose, looking at camera with big sad eyes, feeling overwhelmed by huge emotions, a few drifting clouds in distance" \
  --output "$OUT_DIR/slide-3-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "$REF"

# --- Slide 4 — EBEVEYN NOTU (bonding) ---
python3 scripts/higgsfield_api.py \
  --prompt "$BASE, calm cozy scene of parent bear and bear cub sitting together on a soft rug, parent gently crouched at child's eye level, bear cub feeling heard, both calm and connected, gentle bonding moment, a few floating heart shapes" \
  --output "$OUT_DIR/slide-4-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "$REF"

# --- Slide 5 — KAPANIŞ (goodbye wave + book stack) ---
python3 scripts/higgsfield_api.py \
  --prompt "$BASE, bear cub waving goodbye with a big cheerful smile, small stack of storybooks next to the cub, calm sunny mood, a tiny cloud and a little star above" \
  --output "$OUT_DIR/slide-5-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "$REF"

echo
echo "Tüm illüstrasyonlar hazır. Şimdi metin bindirme:"
echo "  python3 scripts/overlay_text.py outputs/2026-04-22-ogle-12/layout.json"
