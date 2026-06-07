# Sincap Kitap IG — 2026-06-07 Sabah 09:00

## Konu
**Kardeş kıskançlığı** — 0-6 yaş çocuklarda yeni kardeşin gelişiyle yaşanan duygusal dengesizlik, "anne sevgisini paylaşmak istememe" sahnesi.

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
**Bear cub** (ayı yavrusu) — 5 slide boyunca sabit. Sıcak duygu temasına uygun, kucaklanası bir karakter.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** "Onu Sevmiyorum"
- **Başlık (aksan):** "Diyor!"
- **Alt başlık:** "Kardeş kıskançlığı, sevginin yer arama çabasıdır."

### Slide 2 — TANIDIK SAHNE
> Bebek ağladığında abisinin gözleri buğulanıyor. Oyuncağı fırlatıyor, sana sırtını dönüyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> Eskiden sadece benimdin. Şimdi paylaşmak çok zor.

### Slide 4 — UNUTMAYIN
- **Başlık:** UNUTMAYIN!
- **Gövde:** Kıskançlık, sevginin yer arayışıdır. Günde 10 dakikalık 'sadece bizim olan' bir zaman yaratın. Adını koyun: "Bu bizim özel anımız." Telefon yok, kardeş yok.

### Slide 5 — KAPANIŞ
> Her çocuk, kalbinde kendine ait bir yer ister. Onu görmek, dengeyi geri getirir. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar

Her slide için temel iskelet (palette ve karakter sabit):

> Children's book illustration, watercolor gouache painting, textured brush strokes, cute **bear cub** character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid **#E63B5C** background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, **{SAHNE}**

Sahneler:
1. big character standing on a small hill, decorative leaves and stars around, looking hopeful
2. bear cub character with mother bear, warm hugging interaction, cozy indoor scene, a tiny baby bear sibling beside them
3. small isolated bear cub, emotional vulnerable pose, vast empty space around, scale contrast, looking up with teary big eyes
4. family bear scene, mother bear and bear cub reading a storybook together on a cozy bed, warm bedroom setting, baby bear sibling sleeping nearby
5. bear cub waving goodbye, smiling, sitting on a stack of books

Tam JSON: `outputs/2026-06-07-sabah-9/higgsfield-prompts.json`

## Üretim Notu

**Higgsfield görselleri bu çalıştırmada üretilemedi.** Sandbox ağ politikası `vercel-hf-probe.vercel.app` ve `*.higgsfield.ai` adreslerini outbound proxy seviyesinde reddediyor (`HTTP 403 x-deny-reason: host_not_allowed`). Bu, Routine yürütme ortamının izinli host listesine bu domain'lerin eklenmesi gerektiği anlamına geliyor.

Şimdilik `assets/gorseller/2026-06-07-sabah-9/slide-*.png` ve `outputs/.../raw/slide-*-raw.png` dosyaları solid AHUDUDU (#E63B5C) **placeholder**'larıdır. Overlay script bunların üzerine metni başarıyla bindirdi — yerleşim ve metin akışı kontrolüne uygun ancak nihai estetik için Higgsfield watercolor görselleriyle yeniden üretilmesi gerekiyor.

**Düzeltmek için:**
1. Routine ortamının network allowlist'ine `vercel-hf-probe.vercel.app` eklenir.
2. Bu routine yeniden çalıştırılır — `scripts/relay_api.py` aynı slot'a (`2026-06-07-sabah-9`) görselleri commit'ler.
3. `python3 scripts/overlay_text.py outputs/2026-06-07-sabah-9/layout.json` ile final slide'lar yeniden render edilir.

**Ek not:** `assets/fonts/BagelFatOne-Regular.ttf` ve `Baloo2-Regular.ttf` da repo'da yok (`KALAN-ISLER.md` Madde 3 hâlâ açık). Overlay PIL default fontuna düştü — fontlar eklendikten sonra yeniden render edilince başlıklar tasarlanan ağırlığında görünecek.
