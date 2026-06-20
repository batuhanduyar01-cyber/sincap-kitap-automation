# DURUM: YAYINLANMADI — Network Allowlist Engeli

**Tarih/Slot:** 2026-06-20 — öğle 12:00 (`2026-06-20-ogle-12`)
**Konu:** banyo direnci

## Ne Oldu

`scripts/relay_api.py submit-batch` çağrısı `vercel-hf-probe.vercel.app` adresine istek atınca **HTTP 403** ile reddedildi:

```
Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access.
```

Bu, **routine container'ının çıkış (egress) ağ politikası** kaynaklı — Higgsfield WAF değil. Daha önce relay yaklaşımı eklendiğinde (`eb1f3b8 feat: Vercel relay for Higgsfield routing`) host'un routine egress allowlist'ine eklenmesi atlanmış olabilir. Önceki test commitleri (`66acaaa`, `6246c94`, `1a45d11` vb.) farklı bir egress policy ile çalışmış olmalı.

## Yapılması Gereken (manuel)

1. Anthropic Routine UI → bu routine'in environment ayarları → **Network egress allowlist**'e şu host'u ekle:
   ```
   vercel-hf-probe.vercel.app
   ```
2. Routine'i tekrar çalıştır. Bu branch'teki hazır içerik (text + prompts + layout) tekrar kullanılabilir; aşağıdaki adımı çalıştırmak yeterli:
   ```bash
   SLOT="2026-06-20-ogle-12"
   BRANCH="claude/confident-dijkstra-ydhrc9"
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<vercel-secret>" \
     python3 scripts/relay_api.py submit-batch \
     --slot "$SLOT" --branch "$BRANCH" \
     --prompts-file outputs/2026-06-20-ogle-12/raw/higgsfield-prompts.json
   ```
3. 5/5 PNG `assets/gorseller/2026-06-20-ogle-12/` altına commit'lenince:
   ```bash
   git pull --ff-only
   python3 scripts/overlay_text.py outputs/2026-06-20-ogle-12/layout.json
   ```
4. `logs/ogle-12.md` dosyasına şu satırı ekle (bu çalıştırmada eklenmedi, post yayınlanmadığı için):
   ```
   - 2026-06-20: banyo direnci
   ```

## Bu Çalıştırmada Hazırlananlar

- `outputs/2026-06-20-ogle-12/icerik.md` — konu, palette, 5 slide metni, hashtag listesi
- `outputs/2026-06-20-ogle-12/caption.txt` — Instagram caption (~360 kelime)
- `outputs/2026-06-20-ogle-12/layout.json` — overlay_text.py için hazır config
- `outputs/2026-06-20-ogle-12/raw/higgsfield-prompts.json` — 5 Higgsfield prompt'u (TOZ MAVİSİ #C9DDEC, baby sincap karakteri)

Higgsfield görseli yokken `overlay_text.py` çalıştırmadım (raw PNG'leri bekliyor). Allowlist düzeldikten sonra yukarıdaki 4 adımı izleyince post tamamlanır.
