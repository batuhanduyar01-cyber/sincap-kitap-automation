# Durum — 2026-05-14 İkindi 15:00

**Konu:** Korkularla başa çıkma
**Slot:** 2026-05-14-ikindi-15

## Tamamlanan adımlar

1. ADIM 1 — Tekrar kontrolü yapıldı (loglar boş, konu çakışması yok). `logs/ikindi-15.md` güncellendi.
2. ADIM 2 — Türkçe slide metinleri, caption (≈440 kelime) ve 20 hashtag yazıldı → `icerik.md`, `caption.txt`.
3. ADIM 3 — Palette: Turuncu (bg `#E97E28` / accent `#FFFFFF` / text `#2A1810`).
4. ADIM 4a — 5 Higgsfield prompt'u hazırlandı → `raw/prompts.json`.

## ADIM 4b blokeri — relay allowlist (403)

Vercel relay `https://vercel-hf-probe.vercel.app` bu Routine runner'ını kabul etmiyor:

```
GET  /                 -> HTTP 403
POST /api/hf/submit    -> HTTP 403   body: "Host not in allowlist"
```

Hata mesajı doğrudan relay'in kendi gövdesinden geliyor (Cloudflare WAF değil, relay'in
IP/host allowlist'i). Bu nedenle bu oturumdan görselleri üretip GitHub'a commit'leyemedik.

## Sonraki adımlar (allowlist'te bir host'tan çalıştırmak için)

```bash
SLOT="2026-05-14-ikindi-15"
BRANCH="claude/zen-wozniak-zuaOf"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-env-deki gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-14-ikindi-15/raw/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-14-ikindi-15/layout.json
```

Görseller `assets/gorseller/2026-05-14-ikindi-15/slide-1..5.png` olarak indikten sonra
`overlay_text.py` overlay edip `outputs/2026-05-14-ikindi-15/slide-1..5.png` üretir.

## Olası çözümler

- Vercel `vercel-hf-probe` projesinin IP/host allowlist'ine Routine runner'ının
  egress IP aralığını ekle.
- Allowlist'i `RELAY_SHARED_SECRET` ile birlikte Authorization header'a güvenip
  IP-kısıtsız hale getir (riskli; bearer-only auth yeterli ise).
