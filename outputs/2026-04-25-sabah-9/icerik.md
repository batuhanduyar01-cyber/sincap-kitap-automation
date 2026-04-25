# Sincap Kitap IG — 2026-04-25 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3D2817` (koyu kahve)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- **Title main:** Anne, Biraz Daha
- **Title accent:** Uyumayalım!
- **Subtitle:** Uyku direnci, sevginin sessiz çağrısıdır.
- Dekorasyonlar: aktif

### Slide 2 — TANIDIK SAHNE
> Pijamalar giyildi, dişler fırçalandı, ışıklar kısıldı. Ama o küçük gözler hâlâ pırıl pırıl, sizin elinize sıkıca tutunmuş. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Anneciğim, gözlerimi kapatınca dünya bitmesin diye uyumak istemiyorum. Bir hikâye daha, bir öpücük daha?"

### Slide 4 — UNUTMAYIN!
- **Başlık:** UNUTMAYIN!
- **Body:** Uykuya direnç, çocuğunuzun günü size sığdırmak istemesidir. Sabit bir rutin, sakin sesiniz ve aynı kitap; güvenli bir köprüdür. Bugün: Yatak öncesi 10 dakikayı kucaklaşma ve tek bir sayfa için ayırın.

### Slide 5 — KAPANIŞ
> Yarın yine yorgun uyanabilirsin, biliyoruz. Ama bu küçük direnç, en derin sevginin imzasıdır. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (TEK STRING / slide)

### Slide 1
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, big bear cub character standing on a small hill made of pillows and a soft blanket, tiny moons and stars and sleepy clouds floating around, holding a small picture book, looking hopeful and cozy
```

### Slide 2
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, bear cub with mother bear character, warm hugging interaction at bedtime, mother kneeling beside a small bed tucking the cub in, cozy indoor bedroom scene, soft pillows and a tiny lamp
```

### Slide 3
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, small isolated bear cub sitting alone on a giant pillow, emotional vulnerable pose hugging a tiny teddy, vast empty space around with a few faint stars, scale contrast tiny cub looking up wide-eyed
```

### Slide 4
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, family scene, mother bear and bear cub reading a picture book together, warm cozy bedroom setting at night, small bed and soft blanket, tiny lamp casting gentle light
```

### Slide 5
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, bear cub waving goodnight smiling sweetly, sitting on a stack of three picture books, a tiny crescent moon beside it
```

## ⚠️ Bu çalıştırmada Higgsfield çağrısı YAPILAMADI

Bu Routine çalıştırmasında ADIM 4 (Higgsfield via Vercel relay) bu sandbox'tan çalıştırılamadı. Sandbox'ın egress proxy'si `vercel-hf-probe.vercel.app` (ve `api.ipify.org`, `ifconfig.me` gibi diğer arbitrary host'lar) için 403 `Host not in allowlist` döndürüyor.

```
$ curl -i https://vercel-hf-probe.vercel.app/
HTTP 403
Host not in allowlist
```

Bu sandbox'ın izinli host listesinde yalnızca github.com, pypi vb. var; Vercel relay'imize erişim yok. Bu yüzden `assets/gorseller/2026-04-25-sabah-9/slide-*.png` dosyaları **düz #C9DDEC arka plan** olarak hazırlandı (placeholder). Overlay text'ler bunların üzerine bindirildi, böylece pipeline ucu ucuna çalıştığını gösterebildi.

**Yapılması gereken (kullanıcı tarafında):**
1. Sandbox'ın egress allowlist'ine `vercel-hf-probe.vercel.app` ekle (Claude Code on the Web → repo settings → network policy), VEYA
2. `/tmp/prompts.json` içindeki 5 prompt'u local makinada çalıştır (`python3 scripts/relay_api.py submit-batch ...`), webhook commit'leri bu branch'e geldikten sonra `python3 scripts/overlay_text.py outputs/2026-04-25-sabah-9/layout.json` komutunu yeniden çalıştır — slide-*.png'ler gerçek illüstrasyonla yenilenir.

## ⚠️ Font'lar repo'da yok

`assets/fonts/BagelFatOne-Regular.ttf` ve `assets/fonts/Baloo2-Regular.ttf` repo'da yok (sadece README var). Overlay script PIL default font'una düştü. Görsel sonuç tipografisi nihai görünmeyecek. Bu da bir kerelik kullanıcı işidir: doğru .ttf dosyalarını `assets/fonts/` altına ekleyin.

## Çıktı Dosyaları
- `outputs/2026-04-25-sabah-9/slide-1.png` ... `slide-5.png` (bindirilmiş, placeholder zemin)
- `outputs/2026-04-25-sabah-9/raw/slide-1-raw.png` ... `slide-5-raw.png` (placeholder ham görseller)
- `outputs/2026-04-25-sabah-9/caption.txt`
- `outputs/2026-04-25-sabah-9/layout.json`
- `outputs/2026-04-25-sabah-9/icerik.md` (bu dosya)
