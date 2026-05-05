# Relay Submit Durumu — 2026-05-05 İkindi 15:00

**Sonuç:** Görsel üretimi yapılamadı.

## Hata
```
POST https://vercel-hf-probe.vercel.app/api/hf/submit
HTTP 403
x-deny-reason: host_not_allowed
body: "Host not in allowlist"
```

Aynı yanıt `/`, `/api/hf/health` gibi endpointlerde de döndü — yani hata bizim
çağrı içeriğimizle (prompts / secret) ilgili değil. Vercel relay bu oturumun
çalıştığı host'u allowlist'inde tanımıyor; relay yalnızca Anthropic Routine
runner IP'lerinden gelen istekleri kabul edecek şekilde kilitli.

## Beklenen Akış
- Routine UI üzerinden 15:00 cron tetiklenir → submit allowlist'i geçer.
- 5 PNG `assets/gorseller/2026-05-05-ikindi-15/slide-{1..5}.png` olarak
  branch'e commit'lenir.
- `python3 scripts/overlay_text.py outputs/2026-05-05-ikindi-15/layout.json`
  çalıştırılır → final 5 slide `outputs/2026-05-05-ikindi-15/slide-{1..5}.png`
  olarak üretilir.

## Manuel Devam
Bu oturumda 5 slide'lık metin + caption + hashtag + layout.json + prompts.json
hazır. Operatör veya planlanmış Routine PNG'leri eklediğinde overlay tek
komutla biter:

```bash
python3 scripts/overlay_text.py outputs/2026-05-05-ikindi-15/layout.json
```
