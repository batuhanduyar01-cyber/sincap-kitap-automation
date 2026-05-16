# Sincap Kitap IG — 2026-05-16 Öğle 12:00

## Konu

**yatmayı istememe** (yatma vaktine direnç, çocuk perspektifinden)

Tekrar kontrolü: `logs/ogle-12.md` boştu — son 14 günde kullanılmış konu yok.
Seçilen konu loga eklendi: `- 2026-05-16: yatmayı istememe`

## Palette

**MOR** — çocuğun gözünden gece/uyku temasına uygun.

| Alan | Renk |
|---|---|
| Arka plan (bg) | `#7E5BA0` |
| Aksan (accent) | `#C5E86C` |
| Metin (text) | `#FFFFFF` |

5 slide boyunca sabit kullanıldı.

## Karakter

Sevimli ayı yavrusu (bear cub) — pijamalı, uykulu ama neşeli. 5 slide'da aynı.

## Slide Metinleri (çocuk ağzından, alıntı ağırlıklı)

### Slide 1 — KAPAK
- Başlık (ana): **Daha Uykum**
- Başlık (aksan): **Gelmedi!**
- Alt başlık: Gözlerim açık, dünya hâlâ çok eğlenceli.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Uyumak istemiyorum, çünkü seninle geçen her an çok güzel."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Koca bir günü daha yeni bitiriyorum, durmak için biraz zamana ihtiyacım var."

### Slide 4 — EBEVEYN NOTU
- Başlık: **Ebeveyn Notu**
- Gövde: Çocuklar uykuya geçişi yavaş yavaş öğrenir. Sakin bir beden, sakin bir uyku getirir. Bugün: yatmadan önce hep aynı sırayı izleyin — kitap, sarılma, iyi geceler.

### Slide 5 — KAPANIŞ
- Gövde (görselde): İyi geceler! Yarın yeni maceralara birlikte uyanırız. Sincap Kitap'ı takip et.
- Not: 🐿️ emojisi caption'da yer alıyor; paketlenen fontlar (Bagel Fat One / Baloo 2) emoji glifi içermediğinden görsele bindirilmedi (aksi halde boş kutu çıkıyor).

## Higgsfield Prompt'ları (relay üzerinden gönderilen 5 prompt)

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character wearing cozy pajamas, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #7E5BA0 background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, {SAHNE}`

1. **Slide 1:** bear cub in a dynamic playful pose wide awake at bedtime hugging a small teddy, one paw rubbing an eye but smiling, 6 decorative elements around (stars, crescent moons, sparkles)
2. **Slide 2:** bear cub and a parent bear in a warm loving hug under a soft blanket, both giggling together, cozy night-time interaction
3. **Slide 3:** a small lonely bear cub sitting alone in a big bed, tiny scale against a vast dark bedroom, looking up with an emotional vulnerable expression
4. **Slide 4:** calm cozy scene of a parent bear and bear cub reading a bedtime storybook together in bed, soft warm lamp glow, gentle bonding moment
5. **Slide 5:** bear cub waving goodbye with a cheerful sleepy smile wearing pajamas, standing next to a small stack of books, holding a tiny glowing nightlight

Tümü `1152x1536`, `1080p` olarak gönderildi (`/tmp/prompts.json`).

## Layout config

`outputs/2026-05-16-ogle-12/layout.json` (repo `.gitignore` `layout.json` dosyalarını yok saydığı için commit'lenmez):

- output_dir: `outputs/2026-05-16-ogle-12`
- palette: bg `#7E5BA0`, accent `#C5E86C`, text `#FFFFFF`
- 5 slide: cover / quote / quote / tip / cta

## ÖNEMLİ — Görsel üretimi tamamlanamadı

ADIM 4 (Higgsfield görselleri) bu çalıştırma ortamında **tamamlanamadı**.

- Relay'e (`https://vercel-hf-probe.vercel.app`) yapılan POST `403 "Host not in allowlist"` döndü.
- Aynı şekilde `higgsfield.ai` ve `vercel.com` da `403` döndü.
- Sebep: bu uzak çalıştırma ortamının ağ politikası (allowlist) bu host'ları engelliyor — relay'in kendisiyle veya `RELAY_SHARED_SECRET` ile ilgili bir sorun değil. (`pypi.org` ve `github.com` erişilebilir durumda.)
- `relay_api.py submit-batch` exit kodu: **3** (submit fail).

Bu nedenle `outputs/2026-05-16-ogle-12/slide-*.png` dosyaları, gerçek
suluboya illüstrasyonlar yerine **düz `#7E5BA0` arka plan üzerine metin
bindirilmiş ÖN İZLEME slaytlarıdır**. Ham yer tutucular `raw/slide-*-placeholder.png`.

### Tamamlamak için
Ağ politikası relay host'una izin veren bir ortamda:

```bash
SLOT="2026-05-16-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
git pull --ff-only origin "$BRANCH"
```

Ardından `layout.json` içindeki `raw_image` yollarını
`assets/gorseller/2026-05-16-ogle-12/slide-N.png` olarak güncelleyip
`python3 scripts/overlay_text.py outputs/2026-05-16-ogle-12/layout.json`
komutunu yeniden çalıştırmak yeterli — metinler ve yerleşim hazır.

## Bu çalıştırmada yapılan diğer düzeltmeler

- `assets/fonts/BagelFatOne-Regular.ttf` ve `Baloo2-Regular.ttf` indirildi
  (önceden eksikti; GitHub Google Fonts mirror'ından çekildi).
- `scripts/overlay_text.py` → `render_cover`: başlık / aksan / alt başlık
  blokları üst üste biniyordu. Blok yerleşimi font metriklerine
  (`getmetrics`) göre yeniden yazıldı.
