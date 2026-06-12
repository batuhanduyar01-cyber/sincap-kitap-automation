# Görsel üretimi atlandı — ağ egress bloğu

Routine 2026-06-12 ikindi 15:00 çalıştı, **metin/içerik tamamlandı**, ancak
Higgsfield görselleri üretilemedi.

## Bloklanan hostlar (sandbox egress policy)

```
POST https://vercel-hf-probe.vercel.app/api/hf/submit
  → 403 "Host not in allowlist: vercel-hf-probe.vercel.app.
         Add this host to your network egress settings to allow access."

HEAD https://platform.higgsfield.ai/v1/text2image/soul
  → 403 (egress aynı şekilde bloklu)
```

İki yol da kapalı: ne relay ne de Higgsfield doğrudan ulaşılabilir.

## Çözüm

Bu environment'in **Network egress settings** ekranına şu hostları ekleyin:

- `vercel-hf-probe.vercel.app` (relay — birincil yol)
- (opsiyonel yedek) `platform.higgsfield.ai`

Routine'i tekrar tetiklediğinizde Adım 4'ten devam edecek:

```bash
SLOT="2026-06-12-ikindi-15"
BRANCH="claude/zen-wozniak-ltpp54"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-env-deki-secret>" \
python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-06-12-ikindi-15/raw/prompts.json
```

Sonra:
```bash
python3 scripts/overlay_text.py outputs/2026-06-12-ikindi-15/layout.json
```

## Bu çalıştırmada hazır olan içerik

- `icerik.md` — 5 slide metni (konu: Hayal Gücü, palette: Turuncu)
- `caption.txt` — Instagram caption (~530 kelime) + 20 hashtag
- `layout.json` — overlay_text.py için tam config
- `raw/prompts.json` — Higgsfield için 5 prompt (relay submit'e hazır)
- `logs/ikindi-15.md` — konu kaydı eklendi
