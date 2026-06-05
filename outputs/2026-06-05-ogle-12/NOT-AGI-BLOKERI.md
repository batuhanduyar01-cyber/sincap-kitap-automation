# Higgsfield Görselleri Üretilemedi — Sandbox Allowlist Blokeri

**Tarih:** 2026-06-05 öğle 12:00
**Slot:** 2026-06-05-ogle-12

## Ne oldu?

Hem `https://vercel-hf-probe.vercel.app` (relay) hem de `https://higgsfield.ai/` (doğrudan), bu Routine container'ından **403 "Host not in allowlist"** ile reddedildi. Bu yanıt Vercel'den ya da Higgsfield'dan değil — sandbox network policy'sinden geliyor; istek hedef sunucuya hiç ulaşmadan kesiliyor.

```
HTTP 403
Host not in allowlist
```

Aynı yanıt iki host için de geldi, secret/auth header'larından bağımsız.

## Sonuç

Bu çalışmada:
- ✅ Konu seçildi, log güncellendi (`kreşe gitmek istememe`)
- ✅ 5 slide metni + caption + 20 hashtag üretildi (`icerik.md`, `caption.txt`)
- ✅ Higgsfield prompt'ları kaydedildi (`raw/higgsfield-prompts.json`) — relay tekrar açıldığında submit edilebilir
- ⚠️ **Ham görseller MERCAN (#F08A7B) düz renk placeholder olarak oluşturuldu.** Overlay metin/logoyu yerleştirdi ama altta watercolor tavşan illüstrasyonu YOK.
- ✅ Layout + overlay pipeline çalıştı

## Düzeltmek için

Routine'in environment ayarlarına şu hostların eklenmesi gerekiyor:
- `vercel-hf-probe.vercel.app` (öncelikli — birincil yol)
- `higgsfield.ai` (yedek)

Allowlist güncellendikten sonra `raw/higgsfield-prompts.json` doğrudan `scripts/relay_api.py submit-batch` ile tekrar gönderilebilir; ardından `python3 scripts/overlay_text.py outputs/2026-06-05-ogle-12/layout.json` overlay'i tekrar üretir.
