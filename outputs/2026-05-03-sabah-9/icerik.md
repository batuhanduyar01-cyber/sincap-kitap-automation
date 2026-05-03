# Sincap Kitap IG — 2026-05-03 Sabah 09:00

## Konu
**uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4B2E1A` (koyu kahve)

## Karakter
bear cub (yavru ayı) — 5 slide boyunca sabit

## Carousel Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Anne, Daha
- **Başlık (aksan):** Uyumayacağım!
- **Alt başlık:** Uyku direnci, küçük bir korkunun şifresidir.

### Slide 2 — TANIDIK SAHNE
> Saat 22:00. "Bir su daha." "Bir kitap daha." Yorgun bedenin küçük gözlerin direncine yenildiğini hissediyorsun. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kapattığımda dünya kayboluyor; ben de kaybolacağım sanıyorum."

### Slide 4 — UNUTMAYIN!
> Uykuya direnç inat değil; ayrılık ve kontrolü kaybetme korkusudur. Sabit bir rutin (banyo–kitap–ışık) bu korkuyu yumuşatır.
>
> **Bugün:** yatmadan önce "hangi şarkıyla uyumak istersin?" diye küçük bir seçim hakkı verin.

### Slide 5 — KAPANIŞ
> İyi geceler hikâyeleri için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (5 slide)

Tüm prompt'lar `higgsfield-prompts.json` dosyasında.

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

| # | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful, holding a tiny pillow |
| 2 | bear cub with mother bear character, warm hugging interaction, cozy bedroom scene at night, soft moonlight |
| 3 | small isolated bear cub character on a big bed, emotional vulnerable pose, vast empty space around, looking up at the dark window with stars |
| 4 | family scene, mother bear and bear cub reading a bedtime book together, warm cozy bedroom setting, warm bedside lamp glow |
| 5 | bear cub waving goodbye, smiling sleepily, sitting on a stack of bedtime books, holding a small star |

## ⚠️ ÜRETİM DURUMU — DİKKAT

**Higgsfield görselleri üretilemedi.** Vercel relay (`https://vercel-hf-probe.vercel.app`) bu Claude Code ortamının IP'sini reddediyor:

```
HTTP/2 403
x-deny-reason: host_not_allowed
content-length: 21
content-type: text/plain
```

Sebep: routine prompt'undaki `RELAY_SHARED_SECRET` placeholder (`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`) gerçek değerle değiştirilmedi VE/VEYA bu IP relay'in allowlist'inde yok. Relay yalnızca whitelisted Routine runner IP'lerini kabul ediyor.

Bu çıktıdaki `slide-*.png` dosyaları **placeholder**'dır (#C9DDEC düz renk üstüne overlay metin). Yayına göndermeden önce:

1. Relay'i whitelisted bir ortamdan tekrar tetikle, VEYA
2. `higgsfield-prompts.json`'u manuel olarak Higgsfield UI'ye yapıştır, üretilen 5 PNG'yi `assets/gorseller/2026-05-03-sabah-9/slide-{1..5}.png` yolun*a indir, sonra:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-05-03-sabah-9/layout.json
   ```
   komutunu yeniden çalıştır.

## Notlar
- `assets/fonts/BagelFatOne-Regular.ttf` ve `Baloo2-Regular.ttf` repoda yok; PIL default font'a düştü. Final üretimden önce font dosyalarını eklemek gerekli.
