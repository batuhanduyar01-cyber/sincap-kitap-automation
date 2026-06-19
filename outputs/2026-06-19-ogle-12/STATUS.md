# Çalışma Durumu — 2026-06-19 Öğle 12:00

## ❌ BLOKAJ: Relay endpoint network allowlist'te DEĞİL

Vercel relay'e istek atıldı, Routine ortamının network egress policy'si reddetti:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access.
```

Bu yüzden bu run'da Higgsfield görselleri üretilemedi. Aynı blokaj sabah-9 ve ikindi-15 routine'leri için de geçerli olacak — Routine ortamının network policy'sine `vercel-hf-probe.vercel.app` eklenene kadar hiçbir slot görsel üretemez.

## ✅ Bu run'da tamamlanan

- Konu seçimi ve log kaydı (`logs/ogle-12.md`)
- 5 slide Türkçe metin (çocuk sesi ağırlıklı)
- IG caption (300-400 kelime) + 20 hashtag
- Palette seçimi (HARDAL)
- 5 Higgsfield prompt'u (`raw/prompts.json` — hazır submit edilmek için)
- `layout.json` (overlay_text.py için)

## 🔁 Relay açıldıktan sonra yapılacaklar

1. Network policy'ye `vercel-hf-probe.vercel.app` eklensin.
2. (Opsiyonel) Higgsfield için doğrudan da açılırsa: `*.higgsfield.ai`.
3. Bu klasördeki `raw/prompts.json` ile tekrar submit:

```bash
SLOT="2026-06-19-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek-secret>" \
python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-06-19-ogle-12/raw/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-06-19-ogle-12/layout.json
```

4. `outputs/2026-06-19-ogle-12/slide-1..5.png` oluşur, post yayına hazır.

## Notlar

- Fontlar bu run'da indirildi (`assets/fonts/BagelFatOne-Regular.ttf`, `Baloo2-Regular.ttf`) — sonraki run'lar için commit'lendi.
- Pillow yerel kuruldu, gelecek run'larda mevcut olmazsa `pip install Pillow` gerekir.
