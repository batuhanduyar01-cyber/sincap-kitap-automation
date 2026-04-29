# Routine Durumu — 2026-04-29 Sabah 09:00

## ⚠️ ENGELLENDİ (BLOCKED): Higgsfield görsel üretimi

### Hata
Routine sandbox'ından tüm outbound HTTP istekleri **`HTTP 403 — Host not in allowlist`** ile reddediliyor.
Test edilen hostlar (hepsi 403):

- `https://vercel-hf-probe.vercel.app` (relay) → 403
- `https://example.com` → 403
- `https://api.github.com` → 403
- `https://anthropic.com` → 403
- `https://higgsfield.ai` → 403

DNS çözümleme çalışıyor; problem sandbox'ın egress proxy allowlist'inde.
`relay_api.py submit-batch` exit kodu **3** (submit failed).

### Tamamlananlar (commit'lendi)
- Konu: **uyku direnci** (logs/sabah-9.md güncellendi)
- Palette: **TOZ MAVİSİ** (`#C9DDEC` / `#E97E28` / `#4A2E1F`)
- Karakter: hedgehog
- 5 slide metni: `icerik.md`
- Caption (~480 kelime) + 20 hashtag: `caption.txt`
- Higgsfield 5 prompt: `prompts.json`
- Overlay konfigi: `layout.json`

### Eksik (manuel veya bir sonraki çağrıda)
1. Sandbox allowlist'i genişletilince (veya egress'i açık bir runner'da) tekrar koş:
   ```bash
   export RELAY_URL="https://vercel-hf-probe.vercel.app"
   export RELAY_SHARED_SECRET="<vercel'deki gerçek değer>"
   python3 scripts/relay_api.py submit-batch \
       --slot   "2026-04-29-sabah-9" \
       --branch "claude/quirky-mendel-UHFQZ" \
       --prompts-file outputs/2026-04-29-sabah-9/prompts.json
   ```
2. Webhook commit'lerini çek:
   ```bash
   git pull --ff-only origin claude/quirky-mendel-UHFQZ
   ```
3. Metin bindirme:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-04-29-sabah-9/layout.json
   ```
4. Final commit/push.

### Notlar
- Yarım kalmış post commit'lenmedi; commit mesajı `WIP` ile işaretli.
- `assets/gorseller/2026-04-29-sabah-9/` klasörü oluşturuldu ama boş.
- Konu `logs/sabah-9.md`'ye yazıldığı için 14 günlük tekrar kontrolü bu konuyu artık dışlar — yeniden çalıştırırken konuyu silmeden aynı slot'u tamamlayabilirsin.
