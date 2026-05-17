# Sincap Kitap IG — 2026-05-17 Sabah 09:00

## Konu

**Karanlık korkusu** (0-6 yaş)
Ton: anne odaklı, sıcak, empatik, yargısız.

## Palette

**MOR**

| Rol | Renk |
|---|---|
| Arka plan | `#7E5BA0` |
| Aksan | `#C5E86C` (yeşil) |
| Metin | `#FFFFFF` (beyaz) |

Eşleştirme gerekçesi: korkular/kaygı temalı konular → MOR.

## Karakter

Baby squirrel (yavru sincap) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK (cover)
- Başlık (ana): **Anne, Karanlık**
- Başlık (aksan): **Beni Korkutuyor**
- Alt başlık: Bu korku, hayal gücünün büyüdüğünün işareti.

### Slide 2 — TANIDIK SAHNE (inner)
Yatma vakti gelince minik eller yorganı sıkıca tutuyor; 'ışık açık kalsın' diye yalvaran o gözler... Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (quote)
"Gözlerimi kapatınca odam kocaman ve sessiz oluyor; yanımda olduğunu bilmek beni rahatlatıyor."

### Slide 4 — UNUTMAYIN (tip)
- Başlık: **UNUTMAYIN!**
- Metin: Karanlık korkusu gelişimin doğal bir parçası; küçümsemeden, sakin varlığınızla güven verebilirsiniz. Bugün: yatmadan önce odayı birlikte gezip her köşeye 'iyi geceler' diyebilirsiniz.

### Slide 5 — KAPANIŞ (cta)
Her gece biraz daha cesaret büyüyor; siz yanındayken karanlık o kadar da büyük değil. Bu yolculukta sana eşlik edecek kitaplar için Sincap Kitap'ı takip et. 🐿️

## Higgsfield Görsel Prompt'ları

Karakter: baby squirrel · Palette HEX: `#7E5BA0` · 1152x1536 · 1080p

| Slide | Sahne |
|---|---|
| 1 | big character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | character with mother squirrel parent character, warm hugging interaction, cozy indoor scene at bedtime |
| 3 | small isolated character, emotional vulnerable pose, vast empty dark space around with scale contrast, looking up |
| 4 | family scene, parent and child squirrel reading book together, warm cozy bedroom setting with soft night light |
| 5 | character waving goodbye, smiling, sitting on a book stack |

Ortak iskelet (her slide): `Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #7E5BA0 background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

Tam prompt JSON: `outputs/2026-05-17-sabah-9/prompts.json`

## Görsel Üretim Notu

> **ADIM 4 (Higgsfield görselleri) bu çalıştırmada tamamlanamadı.**
> Vercel relay'i (`https://vercel-hf-probe.vercel.app`) bu çalışma ortamının
> ağ allowlist'inde olmadığı için egress proxy tarafından bloklandı
> (`HTTP 403 — Host not in allowlist`). `relay_api.py submit-batch` exit 3 ile
> döndü. Slide'lar bu nedenle düz MOR (`#7E5BA0`) arka plan üzerine
> metin + logo bindirilerek üretildi (watercolor sincap illüstrasyonu yok).
>
> Düzeltme için relay alan adı ortamın ağ politikası allowlist'ine eklenmeli;
> ardından `assets/gorseller/2026-05-17-sabah-9/slide-*.png` ham görsellerle
> değiştirilip `python3 scripts/overlay_text.py layout.json` yeniden
> çalıştırılabilir.

## Çıktı Dosyaları

- `outputs/2026-05-17-sabah-9/slide-1.png` … `slide-5.png` — final slide'lar
- `outputs/2026-05-17-sabah-9/raw/slide-1-raw.png` … `slide-5-raw.png` — ham arka planlar (düz MOR placeholder)
- `outputs/2026-05-17-sabah-9/caption.txt` — Instagram caption + hashtag'ler
- `outputs/2026-05-17-sabah-9/layout.json` — overlay config
- `outputs/2026-05-17-sabah-9/prompts.json` — Higgsfield prompt batch'i
