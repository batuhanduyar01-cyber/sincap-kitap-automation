# Sincap Kitap IG — 2026-06-01 Sabah 09:00

## Konu
**Uyku Direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ** — sakinlik / uyku temasıyla uyumlu.
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3B2A1F` (koyu kahve)

## Karakter
**Bear cub** — yumuşak pijamalı küçük ayı yavrusu. 5 slide boyunca sabit.

---

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık ana:** Uykuya Bir Türlü
- **Başlık aksan:** Geçemiyor
- **Alt başlık:** Uyku direnci, geçici bir gelişim eşiğidir.
- **Dekorasyon:** Açık (yıldız, ay, nokta)

### Slide 2 — TANIDIK SAHNE
> Saat geç oldu, lambalar kısıldı ama o hâlâ ayakta. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "Gözlerimi kapatınca gün bitiyor, ben daha doymadım."

### Slide 4 — UNUTMAYIN!
**UNUTMAYIN!**
Uyku direnci inat değil, gevşeyememektir. Sabit bir akış güven verir. Bu akşam: ışıkları kıs, sesi yumuşat, son 20 dakikayı kucağında bir kitapla geçir.

### Slide 5 — KAPANIŞ
> Uykuya yumuşak bir geçiş için yanında olalım. Sincap Kitap'ı takip et 🐿️

---

## Higgsfield Prompt'lar

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character in soft pajamas, large expressive eyes, rosy blush cheeks,
warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc
Boutavant style, storybook art, no text, no frames, no borders, soft painterly
shading, portrait orientation, {SAHNE}
```

| # | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill of pillows, decorative moons stars and crescents around, looking hopeful and a little tired |
| 2 | bear cub character with mother bear, warm hugging interaction at bedtime, cozy indoor bedroom scene with soft blanket |
| 3 | small isolated bear cub character sitting alone on a big bed, emotional vulnerable pose, vast empty space around with scale contrast, looking up at the ceiling |
| 4 | family scene with parent bear and bear cub reading a bedtime book together, warm cozy bedroom setting with soft lamp glow |
| 5 | bear cub character waving goodnight, smiling, sitting on a stack of storybooks |

Çözünürlük: `1152x1536`, quality `1080p`.

---

## Üretim Notu — Bu Çalıştırma

Higgsfield relay'i (`https://vercel-hf-probe.vercel.app`) bu container'ın egress IP'sini
allowlist'te tutmadığı için `submit` çağrısı `HTTP 403 "Host not in allowlist"`
döndürdü. `prompts.json` ve `layout.json` aşağıdaki yapıda hazırlandı; relay'e
yetkili bir runner üzerinden tekrar gönderildiğinde (veya allowlist güncellendiğinde)
5 PNG `assets/gorseller/2026-06-01-sabah-9/slide-{1..5}.png` yoluna düşecek ve
`scripts/overlay_text.py outputs/2026-06-01-sabah-9/layout.json` final slide'ları
üretecektir.

Ön izleme amacıyla, ham görseller yokluğunda overlay scripti TOZ MAVİSİ düz
arka plan üzerine çalıştırılarak `slide-1.png … slide-5.png` üretildi (kompozisyon,
tipografi ve metin akışı bu önizleme üzerinden doğrulanabilir).
