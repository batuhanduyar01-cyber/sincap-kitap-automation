# Sincap Kitap IG — 2026-04-28 Sabah 09:00

## Konu
**uyku direnci** (0-6 yaş)

Son 14 gün log'u boştu, çakışma yok. `logs/sabah-9.md` güncellendi.

## Palette
**TOZ MAVİSİ** — sakinlik / uyku eşleşmesi

| Rol | Hex |
|---|---|
| Arka plan | `#C9DDEC` |
| Aksan | `#E97E28` (turuncu) |
| Metin | `#3E2A1F` (koyu kahve) |

## Karakter
`bear cub` (ayıcık) — pijamalı, uykulu büyük gözler, yatma teması için sıcak ve ailesel bir karakter. 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): **Anne, Daha Uyumak**
- Başlık (aksan): **İstemiyorum!**
- Alt başlık: *Uyku direnci, güvene duyulan bir çağrıdır.*
- Dekorasyon: var

### Slide 2 — TANIDIK SAHNE (inner)
> Saat geç, sen yorgunsun, o hâlâ kıpır kıpır. Bir bardak su daha, bir öpücük daha... Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (quote)
> Karanlık çok büyük, sen yanımda olunca küçülüyor.

### Slide 4 — UNUTMAYIN! (tip)
**UNUTMAYIN!**
> Uyku direnci inatçılık değil, güvenli liman arayışıdır. Sabit bir rutin, çocuğunuza "her şey yolunda" der. Bugün: Yatmadan 30 dakika önce ışıkları kısın, fısıltıyla konuşun.

### Slide 5 — KAPANIŞ (cta)
> Sakin geceler kuran kitaplarla yanındayız. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Tüm prompt'lar ortak iskelet kullanır: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character in soft pajamas, large expressive [sleepy/vulnerable] eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

| Slide | Sahne |
|---|---|
| 1 | big bear cub character standing on a small fluffy hill of pillows, decorative crescent moons stars and tiny clouds floating around, holding a small lantern, looking hopeful and curious |
| 2 | bear cub character with a tender mother bear character, warm hugging interaction at bedside, cozy indoor bedroom scene with soft blanket and a small lamp, mother stroking cub's head |
| 3 | small isolated bear cub character sitting alone on a giant bed, emotional vulnerable pose, vast empty space around with scale contrast, looking up toward a single window with moonlight, tiny dust particles in the air |
| 4 | family scene of mother bear and bear cub reading a storybook together, warm cozy bedroom setting, soft lamp glow, snuggled under a quilt with stars and moons pattern |
| 5 | bear cub character waving goodnight goodbye, gentle smile, sitting on a small stack of storybooks, tiny crescent moon and stars floating gently around |

Tam JSON: `/tmp/prompts.json` (bu repo'ya commit edilmemiş; gerektiğinde `outputs/2026-04-28-sabah-9/prompts.json`'dan da okunabilir).

## Uygulama Durumu — Higgsfield/Vercel Relay BLOKLU ⚠️

Bu Routine ortamından `https://vercel-hf-probe.vercel.app` relay'ine yapılan **her** istek edge tarafında reddediliyor:

```
HTTP 403
Host not in allowlist
```

- Hem `GET /` hem `POST /api/hf/submit` aynı yanıtı döndürüyor.
- Bu, auth (401) değil, **IP/host-level allowlist** bloğu. Yani `RELAY_SHARED_SECRET` doğru olsa bile request relay app koduna ulaşmıyor.
- `relay_api.py submit-batch` exit code 3 ile düştü.

### Unblock için yapılması gerekenler
1. Vercel projesi `vercel-hf-probe` → bu Routine container'ının egress IP'si (veya Anthropic Routine IP aralığı) WAF/host allowlist'e eklenmeli.
2. Eklendikten sonra aşağıdaki tek komutla görseller tetiklenip commit'lenir; sonrasında `overlay_text.py` çalıştırılır:

```bash
export SLOT="2026-04-28-sabah-9"
export BRANCH="claude/quirky-mendel-yjLtu"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<gerçek değer>"

python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-04-28-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-04-28-sabah-9/layout.json
```

`prompts.json`, `layout.json`, `caption.txt`, ve bu `icerik.md` zaten branch'e commit'li olduğu için relay açılır açılmaz iş tek komutla tamamlanır.
