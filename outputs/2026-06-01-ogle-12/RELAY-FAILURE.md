# Görsel Üretimi Başarısız — 2026-06-01 Öğle 12:00

## Hata

`scripts/relay_api.py submit-batch` çağrısı **HTTP 403** ile döndü:

```
{"_raw": "Host not in allowlist"}
```

## Sebep

Routine prompt'undaki `RELAY_SHARED_SECRET` placeholder değeri
(`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`)
Vercel'deki gerçek `RELAY_SHARED_SECRET` ile **değiştirilmeden** çalıştırıldı.
Bu değer relay tarafında allowlist kontrolünü geçemediği için submit reddediliyor.

## Test edilen istek

```
POST https://vercel-hf-probe.vercel.app/api/hf/submit
Authorization: Bearer 78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4
Body: {"slot": "2026-06-01-ogle-12",
       "branch": "claude/confident-dijkstra-4nnSs",
       "prompts": [...5 prompt...]}
```

## Çözüm

1. Vercel → `vercel-hf-probe` projesi → Environment Variables → `RELAY_SHARED_SECRET` değerini kopyala.
2. Routine prompt'unda iki yerde geçen placeholder hash'i bu gerçek değerle değiştir.
3. Routine'u tekrar tetikle.

## Bu çalıştırmada üretilen içerik

- ✅ `icerik.md` — 5 slide metni (konu: yemeği reddetme)
- ✅ `caption.txt` — Instagram caption + hashtag
- ✅ `logs/ogle-12.md` — konu kaydı güncellendi
- ✅ `/tmp/prompts.json` — Higgsfield prompts (relay düzeltildikten sonra yeniden gönderilebilir)
- ❌ `assets/gorseller/2026-06-01-ogle-12/slide-*.png` — üretilemedi
- ❌ `outputs/2026-06-01-ogle-12/slide-*.png` — overlay yapılamadı (ham görsel yok)
