# 2026-05-25 Öğle 12:00 — Durum Notu

## Yapıldı
- Konu seçildi: **yemeği reddetme** (log güncellendi)
- 5 slide metni yazıldı → `icerik.md`
- Instagram caption (300-400 kelime) + 20 hashtag → `caption.txt`
- Palette belirlendi: HARDAL #F5C82E (bg) + MOR #7E5BA0 (accent) + #3D2817 (text)
- 5 Higgsfield prompt'u hazırlandı → `raw/prompts.json`
- Overlay layout hazırlandı → `layout.json`

## BLOKER — Görsel üretimi yapılamadı

Vercel relay (`https://vercel-hf-probe.vercel.app`) bu container'ın egress IP'sini
allowlist'te bulunmadığı için 403 döndürdü:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
```

Aynı hata `/api/hf/status` endpoint'inde de var → relay-tarafı IP filtresi.
Bu, relay'in WAF/middleware katmanında ayarlanmış bir kısıt, secret değil.

## Devam etmek için (allowlist'te bir host'tan, örn. Routine runner)

```bash
cd <repo>
git checkout claude/confident-dijkstra-dy6eL
git pull

SLOT="2026-05-25-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-25-ogle-12/raw/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-25-ogle-12/layout.json
```

## Diğer bekleyen kurulum
- `assets/fonts/` boş (sadece README var). Overlay script default fonta düşer →
  başlıklar incecik görünür. Font dosyalarını eklemek gerek (bkz. `assets/fonts/README.md`).
