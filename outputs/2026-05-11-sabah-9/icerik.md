# Sincap Kitap IG — 2026-05-11 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4A2C16` (koyu kahve)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca sabit

## Slide Metinleri

### Slide 1 — KAPAK
- **Title main:** Uyumak
- **Title accent:** İstemiyorum!
- **Subtitle:** Uyku direnci, gelişimin doğal bir parçasıdır.

### Slide 2 — TANIDIK SAHNE
> Saat geç oldu, gözleri kapanıyor ama yatağa girmek istemiyor. Bin türlü oyalanma. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kaparsam güzel anlar bitecek sanıyorum."

### Slide 4 — UNUTMAYIN
- **Title accent:** UNUTMAYIN!
- **Body:** Uyku direnci inattan değil, dünyayı kaçırma korkusundan gelir. Sabit bir rutin, beynin 'şimdi gevşeme zamanı' sinyalini güçlendirir. Bugün: her gece aynı saatte aynı kitabı okumayı deneyin.

### Slide 5 — KAPANIŞ
> Sakin gecelerin sırrı, tanıdık ritimlerde gizli. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (her slide, TEK STRING)

**Slide 1 (kapak — umutlu duruş):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character with soft fluffy fur, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful and a little sleepy

**Slide 2 (tanıdık sahne — anne sarılması):**
> ...bear cub character with mother bear parent character, warm hugging interaction at bedtime, cozy indoor scene with a small lamp

**Slide 3 (alıntı — kırılgan):**
> ...small isolated bear cub character, emotional vulnerable pose holding a tiny blanket, vast empty space around (scale contrast), looking up at the moon

**Slide 4 (ipucu — birlikte okuma):**
> ...family scene with mother bear and bear cub reading a bedtime book together, warm cozy bedroom setting with a small night lamp and pillow

**Slide 5 (kapanış — el sallama):**
> ...bear cub character waving goodbye, smiling sleepily, sitting on a stack of storybooks

## Hashtag'ler
#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #uykudirenci #çocukgelişimi #annelikgünlüğü #uykurutini #çocukpsikolojisi #okulöncesi #annenotları #yatakzamanı #okulöncesieğitim #bebekuykusu #çocukkitapları #annebebek #bilinçliebeveynlik #çocukedebiyatı #pozitifebeveynlik

## Üretim Notu — 2026-05-11

**Higgsfield görselleri üretilemedi.** Vercel relay (`https://vercel-hf-probe.vercel.app`) tüm isteklere `HTTP 403 — Host not in allowlist` döndürüyor (kimliksiz `/` çağrıları dahil). Bu, relay'in kendi IP/host allowlist katmanı; Routine runner IP'si listede değil.

Düzeltme adımları (operatör için):
1. Vercel dashboard → `vercel-hf-probe` projesi → ilgili middleware/edge config'in Host/IP allowlist'ine Anthropic Routine runner aralığını ekle.
2. Bu routine'i yeniden çalıştır; ADIM 4 (submit-batch) bittikten sonra ADIM 5 overlay'i yürütülecek.

`layout.json`, `caption.txt`, `icerik.md` ve `prompts.json` hazır — sadece `assets/gorseller/2026-05-11-sabah-9/slide-{1..5}.png` dosyaları eksik. Görseller commit'lendikten sonra:

```bash
python3 scripts/overlay_text.py outputs/2026-05-11-sabah-9/layout.json
```

komutu son slide'ları üretecek.
