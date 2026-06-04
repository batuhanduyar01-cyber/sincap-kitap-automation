# Sincap Kitap IG — 2026-06-04 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3D2817` (koyu kahve)

## Karakter
**bear cub** (5 slide boyunca aynı)

## Slide Metinleri

### Slide 1 — Kapak
- **Başlık (ana):** Anne, Daha
- **Başlık (aksan):** Uyumam!
- **Alt başlık:** Uyku direnci, bağlanmanın sessiz dilidir.

### Slide 2 — Tanıdık Sahne
> Saat geç oldu, gözleri ağırlaşmış ama yatağa girmek istemiyor. Beşinci kez su, altıncı kez sarılmak istiyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun Sesi
> "Gözlerimi kapatınca seni bir daha göremem sanıyorum."

### Slide 4 — UNUTMAYIN!
**Başlık:** UNUTMAYIN!

> Uyku direnci, çocuğun günü size 'daha bitirmedim' demesidir. Sabit bir uyku ritüeli, güvenli bir köprü kurar. Bugün: aynı saatte, aynı kitap, aynı şarkıyla uğurlayabilirsiniz.

### Slide 5 — Kapanış / CTA
> İyi geceler masallarıyla yola çıkmak için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt İskeleti

```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

### Slide sahneleri
1. big bear cub character standing on a small hill at twilight, decorative stars and tiny clouds around, holding a soft pillow, looking sleepy but hopeful
2. bear cub with mother bear, warm hugging interaction at bedtime, cozy indoor scene with a small lamp and a blanket
3. small isolated bear cub in pajamas, emotional vulnerable pose under a vast starry sky (scale contrast), looking up with shiny eyes
4. family scene, mother bear and bear cub reading a bedtime book together, warm cozy bedroom setting with soft pillows and a tiny nightlight
5. bear cub waving goodbye, smiling softly, sitting on a stack of bedtime story books with a tiny crescent moon nearby

## Notlar (bu çalıştırmada)

- **ADIM 4 (Higgsfield) başarısız oldu.** Routine ortamının çıkış (egress) allowlist'i `vercel-hf-probe.vercel.app` host'una izin vermiyor; relay'e yapılan istek `HTTP 403 "Host not in allowlist"` döndü. Görsellerin yerine TOZ MAVİSİ düz renk placeholder'lar kullanıldı.
- **Fontlar eksik.** `assets/fonts/BagelFatOne-Regular.ttf` ve `assets/fonts/Baloo2-Regular.ttf` repo'da yok; overlay scripti PIL default fontuna düştü. Final slide'lardaki yazılar ince/küçük görünecek. Düzeltmek için `assets/fonts/README.md`'deki komutlarla iki TTF eklenmeli.
- Tekrar üretmek için: Vercel host'unu allowlist'e ekledikten sonra `python3 scripts/relay_api.py submit-batch --slot 2026-06-04-sabah-9 --branch claude/quirky-mendel-mDf3v --prompts-file /tmp/prompts.json` çalıştırılabilir; sonrasında `python3 scripts/overlay_text.py outputs/2026-06-04-sabah-9/layout.json` yeniden render eder.
