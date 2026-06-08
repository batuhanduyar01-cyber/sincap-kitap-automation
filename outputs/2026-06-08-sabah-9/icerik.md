# Sincap Kitap IG — 2026-06-08 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
Kitten (yavru kedi) — 5 slide boyunca aynı.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık ana: **Çocuğum Yine**
- Başlık aksan: **Patladı!**
- Alt başlık: Öfke nöbeti, kontrol değil; duygu dilidir.

### Slide 2 — TANIDIK SAHNE
> Markette mavi bardak yüzünden yere yatıyor. Çevredeki bakışlar üzerinizde. İçiniz hem sıkışıyor hem eriyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "İçimde kocaman bir fırtına var, ama nasıl söyleyeceğimi bilmiyorum."

### Slide 4 — UNUTMAYIN!
> Öfke, küçük bir beynin büyük duygularla baş etme çabasıdır. Yargılamadan yanında kalmak, en güçlü tampondur. Bugün: "Çok kızdın, anlıyorum. Buradayım." deyip sessizce yanına oturun.

### Slide 5 — KAPANIŞ
> Duyguları anlamayı kolaylaştıran kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar

Ortak iskelet — `solid #E63B5C background`, `cute kitten character`, watercolor gouache, Oliver Jeffers + Marc Boutavant stil, portrait 1152x1536.

- **Slide 1:** big character standing on a small hill, decorative leaves and stars around, looking hopeful
- **Slide 2:** character with mother cat character, warm hugging interaction, cozy indoor scene
- **Slide 3:** small isolated kitten character, emotional vulnerable pose, vast empty space around with scale contrast, looking up
- **Slide 4:** family scene, mother cat and kitten reading book together, warm cozy bedroom setting
- **Slide 5:** kitten character waving goodbye, smiling, sitting on a book stack

Prompt'ların tam hali: `/tmp/prompts.json` (commit'lenmedi — repo köküne taşınmak istenirse `outputs/.../prompts.json`).

## Durum

**ADIM 1-3 (konu/metin/palette):** ✅ Tamamlandı, bu dosyada yazılı.
**ADIM 4 (Higgsfield görselleri):** ❌ Blocker — Vercel relay `https://vercel-hf-probe.vercel.app` host allowlist'i bu Routine runner'ın IP'sini reddediyor. Detay: `RAPOR.md`.
**ADIM 5 (overlay):** ❌ ADIM 4 bitmediği için çalıştırılamadı. Ek olarak fontlar (`BagelFatOne-Regular.ttf`, `Baloo2-Regular.ttf`) repo'da eksik — KALAN-ISLER.md'de belirtilmiş.
**ADIM 6 (commit/push):** ✅ Bu klasör branch'e push'lanıyor.
