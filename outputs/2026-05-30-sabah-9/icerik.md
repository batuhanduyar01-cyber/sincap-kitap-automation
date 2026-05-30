# Sincap Kitap IG — 2026-05-30 Sabah 09:00

## Konu
**Karanlık korkusu** (2-6 yaş arası gelişimsel bir aşama olarak)

## Palette
**MOR** — Arka plan `#7E5BA0`, Aksan `#C5E86C` (yeşil), Metin `#FFFFFF` (beyaz)

> Korkular / ayrılık kaygısı temaları için mor kullanılmıştır.

## Karakter
**Bear cub (ayı yavrusu)** — 5 slide boyunca sabit; sıcak, sarılınası bir karakter karanlık temasını yumuşatmak için seçildi.

## Slide Metinleri

### Slide 1 — Kapak
- **Başlık (ana):** "Anne, Işığı"
- **Aksan kelime:** "Açık Bırak!"
- **Alt başlık:** "Karanlık korkusu, hayal gücünün ilk işaretidir."

### Slide 2 — Tanıdık sahne
> Işıkları kapatınca minik elini sıkıca tutuyor. Yatağın altına bakıyor, dolaba bir kez daha göz atıyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun sesi
> "Karanlık olunca odam çok büyüyor anne, ben küçücük kalıyorum."

### Slide 4 — UNUTMAYIN
> Karanlık korkusu, 2-6 yaş arası hayal gücünün geliştiğinin sağlıklı bir işaretidir. Korkuyu küçümsemeden adlandırmak, çocuğu güvende hissettirir. **Bugün:** yatmadan önce odayı birlikte gezin, "gölgeye merhaba" deyin.

### Slide 5 — Kapanış
> Bu süreçte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Promptları

Stil iskeleti her slide için ortak:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, **solid #7E5BA0 background**, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, **{SAHNE}**

| Slide | SAHNE |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful, holding a small glowing lantern |
| 2 | bear cub character with mother bear parent character, warm hugging interaction, cozy indoor bedroom scene at night with a soft nightlight |
| 3 | small isolated bear cub character clutching a blanket, emotional vulnerable pose, vast empty dark space around with tiny stars (scale contrast), looking up wide-eyed |
| 4 | family scene, mother bear and bear cub reading a picture book together under a warm bedside lamp, cozy bedroom setting with pillows |
| 5 | bear cub character waving goodbye, smiling, sitting on a stack of storybooks with a small crescent moon nearby |

Tam JSON: `prompts.json`

## Çıktı Dosyaları

- `slide-1.png` … `slide-5.png` — final metin bindirilmiş
- `raw/slide-1-raw.png` … `slide-5-raw.png` — ham görseller
- `caption.txt` — Instagram caption + hashtag'ler
- `layout.json` — overlay_text.py için kullanılan config
- `prompts.json` — Higgsfield batch promptları
