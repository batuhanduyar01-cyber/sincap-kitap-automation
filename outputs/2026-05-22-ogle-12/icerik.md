# Sincap Kitap IG Post — 2026-05-22 Öğle 12:00

## Konu
**Diş fırçalatmama** (çocuk perspektifinden, eğlenceli/oyunsu ton)

## Palette
**HARDAL** — Arka plan `#F5C82E` / Aksan `#8E4FAA` mor / Metin `#3D2817` koyu kahve

## Karakter
Sevimli bebek timsah (baby crocodile) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Ana başlık: **Dişlerim**
- Aksan: **Pırıl Pırıl!**
- Alt başlık: Fırçam benim minik arkadaşım.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Seninle birlikte fırçalarken kahkaha atmak çok eğlenceli!"

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Bazen acelem var ama minik dişlerim de azıcık sevgi istiyor."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**
Diş fırçalamak çocuk için bir oyuna dönüşebilir. Acele ettirmeden, gülümseyerek eşlik edin. İpucu: Fırçalama süresi boyunca kısa, neşeli bir şarkı söyleyin.

### Slide 5 — KAPANIŞ
Şimdi gülüşüm pırıl pırıl! Daha çok macera için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Ortak iskelet:
`Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby crocodile character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F5C82E background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, {SAHNE}`

- **Slide 1:** baby crocodile in dynamic expressive pose holding a tiny toothbrush, happy open smile showing little teeth, 5-8 decorative elements around (sparkles, bubbles, tiny stars)
- **Slide 2:** baby crocodile with a parent crocodile in warm loving interaction, giggling together while brushing teeth, cozy bathroom scene
- **Slide 3:** isolated small baby crocodile, tiny scale against vast soft background, emotional vulnerable pose looking up, holding toothbrush hesitantly
- **Slide 4:** calm adult crocodile and child crocodile cozy bonding moment, brushing teeth together gently, warm cozy bathroom setting
- **Slide 5:** baby crocodile waving goodbye with a cheerful sparkling smile, standing next to a small stack of books

Boyut: `1152x1536`, kalite: `1080p`.

## Durum Notu — ADIM 4 (Görsel Üretimi) BLOKLANDI

Higgsfield görselleri **üretilemedi**. Vercel relay (`https://vercel-hf-probe.vercel.app`)
bu Routine ortamının ağ politikası tarafından engelleniyor:

```
POST /api/hf/submit → HTTP 403 "Host not in allowlist"
```

Aynı şekilde `higgsfield.ai` ve `api.github.com` da 403 dönüyor; yalnızca
`github.com` (git push/pull) erişilebilir durumda.

Relay, Higgsfield'ın Cloudflare WAF bloğunu aşmak için kuruluydu; fakat bu sefer
relay'in kendi alan adı da ortamın çıkış (egress) allowlist'inde değil. Bu hard
bir politika bloğu — yeniden deneme transient değil.

**Çözüm:** Routine ortamının ağ politikasına `vercel-hf-probe.vercel.app`
(ve gerekiyorsa `*.vercel.app`) host'u allowlist'e eklenmeli. Ardından:

```bash
SLOT="2026-05-22-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-22-ogle-12/layout.json
```

`layout.json` hazır; görseller `assets/gorseller/2026-05-22-ogle-12/slide-N.png`
yoluna geldiğinde overlay adımı sorunsuz çalışacaktır.
