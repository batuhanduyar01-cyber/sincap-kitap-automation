# Routine Blokeri — 2026-06-25 öğle 12:00

## Olan
ADIM 4 (Higgsfield görsel üretimi) çalıştırılamadı. Vercel relay host'una (`vercel-hf-probe.vercel.app`) bu Routine ortamının HTTPS proxy'si **403 Forbidden** dönüyor (egress policy denial).

```
gateway answered 403 to CONNECT (policy denial or upstream failure)
host: vercel-hf-probe.vercel.app:443
```

Proxy README açıkça "do not retry or route around it — report the blocked host" diyor, bu yüzden alternatif route denenmedi.

## Hazırlananlar (ham olarak burada)
- `icerik.md` — konu, palette, 5 slide metni, hashtag listesi
- `caption.txt` — IG caption (300-400 kelime + hashtag'ler)
- `layout.json` — overlay_text.py için hazır layout (5 slide, palette HARDAL #F5C82E + MOR #7E5BA0)
- `raw/prompts.json` — Higgsfield için 5 prompt (resim yolları `assets/gorseller/2026-06-25-ogle-12/slide-1..5.png` olarak adlandırılmış)
- `logs/ogle-12.md` — "diş fırçalatmama" konusu işaretlendi

## Engel kalktığında devam etmek için
1. `vercel-hf-probe.vercel.app` egress policy'ye whitelist'lenecek **ya da** Routine başka bir ortamda çalıştırılacak.
2. Sonra şu komut çalıştırılır (slot adı korunsun):

   ```bash
   SLOT="2026-06-25-ogle-12"
   BRANCH="claude/confident-dijkstra-fbrs81"
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<gerçek_secret>" \
   python3 scripts/relay_api.py submit-batch \
     --slot "$SLOT" --branch "$BRANCH" \
     --prompts-file outputs/2026-06-25-ogle-12/raw/prompts.json
   ```
3. PNG'ler geldikten sonra:

   ```bash
   git pull --ff-only origin "$BRANCH"
   python3 scripts/overlay_text.py outputs/2026-06-25-ogle-12/layout.json
   ```
