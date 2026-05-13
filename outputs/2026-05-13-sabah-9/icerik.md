# Sincap Kitap IG — 2026-05-13 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: koyu kahve (`#3A2A1A`)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): "Anne, Yatmak"
- Başlık (aksan): "İstemiyorum!"
- Alt başlık: "Uyku direnci, gelişimin sessiz çığlığıdır."

### Slide 2 — TANIDIK SAHNE
> Pijama giyildi, dişler fırçalandı, kitap okundu. Ama gözleri hâlâ pırıl pırıl. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kapatınca seni kaybedecekmişim gibi geliyor."

### Slide 4 — UNUTMAYIN!
> Uykuya direnç, kontrol kaybı duygusudur. Aynı sırayla tekrarlanan kısa bir ritüel, çocuğa güvenli bir köprü kurar. Bugün deneyebilirsiniz: Işıkları kıstıktan sonra 3 dakika sessizce yanında oturun.

### Slide 5 — KAPANIŞ
> Bu yumuşak geçişte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt İskeleti
Her slide için ortak baz:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette,
solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

Slide bazlı sahneler:
- **Slide 1:** big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful, wearing soft pajamas
- **Slide 2:** bear cub with mother bear, warm hugging interaction, cozy indoor bedroom scene at night
- **Slide 3:** small isolated bear cub in pajamas, emotional vulnerable pose, vast empty space around, scale contrast, looking up at moon and stars
- **Slide 4:** family scene, mother bear and bear cub reading a bedtime book together, warm cozy bedroom setting, soft lamp light
- **Slide 5:** bear cub waving goodbye, smiling sleepily, sitting on a stack of storybooks with a small teddy

## Durum

**⚠️ Görsel üretim BLOKE — Higgsfield relay 403 "Host not in allowlist".**

`/tmp/prompts.json` hazırlandı, fakat `scripts/relay_api.py submit-batch` çağrısı
relay tarafından reddedildi. Olası nedenler:
1. Routine UI'ye paste edilirken `RELAY_SHARED_SECRET` placeholder'ı (`78e1...4a4`)
   gerçek Vercel değeriyle değiştirilmedi → gerçek secret routine'a hiç ulaşmadı.
2. Relay tarafında bir IP/host allowlist kuralı bu ortamı reddediyor.

Çözüldükten sonra şu komutla devam edilebilir (metinler ve layout zaten hazır):
```bash
SLOT="2026-05-13-sabah-9"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<GERÇEK_DEĞER>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-13-sabah-9/layout.json
```
