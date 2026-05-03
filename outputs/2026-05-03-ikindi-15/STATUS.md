# 2026-05-03 İkindi 15:00 — Çalıştırma Durumu

**Konu:** Duygu Adlandırma
**Slot:** `2026-05-03-ikindi-15`
**Branch:** `claude/zen-wozniak-asmbS`
**Palette:** Turuncu (`#E97E28` / `#FFFFFF` / `#2A1810`)

## Tamamlanan adımlar
- [x] Konu seçimi + log güncelleme (`logs/ikindi-15.md`)
- [x] 5 slide metni (`icerik.md`)
- [x] Caption + hashtag (`caption.txt`, ~430 kelime, 20 hashtag)
- [x] Higgsfield prompt'ları (`prompts.json`)
- [x] Overlay layout (`layout.json`)

## Bloke olan adımlar
- [ ] **Higgsfield görsel üretimi** — `relay_api.py submit-batch` HTTP **403 "Host not in allowlist"** döndü.
  Vercel relay (`https://vercel-hf-probe.vercel.app`) yalnızca Anthropic Routine runner IP'lerini allowlist'inde tutuyor; bu Claude Code session'ının çıkış IP'si listede değil. Aynı prompt zamanlanmış Routine içinden tetiklendiğinde relay submit'i kabul edecek.
- [ ] **`overlay_text.py`** — ham `assets/gorseller/2026-05-03-ikindi-15/slide-{1..5}.png` dosyaları gelmeden çalışmaz (girdi PNG bekliyor).

## Devam etmek için
1. Bu prompt'u Routine olarak (saat 15:00 cron) tetikle — runner'ın çıkış IP'si relay allowlist'inde olduğu için submit geçer.
2. Veya bu branch'te elle: `RELAY_SHARED_SECRET=... RELAY_URL=https://vercel-hf-probe.vercel.app python3 scripts/relay_api.py submit-batch --slot 2026-05-03-ikindi-15 --branch claude/zen-wozniak-asmbS --prompts-file outputs/2026-05-03-ikindi-15/prompts.json`
3. Webhook 5 PNG'yi `assets/gorseller/2026-05-03-ikindi-15/slide-{1..5}.png` olarak commit'leyince:
   `python3 scripts/overlay_text.py outputs/2026-05-03-ikindi-15/layout.json`
