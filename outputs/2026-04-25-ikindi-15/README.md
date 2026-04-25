# 2026-04-25 İkindi 15:00 — Merak

## Durum

- ✅ Konu seçildi: **Merak**
- ✅ Log güncellendi: `logs/ikindi-15.md`
- ✅ Slide metinleri: `icerik.md`
- ✅ Caption + hashtag: `caption.txt`
- ✅ Higgsfield prompt'ları: `prompts.json`
- ✅ Overlay layout: `layout.json`
- ⚠️ Higgsfield görselleri: **ÜRETİLEMEDİ** — Vercel relay 403 (`x-deny-reason: host_not_allowed`) döndürdü; bu ortamın IP'si relay allowlist'inde değil.
- ⏳ PIL overlay: bekliyor (raw görseller gelince çalıştırılacak)

## Relay'in çalışması için

Bu prompt'u ekibin Routine UI'sinden veya allowlist'te olan bir runner'dan çalıştırın:

```bash
export SLOT="2026-04-25-ikindi-15"
export BRANCH="claude/zen-wozniak-zwnhz"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<vercel'deki gerçek secret>"

python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-04-25-ikindi-15/prompts.json

git pull --ff-only origin "$BRANCH"
# overlay-config.json'u layout.json olarak kopyala (layout.json .gitignore'da)
cp outputs/2026-04-25-ikindi-15/overlay-config.json layout.json
python3 scripts/overlay_text.py layout.json
```

## Palette

- **TURUNCU** (ikindi sıcaklığı, merak/keşif teması)
- BG `#E97E28`, accent `#FFFFFF`, text `#2A1810`
- Karakter: baby squirrel
