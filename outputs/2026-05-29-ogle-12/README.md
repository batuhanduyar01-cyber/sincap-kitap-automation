# 2026-05-29 — Öğle 12:00 — Diş Fırçalatmama

## Durum

- Metin, caption, hashtag, layout JSON ve Higgsfield prompt'ları hazır.
- **Görseller üretilemedi** — bu Claude Code remote ortamı, hem `vercel-hf-probe.vercel.app` hem `api.higgsfield.ai` adreslerine erişimde 403 "Host not in allowlist" döndürdü. Sadece github.com gibi izin verilen hostlara çıkış var.

## Üretmek için

`RELAY_URL` ve `RELAY_SHARED_SECRET` env'lerine erişebilen bir ortamda:

```bash
SLOT="2026-05-29-ogle-12"
BRANCH="claude/confident-dijkstra-GHLxM"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-29-ogle-12/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-29-ogle-12/layout.json
```

## Çıktılar

- `icerik.md` — 5 slide metni + ebeveyn notu
- `caption.txt` — Instagram caption (~340 kelime) + 20 hashtag
- `layout.json` — overlay_text.py için layout config
- `prompts.json` — Higgsfield için 5 prompt
- `slide-{1..5}.png` — overlay sonrası (henüz üretilmedi)
- `raw/` — ham Higgsfield çıktılarının kopyası (boş)

## Palette

| Rol | Renk |
|---|---|
| Background | `#E97E28` (TURUNCU) |
| Accent | `#7E5BA0` (MOR) |
| Text | `#3D2817` (KOYU KAHVE) |
