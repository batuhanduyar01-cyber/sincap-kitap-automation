# Sincap Kitap IG — 2026-05-15 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3E2723` (koyu kahve)

## Karakter
**bear cub** (ayı yavrusu) — 5 slide boyunca tutarlı

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Anne, Daha
- **title_accent:** Uyumak İstemiyorum
- **subtitle:** Uyku direnci, ayrılığa karşı bir çağrıdır.

### Slide 2 — TANIDIK SAHNE
> Saat geç oldu, gözlerinde uyku var ama "beş dakika daha" diyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "Karanlık olunca tek başıma kalıyorum, hâlâ seninle olmak istiyorum."

### Slide 4 — UNUTMAYIN!
**UNUTMAYIN!**
Uyku direnci, günden ayrılma kaygısıdır. Sakin bir rutin, sıcak bir kucak ve birlikte bir kitap, uykuya yumuşak bir köprü kurar. Bu akşam: Yatağa 10 dk önce girip kucağında kitap okumayı deneyin.

### Slide 5 — KAPANIŞ
> Yorgun günler geçici, kucağında okuduğun anılar kalıcı. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts

Tüm slide'lar için ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid `#C9DDEC` background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}

Sahneler:

1. **Slide 1:** big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful, wearing a tiny soft pajama
2. **Slide 2:** bear cub character with mother bear, warm hugging interaction, cozy bedroom scene with a soft blanket and pillow
3. **Slide 3:** small isolated bear cub in pajamas, emotional vulnerable pose sitting on a bed, vast empty space around with a few quiet stars (scale contrast), looking up
4. **Slide 4:** family scene, mother bear and bear cub reading a book together, warm cozy bedroom setting with a soft bedside lamp glow
5. **Slide 5:** bear cub waving goodnight, smiling sleepily, sitting on a small stack of books with a tiny crescent moon nearby

Boyut: `1152x1536`, kalite: `1080p`

`/tmp/prompts.json` dosyası repo'da `outputs/2026-05-15-sabah-9/prompts.json` olarak kaydedildi.

## Üretim Durumu

❌ **Higgsfield görselleri üretilemedi.** Relay submit denemesi `HTTP 403 "Host not in allowlist"` döndürdü çünkü routine prompt'undaki `RELAY_SHARED_SECRET` placeholder değer (`78e1e7...`) olarak kalmış — Vercel dashboard'undaki gerçek değerle değiştirilmemiş.

### Çözüldükten sonra çalıştırılacak adımlar

```bash
# 1) Görselleri üret (gerçek secret ile)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "2026-05-15-sabah-9" \
    --branch "claude/quirky-mendel-EvCcn" \
    --prompts-file outputs/2026-05-15-sabah-9/prompts.json

# 2) Webhook commit'lerini çek
git pull --ff-only origin claude/quirky-mendel-EvCcn

# 3) Metni bindir
python3 scripts/overlay_text.py outputs/2026-05-15-sabah-9/layout.json
```

## Hashtag'ler (caption.txt içinde)
#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #uykudirenci #çocukuykusu #yatmasaati #annelikyolculuğu #annelikhayatı #pedagoji #çocukgelişimi #birliktebüyüyoruz #masalkitabı #okumasaati #annevecocuk #ebeveynolmak #anneolmak #çocuklaiçinkitap #annelikhali #sevgivesabir
