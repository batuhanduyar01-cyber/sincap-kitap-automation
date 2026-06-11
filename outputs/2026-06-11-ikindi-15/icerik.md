# Sincap Kitap IG — 2026-06-11 İkindi 15:00

## Konu
**Merak** (0-6 yaş gelişim · pedagojik ipucu)

## Palette
**TURUNCU** — gün sonu sıcak hissi
- Arka plan: `#E97E28`
- Aksan: `#FFFFFF` (beyaz)
- Metin: `#2A1810` (koyu kahve / mor)

## Karakter
Baby squirrel (Sincap Kitap maskotu) — 5 slide'da aynı karakter.

## Slide Metinleri

### Slide 1 — KAPAK
- title_main: **Çocuğun Sonsuz**
- title_accent: **Merakı**
- subtitle: *Her 'neden' sorusu, bir keşfin kapısıdır.*

### Slide 2 — ÇERÇEVE
> Çocuğunuz gün boyu sorular soruyor. Bu durmaksızın akan 'neden'ler aslında öğrenmenin en saf hali.

### Slide 3 — ANAHTAR KAVRAM
- Başlık: **Merak**
- Açıklama: *Yeni şeyleri keşfetme isteği; çocuğun zihnini büyüten en güçlü itici güçtür.*

### Slide 4 — UNUTMAYIN!
> Her soru bir öğrenme fırsatıdır. Hemen cevap vermek yerine 'Sen ne düşünüyorsun?' diye sormak, çocuğun düşünme kasını çalıştırır.
>
> **Bu akşam:** bahçede ya da pencere kenarında 3 ilginç şey bulup birlikte adlandırın.

### Slide 5 — KAPANIŞ
> Çocuğunuzun merakını besleyen hikayeler için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Prompts (slide-1 → slide-5)

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute baby squirrel character in rich scene, multiple storybook animal characters,
large expressive eyes, rosy cheeks, warm painterly palette,
solid #E97E28 background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation,
{SAHNE}
```

**Sahneler:**
1. central baby squirrel character holding a magnifying glass, surrounded by floating question marks and 2-3 small side objects (pencil, open book, butterfly), looking up with wide curious eyes, decorative leaves around
2. rich scene with multiple animal characters in a cozy library corner: a bear cub reading a giant book, a hedgehog peeking at a globe, a baby squirrel pointing at illustrated stars on the wall, warm afternoon light through window
3. scene representing curiosity: a small baby squirrel discovering a glowing seashell with stars and tiny galaxies floating out of it, magical sparkles, sense of wonder, painterly storybook style
4. warm parent-child activity scene: a mother squirrel and her child kneeling in a backyard garden examining a snail and a sprouting seed together, watering can nearby, sunlight rays, painterly cozy mood
5. baby squirrel character smiling and waving warmly, sitting on a stack of three small storybooks, holding an acorn, surrounded by floating tiny stars and leaves, cheerful expression

## ⚠️ Üretim Notu
Bu çalıştırmada Vercel relay (`https://vercel-hf-probe.vercel.app`) tüm endpoint'lerde
`HTTP 403 — Host not in allowlist` döndürdü. Higgsfield illustrasyonları üretilemedi;
slide arka planları geçici olarak düz `#E97E28` palette dolgusu ile bindirildi.

Relay erişimi tekrar açıldığında `/tmp/prompts.json` ile aynı SLOT için submit-batch
tekrar koşulup `assets/gorseller/2026-06-11-ikindi-15/slide-*.png` dosyaları
gerçek illüstrasyonlarla güncellenmelidir; ardından `python3 scripts/overlay_text.py
outputs/2026-06-11-ikindi-15/layout.json` tekrar çalıştırılır.
