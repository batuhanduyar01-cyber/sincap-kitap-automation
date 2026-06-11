# Sincap Kitap IG — 2026-06-11 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

Son 14 günde kullanılmamış. `logs/sabah-9.md` güncellendi.

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4A2C1A` (koyu kahve)

Eşleştirme gerekçesi: sakinlik/uyku → TOZ MAVİSİ.

## Karakter
`bear cub` — 5 slide boyunca sabit. Uyku/cozy temasıyla uyumlu sıcak hayvan.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): **Anne, Bir Daha**
- Başlık (aksan): **Uyumayalım...**
- Alt başlık: Uyku direnci, yorgunluğun maskesi olabilir.

### Slide 2 — TANIDIK SAHNE
> Saat geç, enerjiniz tükenmiş; ama o hâlâ kalkmak istiyor. "Bir hikaye daha, bir öpücük daha" diye uzayan ritüel. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Karanlık olunca dünya çok büyük, ben çok küçük kalıyorum."

### Slide 4 — UNUTMAYIN!
> Uykuya direnç, çocuğun günü bırakmakta zorlanmasıdır. Tahmin edilebilir bir rutin, güven kapısını açar. Bugün: "Önce diş, sonra hikaye, sonra ışık kapanır" diye sırayı söze dökün.

### Slide 5 — KAPANIŞ
> Her gece biraz daha kolaylaşacak. Bu yolculukta sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar

Hepsi ortak iskelete (`watercolor gouache, bear cub, #C9DDEC bg, Oliver Jeffers & Marc Boutavant style, no text/frames/borders, portrait`) + slide'a özel sahne:

- **Slide 1:** big bear cub standing on a small hill, decorative leaves and stars around, looking hopeful, holding a tiny moon
- **Slide 2:** bear cub with mother bear character, warm hugging interaction, cozy indoor scene, soft blanket, bedtime warmth
- **Slide 3:** small isolated bear cub character, emotional vulnerable pose, vast empty dark space around with tiny stars, looking up with wide eyes
- **Slide 4:** family scene, parent bear and bear cub reading a storybook together, warm cozy bedroom, soft pillow and blanket, lamp glow
- **Slide 5:** bear cub waving goodbye, smiling, sitting on a stack of storybooks, tiny stars around

JSON prompts dosyası: `/tmp/prompts.json` (slot=`2026-06-11-sabah-9`).

## Görsel Üretim Durumu — ⚠ Relay Bloğu

Higgsfield çağrısı Vercel relay (`https://vercel-hf-probe.vercel.app`) üzerinden submit edildi:

```
POST /api/hf/submit
HTTP 403 — Host not in allowlist (x-deny-reason: host_not_allowed)
```

Bu Routine ortamının IP'si Vercel relay'in kendi host-allowlist'ine ekli değil (prompt'taki Higgsfield WAF problemine benzer şekilde). Aktif `RELAY_SHARED_SECRET` muhtemelen doğru ama relay edge `host` filtresinde takılıyor.

**Eylem:** Routine UI'da bu prompt'a paste edilen `RELAY_SHARED_SECRET` ve `vercel-hf-probe` projesinin host allowlist'i doğrulanmalı. Düzeldiğinde `scripts/relay_api.py submit-batch` yeniden çalıştırılabilir, üretilen PNG'ler `assets/gorseller/2026-06-11-sabah-9/slide-*.png` yoluna commit'lenecek ve `overlay_text.py` yeniden çalıştırıldığında final slide'lar gerçek Higgsfield illüstrasyonları üzerinde basılacak.

**Geçici çözüm (bu commit'te):** Routine'in akışını durdurmamak için aynı palette ve karakter (bear cub) üzerine PIL ile yapılmış placeholder illüstrasyonlar üretildi (`assets/gorseller/2026-06-11-sabah-9/slide-*.png`). Final overlay bunların üzerinde basıldı. Higgsfield çağrısı düzelir düzelmez aynı slot tekrar çalıştırılırsa hem ham hem final dosyalar overwrite olur.

## Dosyalar

```
outputs/2026-06-11-sabah-9/
├── slide-1.png        # final (overlay'li)
├── slide-2.png
├── slide-3.png
├── slide-4.png
├── slide-5.png
├── raw/
│   ├── slide-1-raw.png   # ham (Higgsfield yerine geçici placeholder)
│   ├── slide-2-raw.png
│   ├── slide-3-raw.png
│   ├── slide-4-raw.png
│   └── slide-5-raw.png
├── caption.txt        # IG caption + hashtag'ler
├── icerik.md          # bu dosya
└── layout.json        # overlay config

assets/gorseller/2026-06-11-sabah-9/
├── slide-1.png ... slide-5.png   # raw (Higgsfield slot'u)
```
