# BLOCKER — Görsel Üretimi Yapılamadı

**Tarih:** 2026-06-12
**Slot:** öğle 12:00 (diş fırçalatmama)

## Sorun

Bu Routine'un çalıştığı oturumun ağ egress allowlist'i `vercel-hf-probe.vercel.app` host'unu içermiyor. `scripts/relay_api.py submit-batch` ilk POST'ta `403 Host not in allowlist` döndü:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist: vercel-hf-probe.vercel.app. Add this host to your network egress settings to allow access."}
```

Dolayısıyla:
- Higgsfield'a 5 prompt **gönderilemedi**.
- `assets/gorseller/2026-06-12-ogle-12/slide-*.png` üretilmedi.
- Adım 5'teki `overlay_text.py` ham görsel olmadığı için çalıştırılmadı.

## Çözüm

Aşağıdakilerden biri:

1. **Bu oturumun network egress allowlist'ine `vercel-hf-probe.vercel.app` ekle.** (Tercih edilen — relay'i bu amaçla kurmuşsunuz.)
2. Egress'i değiştiremiyorsan, lokal bir makinede aynı komutu çalıştır:
   ```bash
   git fetch origin claude/confident-dijkstra-flwn6p && git checkout claude/confident-dijkstra-flwn6p
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<gerçek sır>" \
   python3 scripts/relay_api.py submit-batch \
     --slot 2026-06-12-ogle-12 \
     --branch claude/confident-dijkstra-flwn6p \
     --prompts-file outputs/2026-06-12-ogle-12/higgsfield-prompts.json
   ```
   Relay PNG'leri `assets/gorseller/2026-06-12-ogle-12/slide-{1..5}.png` olarak commit'leyecek. Sonra:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-06-12-ogle-12/layout.json
   ```

## Hazır Olan Çıktılar

Bu klasör altında, görseller geldiğinde hemen overlay'lenmeye hazır:

- `icerik.md` — konu, palette, karakter, slide metinleri, Higgsfield prompt iskeleti
- `caption.txt` — Instagram caption + 20 hashtag
- `layout.json` — `overlay_text.py` config
- `higgsfield-prompts.json` — relay'e gönderilecek 5 prompt
