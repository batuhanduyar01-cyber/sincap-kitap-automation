# Sincap Kitap IG — 2026-04-29 Öğle 12:00

## Konu
**oyuncak paylaşmama** (0-6 yaş çocuğun "bu benim!" dönemi, paylaşma direnci)

## Palette: HARDAL
- Arka plan (bg): `#F5C82E` (hardal sarı)
- Aksan (accent): `#8E4FAA` (mor)
- Metin (text): `#3D2817` (koyu kahve)

## Karakter
Tilki yavrusu (little fox cub) — turuncu-pas tüylü, beyaz karınlı, büyük parlak gözlü, pembe yanaklı. 5 slide boyunca aynı.

## 5 Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Bu Oyuncak
- **Başlık (aksan):** Benim!
- **Alt başlık:** Paylaşmak öğrenilen bir maceradır.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Oyuncağımı seviyorum, tıpkı seni sevdiğim gibi. İkimize de yetecek kadar var."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Benimle hep oynayacaksan, sıkı sıkı tutmam gerekmez."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**

Çocuğunuz güvende hissettikçe paylaşır. Önce "senin" hakkını tanıyın, sonra sırayla deneyin. Bugün: "Şu zil çalana kadar senin" deyin.

### Slide 5 — KAPANIŞ
> "Bir gün dünyayı paylaşmak en sevdiğim oyun olacak. Sincap Kitap'ı takip et 🐿️"

## Higgsfield Prompt'lar (5 slide, aynı karakter + palette)

**Ortak iskelet:**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute little fox cub character with orange-rust fur and white belly, large expressive shiny eyes, rosy blush cheeks, warm painterly palette, solid #F5C82E mustard yellow background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, ...

- **Slide 1:** fox cub hugging a small plush teddy bear protectively against its chest with a playful possessive smile, dynamic expressive pose, 6-8 decorative elements floating around (purple stars, soft bubbles, tiny leaves, sparkles)
- **Slide 2:** fox cub and a friendly bunny character sitting close together on the ground sharing wooden toy blocks, warm loving giggling interaction, both smiling with rosy cheeks, soft cozy atmosphere
- **Slide 3:** small isolated fox cub holding a single tiny toy tightly to its chest, small scale against vast empty mustard yellow background, vulnerable emotional pose with worried eyes, lots of negative space around character
- **Slide 4:** calm cozy bonding scene of an adult parent fox sitting next to fox cub on a soft cushion, both looking at a wooden toy together, warm gentle interaction, quiet bedroom feel
- **Slide 5:** fox cub waving goodbye with one paw raised, cheerful big smile, standing next to a small stack of three storybooks, joyful farewell pose

## Notlar — Routine Çalışması (2026-04-29)

Bu çalıştırmada Higgsfield görsel üretim adımı tamamlanamadı: Routine sandbox'unun outbound proxy allowlist'i `vercel-hf-probe.vercel.app` host'unu reddediyor (HTTP 403, header: `x-deny-reason: host_not_allowed`). Aynı engel `platform.higgsfield.ai` ve `api.github.com` için de geçerli. Görseller geldiğinde overlay adımı tek komutla tamamlanabilir:

```bash
python3 scripts/overlay_text.py outputs/2026-04-29-ogle-12/layout.json
```
