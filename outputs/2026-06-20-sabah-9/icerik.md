# Sincap Kitap IG — 2026-06-20 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**MOR** — Arka plan `#7E5BA0`, Aksan `#C5E86C` (yeşil), Metin `#FFFFFF` (beyaz)

## Karakter
**Bear cub** (ayıcık) — 5 slide boyunca aynı kalır

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Anne, Patlıyorum
- **Başlık (aksan):** Yardım Et!
- **Alt başlık:** Öfke nöbetleri, küçük bir kalbin duygu fırtınasıdır.

### Slide 2 — TANIDIK SAHNE
> Marketin ortasında yere yığılıp ağlıyor. Çevredeki bakışlar üstünüze çevriliyor, içiniz daralıyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Ben de bilmiyorum ne olduğunu... İçimde fırtınalar kopuyor anne."

### Slide 4 — UNUTMAYIN!
> Öfke nöbeti bir terbiye sorunu değil, gelişimin doğal bir evresi. Çocuğunuz duyguları sözle ifade etmeyi henüz öğreniyor. Bugün deneyin: Yere çömelin, sarın ve sadece "Yanındayım" deyin. Açıklama sonra gelir.

### Slide 5 — KAPANIŞ
> Bu fırtınalı günlerde yalnız değilsin. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts

Tüm prompt'larda ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #7E5BA0 background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}

| Slide | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | bear cub character with mother bear parent, warm hugging interaction, cozy indoor scene |
| 3 | small isolated bear cub character, emotional vulnerable pose, vast empty space around for scale contrast, looking up |
| 4 | family scene, mother bear and bear cub reading a book together, warm cozy bedroom setting |
| 5 | bear cub character waving goodbye, smiling, sitting on a stack of books |

Resolution: 1152x1536 / quality 1080p (her slide).

## Caption ilk 3 satırı
> Marketin ortasında yere yığıldığı an... Belki de bu satırları okurken kalbin sıkışıyor.
>
> Çünkü o sahneyi her annenin içinde küçük bir titreme bırakır. Çevredeki bakışlar, "iyi bir anne olamadın mı?" sorusunun gölgesi, kendi içinde bastırmak zorunda kaldığın çaresizlik...
>
> Önce şunu duyman gerekiyor: Yalnız değilsin. Ve çocuğun da yalnız değil.

## Status

**⚠️ GÖRSEL ÜRETİMİ BLOKE — ROUTINE TAMAMLANAMADI**

Vercel relay'e (`https://vercel-hf-probe.vercel.app`) çağrı atıldığında bu ortamın network egress allowlist'i bu host'u reddetti:

```
HTTP 403: Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access.
```

Adımlar 1-3 (konu seçimi, metin üretimi, palette) tamamlandı ve bu klasöre commit'lendi. **Adım 4 (Higgsfield) ve Adım 5 (overlay) çalıştırılamadı.**

### Yapılması Gereken (Kullanıcı)
1. **Routine ortam ayarları** → Network egress allowlist'ine ekle:
   - `vercel-hf-probe.vercel.app`
2. Routine'i yeniden çalıştır. Bu klasördeki `layout.json`, `caption.txt`, `icerik.md` hazır; yalnızca görseller üretilecek.
3. Alternatif olarak `/tmp/prompts.json` formatında üretilen prompt'lar bu repo'da da saklanıyor — manuel re-submit için `outputs/2026-06-20-sabah-9/prompts.json`.
