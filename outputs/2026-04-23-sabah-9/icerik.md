# Sincap Kitap IG — 2026-04-23 Sabah 09:00

## Konu
**Uyku Direnci** (0-6 yaş çocuklarda yatma vakti direnci, uykuya geçişte zorluk)

## Palette
**TOZ MAVİSİ** — sakinlik, uyku teması
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu, sıcak vurgu)
- Metin: `#4A2E1A` (koyu kahve)

## Karakter
**Bear cub** (ayı yavrusu) — 5 slide boyunca sabit. Sıcak, kucaklanabilir, yatak odası temasına uygun.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık ana:** Anne, Uykum
- **Başlık aksan:** Gelmiyor!
- **Alt başlık:** Uyku direnci, güven ihtiyacının sessiz sesidir.

### Slide 2 — TANIDIK SAHNE
> Pijaması giyili, dişi fırçalı. Ama gözleri bambaşka bir yerde. "Bir dakika daha"nın sonu gelmiyor. Tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerim kapanınca seni kaybedecek gibi hissediyorum."

### Slide 4 — UNUTMAYIN!
Uyku direnci inatlaşma değil, güvensizlik sinyalidir. Tutarlı ritüeller sakinleşmeyi öğretir. **Bugün:** yatmadan önce 10 dakikalık "kitap zamanı" deneyin.

### Slide 5 — KAPANIŞ
> Sakin uykular mümkün. Bu yolculukta yanında olacak kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts (5 slide)

**Ortak iskelet:**
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly
palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading, portrait
orientation, {SAHNE}
```

**Sahneler:**
1. big bear cub standing on a small hill at night, decorative stars and little clouds around, looking hopeful, soft moonlight
2. bear cub with mother bear, warm hugging interaction, cozy bedroom scene with pillow
3. small isolated bear cub in pajamas, emotional vulnerable pose, vast empty room around (scale contrast), looking up with wide eyes
4. bear cub family scene, parent bear and cub reading book together on bed, warm cozy bedroom setting, lamp glow
5. bear cub waving goodbye, smiling softly, sitting on a stack of storybooks

## Kullanılan Script'ler
- `scripts/higgsfield_api.py` — 5 ham görsel
- `scripts/overlay_text.py layout.json` — metin bindirme + logo

## Notlar
- 5 slide AYNI TOZ MAVİSİ paletinde
- Aksan rengi (turuncu) sadece başlık "Gelmiyor!" ve UNUTMAYIN! başlığında
- Dekorasyonlar yalnızca kapakta (stars + dots)
- Logo sol altta, 140px yükseklik
- Tasarımda ok/slide numarası/slide noktası YOK
