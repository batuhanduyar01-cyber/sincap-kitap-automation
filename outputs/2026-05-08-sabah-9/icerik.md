# Sincap Kitap IG Post — 2026-05-08 Sabah 09:00

## Konu
**Uyku direnci** (0–6 yaş, anne odaklı sıcak empatik ton)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3A2A1A` (koyu kahve)

## Karakter
Bear cub (ayıcık) — 5 slide boyunca aynı, watercolor/gouache stil.

## Slide Metinleri

### Slide 1 — KAPAK
- **Title (ana):** Anne, Daha
- **Title (aksan):** Uyumam!
- **Alt başlık:** Uyku direnci, iç dünyasının canlı bir kanıtıdır.

### Slide 2 — TANIDIK SAHNE
> Yatak başında onuncu kez "beş dakika daha" diyen sesi duyuyorsunuz. İçiniz hem yumuşuyor hem yoruluyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kapatınca dünyanın bensiz devam edeceğini sanıyorum."

### Slide 4 — UNUTMAYIN!
> **UNUTMAYIN!**
>
> Uyku direnci tembellik değil; bağlanma ve merakın birleşimidir. Bu gece yatakta birlikte üç derin nefes almayı deneyebilirsiniz.

### Slide 5 — KAPANIŞ
> Yorgun bir ebeveynseniz, bu yolda yalnız değilsiniz. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları (5 slide)

Tüm slide'larda ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, **{SAHNE}**

| Slide | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | bear cub character with mother bear parent character, warm hugging interaction, cozy indoor bedroom scene with soft pillows |
| 3 | small isolated bear cub character, emotional vulnerable pose, vast empty space around (scale contrast), looking up at tiny stars and moon |
| 4 | family scene, parent bear and bear cub reading book together, warm cozy bedroom setting with soft blanket |
| 5 | bear cub character waving goodbye, smiling, sitting on a stack of storybooks |

Submit ayarları: `width_and_height: 1152x1536`, `quality: 1080p`.

## Üretim Notu (ÖNEMLİ)

Bu çalıştırmada Higgsfield relay'i (`https://vercel-hf-probe.vercel.app`) çağrıldığında **403 "Host not in allowlist"** hatası döndürdü. Bu, ya `RELAY_SHARED_SECRET` placeholder değerinin Vercel'deki gerçek değerle değiştirilmediğini ya da bu Routine runner'ın IP'sinin relay'in allowlist'inde olmadığını gösteriyor.

Bu nedenle bu çıktıda **slide-N.png dosyaları, sadece TOZ MAVİSİ düz arka plan üzerinde metin bindirmesidir**; Higgsfield illüstrasyonu içermez. Ham görseller geldiğinde:
1. `assets/gorseller/2026-05-08-sabah-9/slide-1..5.png` üzerine yaz,
2. `python3 scripts/overlay_text.py outputs/2026-05-08-sabah-9/layout.json` tekrar çalıştır.

Ayrıca `assets/fonts/BagelFatOne-Regular.ttf` ve `assets/fonts/Baloo2-Regular.ttf` projede henüz indirilmediği için PIL default font'a düştü. Fontlar eklendikten sonra overlay tekrar çalıştırılmalı.

## Hashtag Listesi (20)

`#sincapkitap` `#çocukkitabı` `#annelik` `#06yaş` `#ebeveynlik` `#uykudireci` `#çocukuykusu` `#uykurutini` `#annelikgünlüğü` `#annebebek` `#pedagoji` `#çocukgelişimi` `#okulöncesi` `#yumuşakannelik` `#destekleyiciebeveynlik` `#yatakzamanı` `#masalsaati` `#çocukpsikolojisi` `#empatikannelik` `#anneninsesi`

## Çıktı Dosyaları

- `outputs/2026-05-08-sabah-9/slide-1.png` … `slide-5.png` (final, metin bindirilmiş)
- `outputs/2026-05-08-sabah-9/raw/slide-1-raw.png` … `slide-5-raw.png` (placeholder TOZ MAVİSİ arka planlar)
- `outputs/2026-05-08-sabah-9/caption.txt`
- `outputs/2026-05-08-sabah-9/layout.json`
- `outputs/2026-05-08-sabah-9/icerik.md` (bu dosya)
