# Sincap Kitap IG — 2026-05-28 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
Yavru ayı (bear cub) — 5 slide'da sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** O Çığlık Aslında
- **Başlık (aksan):** Bir Çağrı
- **Alt başlık:** Öfke nöbetleri, kelimelerin yetmediği yerdedir.

### Slide 2 — TANIDIK SAHNE
> Markette tüm gözler size dönüyor. Çocuğunuz yere yatmış, ağlıyor. Siz de çaresizce nefes alıyorsunuz. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "İçimde kocaman bir fırtına var, ama nasıl söyleyeceğimi bilmiyorum."

### Slide 4 — UNUTMAYIN!
> Öfke nöbetleri gelişimin doğal bir parçası. Çocuğunuz size kötülük yapmıyor; sadece duygularının büyüklüğünden ürküyor. Bugün: Onun yanına çömelip "Buradayım, hazır olunca kucağıma gel," diyebilirsiniz.

### Slide 5 — KAPANIŞ
> Her fırtına geçer; senin sakin sevgin onun limanı oluyor. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts (watercolor gouache, AHUDUDU bg)

Ortak başlangıç:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #E63B5C raspberry background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation,

Slide-spesifik sahneler:
1. big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful and gentle
2. bear cub with mother bear character, warm hugging interaction, cozy indoor scene, soft golden light
3. small isolated bear cub, emotional vulnerable pose, vast empty space around (scale contrast), looking up with tear in eye
4. family scene, mother bear and bear cub reading a picture book together, warm cozy bedroom setting at evening
5. bear cub waving goodbye, smiling brightly, sitting on a small stack of books

## Görsel Üretim Notu

Bu çalıştırmada Vercel relay (`https://vercel-hf-probe.vercel.app/api/hf/submit`) **HTTP 403 "Host not in allowlist"** döndürdü; Higgsfield görselleri üretilemedi. `/tmp/prompts.json` hazır, layout hazır — relay allowlist'i düzeltildikten sonra şu komutla yeniden çalışılabilir:

```bash
SLOT="2026-05-28-sabah-9"
BRANCH="claude/quirky-mendel-nJpbm"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-28-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-28-sabah-9/layout.json
```
