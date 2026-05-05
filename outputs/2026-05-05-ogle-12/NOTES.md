# 2026-05-05 Öğle 12:00 — Çalıştırma Notu

## Durum: KISMEN TAMAMLANDI — görsel üretim adımı manuel müdahale bekliyor

## Hazır olanlar
- `icerik.md` — 5 slide metni (kapak / 2 alıntı / ebeveyn notu / kapanış)
- `caption.txt` — Instagram açıklaması + 20 hashtag
- `prompts.json` — 5 Higgsfield prompt'u (slot=`2026-05-05-ogle-12`, palette=Hardal #F5C82E)
- `layout.json` — `scripts/overlay_text.py` için hazır konfigürasyon

## Engel: Relay erişimi
Bu Routine session'ı, Vercel relay'e (`vercel-hf-probe.vercel.app`) doğrudan erişemiyor.
Sandbox/agent harness, allowlist dışı host'lara giden trafiği `403 host_not_allowed`
ile bloklayarak `relay_api.py submit` çağrısını boşa düşürdü.

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
exit=3
```

## Manuel tamamlama adımları (yerel makinede)

```bash
git fetch origin
git checkout claude/confident-dijkstra-RVfMh
git pull --ff-only origin claude/confident-dijkstra-RVfMh

cp outputs/2026-05-05-ogle-12/prompts.json /tmp/prompts.json

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-env-deki-gerçek-değer>" \
python3 scripts/relay_api.py submit-batch \
  --slot 2026-05-05-ogle-12 \
  --branch claude/confident-dijkstra-RVfMh \
  --prompts-file /tmp/prompts.json

# Görseller commit'lendikten sonra:
git pull --ff-only origin claude/confident-dijkstra-RVfMh
python3 scripts/overlay_text.py outputs/2026-05-05-ogle-12/layout.json

git add outputs/2026-05-05-ogle-12/slide-*.png
git commit -m "Sincap Kitap IG post: 2026-05-05 öğle 12:00 - ben yaparım ısrarı (final overlay)"
git push origin claude/confident-dijkstra-RVfMh
```

## Bilgilendirme
- Karakter: minik tilki yavrusu (5 slide'da sabit)
- Palette: HARDAL #F5C82E (zemin) / MOR #7E5BA0 (aksan) / KOYU KAHVE #3D2817 (gövde metni)
- Konu son 14 günde kullanılmadı (ilk girdi); `logs/ogle-12.md` güncellendi.
