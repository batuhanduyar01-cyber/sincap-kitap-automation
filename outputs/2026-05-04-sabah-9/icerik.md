# Sincap Kitap IG — 2026-05-04 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3D2817` (koyu kahve)

## Karakter
Bear cub (yavru ayı) — 5 slide boyunca aynı karakter.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Uyumak Bu Kadar
- **Başlık (aksan):** Zor mu?
- **Alt başlık:** Uyku direnci, korkuyla değil sevgiyle çözülür.

### Slide 2 — TANIDIK SAHNE
> Saat 22:00. Üçüncü kez yataktan kalkıyor. "Susadım, bir öpücük daha, bir öykü daha…" Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> Karanlıkta gözlerimi kapatınca, sen yokmuşsun gibi geliyor.

### Slide 4 — UNUTMAYIN!
Uyku direnci, ayrılma anının zorluğudur. Sabit bir rutin güven verir. **Bugün:** yatmadan önce 10 dakika yan yana sessizce uzanın; konuşmasanız bile "birlikteyim" hissi yeter.

### Slide 5 — KAPANIŞ
> Uyku, sevgiyle ekilen bir tohum; sabırla büyür. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt İskeleti

Ortak baz (tüm slide'larda aynı):
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks,
warm painterly palette, solid #C9DDEC background,
Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation,
{SAHNE}
```

### Slide sahneleri
1. big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful
2. bear cub character with mother bear character, warm hugging interaction, cozy indoor scene
3. small isolated bear cub character, emotional vulnerable pose, vast empty space around (scale contrast), looking up at a moon
4. family scene, parent bear and child bear cub reading book together, warm cozy bedroom setting
5. bear cub character waving goodbye, smiling, sitting on a book stack

Boyut: `1152x1536` (4:5 portrait), kalite `1080p`.

## Çalıştırma Notları

### Görsel üretimi (Routine UI / Vercel relay üzerinden)
```bash
SLOT="2026-05-04-sabah-9"
BRANCH="claude/quirky-mendel-DQ18a"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot    "$SLOT" \
    --branch  "$BRANCH" \
    --prompts-file outputs/2026-05-04-sabah-9/prompts.json
```

### Metin bindirme (görseller `assets/gorseller/$SLOT/` altında hazır olduktan sonra)
```bash
git pull --ff-only origin "$BRANCH"
cp outputs/2026-05-04-sabah-9/layout.json layout.json
python3 scripts/overlay_text.py layout.json
```

## Caption / Hashtag
`outputs/2026-05-04-sabah-9/caption.txt` dosyasında.

## Bu çalıştırmada (2026-05-04) Bilinmesi Gerekenler

Bu Routine, Claude Code on the web ortamında çalıştırıldı. Vercel relay
(`https://vercel-hf-probe.vercel.app/api/hf/submit`) IP allowlist'i Anthropic
Routine runner IP'lerine göre yapılandırılmış; Claude Code on the web farklı
egress IP'lerinden çıktığı için **403 "Host not in allowlist"** döndü.

Bu yüzden Adım 4 (Higgsfield görsel üretimi) ve Adım 5 (PIL metin bindirme)
**bu oturumda atlandı**. Tüm metin/config artefaktları (`prompts.json`,
`layout.json`, `caption.txt`, `icerik.md` ve log girişi) commit edildi —
gerçek Routine UI üzerinden submit-batch komutu çalıştırıldığında
otomatik olarak görseller üretilecek ve overlay scripti hazırdır.
