# Sincap Kitap IG — 2026-05-23 Sabah 09:00

## Konu
**Ayrılık kaygısı** (0-6 yaş)

## Palette
**MOR**
- Arka plan: `#7E5BA0`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF`

## Karakter
Baby squirrel (sincap yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — Kapak
- **Başlık (ana):** Anne, Beni
- **Başlık (aksan):** Bırakma!
- **Alt başlık:** Ayrılık kaygısı, sevginin derin kanıtıdır.

### Slide 2 — Tanıdık Sahne
> Kapıya yöneldiğinizde küçük eller eteğinize sarılıyor. Gözleri dolu, sesi titrek. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun Sesi
> "Seni göremeyince kalbim hızlı atıyor anne."

### Slide 4 — UNUTMAYIN!
> Ayrılık kaygısı, bağlanmanın sağlıklı bir parçası. Kısa ama net vedalar güveni büyütür. Bugün deneyin: "Yemekten sonra seni alacağım" gibi somut bir söz verin ve sözünüzü tutun.

### Slide 5 — Kapanış
> Bu süreçte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character with fluffy red-brown fur, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #7E5BA0 purple background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation,` + sahne:

1. big baby squirrel standing on a small hill, decorative leaves and stars around, looking hopeful
2. baby squirrel with mother squirrel parent, warm hugging interaction, cozy indoor scene with soft pillows
3. small isolated baby squirrel, emotional vulnerable pose holding a tiny acorn, vast empty space around with scale contrast, looking up hopefully
4. family scene, parent squirrel and baby squirrel reading book together, warm cozy bedroom setting with soft blanket
5. baby squirrel waving goodbye, smiling, sitting on a small stack of storybooks

Her görsel için: `1152x1536`, `1080p`.

## Görsel Üretim Durumu

**⚠ BLOKER:** Vercel relay (`vercel-hf-probe.vercel.app`) bu çalıştırma ortamının IP'sini reddetti — `403 host_not_allowed`. Higgsfield çağrıları yapılamadı.

Geçici çözüm olarak `assets/gorseller/2026-05-23-sabah-9/slide-{1-5}.png` altına solid `#7E5BA0` arka plan placeholder PNG'leri yerleştirildi. Metin overlay'i bunların üzerine başarıyla uygulandı. Gerçek Higgsfield illüstrasyonları için:

1. Bu prompt'u allowlist'te olan bir ortamdan (ör. yerel makine veya allowlist'e eklenmiş Routine container) Adım 4 ile yeniden çalıştırın.
2. Üretilen PNG'ler `assets/gorseller/2026-05-23-sabah-9/slide-{1-5}.png` yoluna geldikten sonra Adım 5'i tekrar koşun:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-05-23-sabah-9/layout.json
   ```

Alternatif: Vercel `vercel-hf-probe` projesinin relay allowlist'ine Claude Code on the Web (web) container IP aralığını ekleyin.

## Dosyalar

- `outputs/2026-05-23-sabah-9/slide-1.png` ... `slide-5.png` — final carousel (metin bindirilmiş)
- `outputs/2026-05-23-sabah-9/raw/slide-{1-5}-raw.png` — ham (placeholder) görseller
- `outputs/2026-05-23-sabah-9/caption.txt` — Instagram caption + hashtag
- `outputs/2026-05-23-sabah-9/layout.json` — overlay config
- `outputs/2026-05-23-sabah-9/icerik.md` — bu dosya
