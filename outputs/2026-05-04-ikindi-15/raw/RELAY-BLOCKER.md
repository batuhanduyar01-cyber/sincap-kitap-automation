# Görsel Üretimi Bloklu — RELAY_SHARED_SECRET Placeholder

`scripts/relay_api.py submit-batch` çağrısı 403 ile döndü:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
```

**Sebep:** Routine prompt'unda `RELAY_SHARED_SECRET` değeri placeholder
(`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`) olarak
bırakıldı; Vercel'deki gerçek secret ile değiştirilmemiş.

**Çözüm — Routine UI'de prompt'u güncelle:**

1. Vercel → `vercel-hf-probe` projesi → Settings → Environment Variables →
   `RELAY_SHARED_SECRET` değerini kopyala.
2. Routine prompt'undaki ADIM 4b bloğunda yer alan
   `78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`
   ifadesini bu gerçek değerle değiştir.
3. Routine'i yeniden tetikle.

**Bu post için hazır olanlar (sadece görseller eksik):**

- `outputs/2026-05-04-ikindi-15/icerik.md` — slide metinleri
- `outputs/2026-05-04-ikindi-15/caption.txt` — IG caption + hashtag
- `outputs/2026-05-04-ikindi-15/raw/prompts.json` — Higgsfield prompt'ları
- `outputs/2026-05-04-ikindi-15/raw/layout.json` — overlay konfigürasyonu
- `logs/ikindi-15.md` — konu logu güncellendi

Secret düzeltildikten sonra şunlar tekrar çalıştırılır:

```
SLOT="2026-05-04-ikindi-15"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<GERÇEK-VERCEL-SECRET>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file outputs/$SLOT/raw/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/$SLOT/raw/layout.json
```
