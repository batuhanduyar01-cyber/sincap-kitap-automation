# Handoff — 2026-04-27 Öğle 12:00 (diş fırçalatmama)

## Durum
Metin, prompts, layout hazır. **Görseller üretilemedi** çünkü bu Claude Code sandbox'ı `vercel-hf-probe.vercel.app` host'una çıkışa izin vermiyor (`x-deny-reason: host_not_allowed`). Relay, Anthropic Routine UI'dan tetiklenmek üzere tasarlanmış; bu sandbox'tan erişilemiyor.

## Hazır olan
- `outputs/2026-04-27-ogle-12/icerik.md` — 5 slide metni + caption + hashtag
- `outputs/2026-04-27-ogle-12/caption.txt` — IG caption (kopyala-yapıştıra hazır)
- `outputs/2026-04-27-ogle-12/prompts.json` — 5 Higgsfield prompt'u
- `outputs/2026-04-27-ogle-12/layout.json` — overlay_text.py için hazır
- `logs/ogle-12.md` — `2026-04-27: diş fırçalatmama` eklendi

## Bitirme adımları (Routine UI'dan veya relay'e erişimi olan terminalden)

```bash
git fetch origin && git checkout claude/confident-dijkstra-zdqdY && git pull
cp outputs/2026-04-27-ogle-12/prompts.json /tmp/prompts.json

export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<vercel env değeri>"
python3 scripts/relay_api.py submit-batch \
    --slot   "2026-04-27-ogle-12" \
    --branch "claude/confident-dijkstra-zdqdY" \
    --prompts-file /tmp/prompts.json

# Webhook PNG'leri commit'leyince
git pull --ff-only origin claude/confident-dijkstra-zdqdY
python3 scripts/overlay_text.py outputs/2026-04-27-ogle-12/layout.json
git add outputs/2026-04-27-ogle-12/slide-*.png
git commit -m "Sincap Kitap IG post: 2026-04-27 öğle 12:00 - diş fırçalatmama"
git push -u origin claude/confident-dijkstra-zdqdY
```

## Konu / Palette / Karakter
- **Konu:** Diş fırçalatmama
- **Palette:** TOZ MAVİSİ #C9DDEC (bg) / MOR #7E5BA0 (accent) / KOYU KAHVE #3D2817 (text)
- **Karakter:** Sevimli beyaz tavşan, iki belirgin ön diş, yumuşak pembe kulaklar
