# Rapor — Sincap Kitap IG Sabah 09:00

**Tarih:** 2026-04-27
**Slot:** `2026-04-27-sabah-9`
**Branch:** `claude/quirky-mendel-aiM7v`

## Seçilen Konu
**Uyku direnci** (0-6 yaş). `logs/sabah-9.md` boştu, son 14 gün içinde tekrar yok.

## Seçilen Palette
**MOR**
- Arka plan: `#7E5BA0`
- Aksan: `#C5E86C` (limon yeşili)
- Metin: `#FFFFFF` (beyaz)

Karakter: bear cub (5 slide boyunca aynı).

## Görseller (final)
- `outputs/2026-04-27-sabah-9/slide-1.png` — KAPAK
- `outputs/2026-04-27-sabah-9/slide-2.png` — TANIDIK SAHNE
- `outputs/2026-04-27-sabah-9/slide-3.png` — ÇOCUĞUN SESİ (alıntı)
- `outputs/2026-04-27-sabah-9/slide-4.png` — UNUTMAYIN
- `outputs/2026-04-27-sabah-9/slide-5.png` — KAPANIŞ

Ham görseller `outputs/2026-04-27-sabah-9/raw/slide-*-raw.png` ve repo'daki üretim yolu `assets/gorseller/2026-04-27-sabah-9/slide-*.png` altında.

## ⚠️ Higgsfield relay BAŞARISIZ — Geçici çözüm uygulandı
ADIM 4b çağrısı `POST https://vercel-hf-probe.vercel.app/api/hf/submit` üzerinden:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
exit=3
```

**Olası sebep:** Routine prompt'unda `RELAY_SHARED_SECRET` placeholder
(`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`)
gerçek Vercel değeriyle değiştirilmemiş, ya da bu çalıştırma ortamının çıkış IP'si
relay'in caller allowlist'inde değil.

**Geçici çözüm:** 5 slide için `#7E5BA0` solid arkaplanlı 1152×1536 PNG'ler
oluşturuldu ve `assets/gorseller/<slot>/slide-N.png` yoluna yerleştirildi. Bu
görseller akabinde `scripts/overlay_text.py`'a beslendi; başlık, alt metin, alıntı
ve logo doğru biçimde bindirildi. **Sonuç görselleri tipografi/yerleşim açısından
doğru ama Higgsfield'ın suluboya illüstrasyonlarına sahip değil.** İllüstrasyonlu
versiyon için Routine UI'de doğru `RELAY_SHARED_SECRET`'i ayarlayıp aynı slot
adıyla yeniden çalıştırmak yeterli — overlay aynı sonucu üretir.

`/tmp/prompts.json` (= `outputs/2026-04-27-sabah-9/prompts.json`) Higgsfield'a
gönderilmek üzere hazır bekliyor.

## Caption (ilk 3 satır)
> Saat dokuzu vurdu. Pijamalar giyildi, dişler fırçalandı, ışıklar yumuşadı. Ama o, hâlâ koridorda zıplıyor. "Bir kitap daha, anne." "Su istiyorum." "Hadi bir oyun daha." 🌙
>
> Sen, kanepeye yığılmış, içinden "ne olur uyu artık" diye sayıyorsun belki. Bu sahneyi bilenlerden misin? Yalnız değilsin. Türkiye'nin her evinde, bu dakikalarda, aynı küçük sahne sahneye konuyor.
>
> Ama şunu fark etmek bazen kalbimizi yumuşatır: 0-6 yaş çocuğu için "uyumak" demek, "anneden ayrılmak" demek. Onun için yatak, koca bir denizin başlangıcı.

Tam caption + 20 hashtag: `outputs/2026-04-27-sabah-9/caption.txt`.

## Üretilen dosyalar
```
outputs/2026-04-27-sabah-9/
├── RAPOR.md            (bu dosya)
├── caption.txt
├── icerik.md
├── layout.json
├── prompts.json        (Higgsfield için hazır prompt'lar)
├── slide-1.png ... slide-5.png      (final, metin bindirilmiş)
└── raw/
    └── slide-1-raw.png ... slide-5-raw.png   (ham, fallback solid bg)

assets/gorseller/2026-04-27-sabah-9/
└── slide-1.png ... slide-5.png      (overlay'in girdisi olan ham)

logs/sabah-9.md   (`- 2026-04-27: uyku direnci` satırı eklendi)
```
