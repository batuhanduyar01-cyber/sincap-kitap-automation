# Sincap Kitap IG — 2026-06-16 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: koyu kahve `#3D2A1F`

## Karakter (Higgsfield)
**bear cub** — 5 slide boyunca sabit, gece/uyku temasıyla doğal eşleşme.

## Slide metinleri

### Slide 1 — Kapak
- **Başlık (ana):** "Bir Daha"
- **Başlık (aksan, turuncu):** "5 Dakika!"
- **Alt başlık:** "Uyku direnci, bağımsızlık adımlarının bir parçasıdır."

### Slide 2 — Tanıdık Sahne
> Banyo bitti, pijama giydi, masal okundu. Ama yine kalkıyor, su istiyor, sarılmak istiyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun Sesi (alıntı)
> "Karanlıkta seni göremeyince güvende hissetmiyorum."

### Slide 4 — UNUTMAYIN!
> Uykuya direnç çoğu zaman gündüzü bırakma korkusudur. Tutarlı bir ritüel —banyo, kitap, sarılma— beyne 'şimdi güvenle gevşeyebilirsin' der. Bugün deneyin: bir kitap, bir öpücük, tek bir küçük ışık.

### Slide 5 — Kapanış / CTA
> Geceyi yumuşatan masallarla çocuğunun uykusu sakinleşsin. Sincap Kitap'ı takip et 🐿️

## Higgsfield prompt iskeleti (her slide)

```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly
palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading, portrait
orientation, {SAHNE}
```

Sahneler `outputs/2026-06-16-sabah-9/prompts.json` içinde tam metin.

## ÜRETİM DURUMU — BLOKE

`scripts/relay_api.py submit-batch` çağrısı, Vercel relay'in DNS isteğinde
**HTTP 403 "Host not in allowlist: vercel-hf-probe.vercel.app"** ile döndü.

Routine ortamının network egress allowlist'ine `vercel-hf-probe.vercel.app`
eklenmesi gerekiyor. Eklendikten sonra:

```bash
SLOT="2026-06-16-sabah-9"
BRANCH="claude/quirky-mendel-o82e39"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-06-16-sabah-9/prompts.json
```

ardından

```bash
python3 scripts/overlay_text.py outputs/2026-06-16-sabah-9/layout.json
```

ile final PNG'ler üretilebilir.

> Not: `assets/fonts/` boş — Bagel Fat One ve Baloo 2 dosyaları eklenmediği için
> overlay scripti default Pillow fontuna düşer. Final yayın öncesi fontların
> eklenmesi önerilir.
