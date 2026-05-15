# Sincap Kitap IG — 2026-05-15 Öğle 12:00

## Konu
**"ben yaparım" ısrarı** — Çocuğun her şeyi kendi başına yapma isteği (bağımsızlık dönemi).

Ton: Çocuk odaklı, eğlenceli, oyunsu — çocuklarla birlikte okunabilir.

## Palette — HARDAL
| Rol | Renk |
|---|---|
| Arka plan (bg) | `#F5C82E` |
| Aksan (accent) | `#8E4FAA` mor |
| Metin (text) | `#3D2817` koyu kahve |

5 slide boyunca sabit kullanıldı.

## Karakter
Sevimli **sincap yavrusu** (baby squirrel) — 5 slide'da aynı. Sincap Kitap maskotuyla uyumlu.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): "Bırak, Ben"
- Başlık (aksan): "Yaparım!"
- Alt başlık: "Minik eller, kocaman işler başarmak ister."

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Sen yanımdayken denemekten hiç korkmuyorum."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Yavaş oluyorum, biliyorum ama kendim başarmak istiyorum."

### Slide 4 — EBEVEYN NOTU
- Başlık: "Ebeveyn Notu"
- Metin: "Çocuğunuz 'ben yaparım' derken bağımsızlığını inşa ediyor. Acele etmeyin, hatasıyla denemesine izin verin. İpucu: İşlere 10 dakika erken başlayın, denemeye vakit kalsın."

### Slide 5 — KAPANIŞ (CTA)
- Metin: "Bugün ayakkabımı kendim giydim, görüşürüz! Sincap'ın maceralarının tamamı için Sincap Kitap'ı takip et 🐿️"

Her slide ≤ 35 kelime.

## Higgsfield Prompt'ları

Ortak iskelet:
`Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F5C82E background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, {SAHNE}`

| Slide | Sahne |
|---|---|
| 1 | baby squirrel in a dynamic proud pose trying to button its own little jacket all by itself, determined cheerful expression, 6 decorative elements around (acorns, leaves, sparkles) |
| 2 | baby squirrel with a warm parent squirrel in a loving interaction, parent gently encouraging and the little one giggling, cozy supportive moment |
| 3 | isolated small baby squirrel against a vast empty background, small scale, concentrating hard on tying a tiny shoelace, focused but vulnerable pose |
| 4 | calm cozy scene of an adult squirrel and a child squirrel bonding together, sitting close and chatting warmly, gentle patient moment |
| 5 | baby squirrel waving goodbye with a cheerful happy smile, standing next to a small stack of books |

Boyut: 1152x1536, kalite: 1080p.

## Caption
Bkz. `caption.txt` (Instagram caption + 20 hashtag).

## DURUM — Görsel üretimi engellendi

ADIM 4 (Higgsfield görselleri) **bu ortamda tamamlanamadı.** Vercel relay'i
(`vercel-hf-probe.vercel.app`) ve Higgsfield'in kendisi (`higgsfield.ai`),
ortamın ağ allowlist'i tarafından engelleniyor:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

GitHub erişimi çalışıyor; sadece relay/Higgsfield host'ları allowlist dışında.
Relay, Higgsfield'in Cloudflare WAF'ını aşmak için kurulmuştu — ancak ortamın
kendi ağ politikası bu sefer relay host'unu da blokluyor.

**Çözüm:** Ortamın ağ politikasına `vercel-hf-probe.vercel.app` host'u
eklenmeli. Ardından ADIM 4-5 yeniden çalıştırılabilir:

```bash
SLOT="2026-05-15-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-15-ogle-12/layout.json
```

`layout.json` ham görselleri `assets/gorseller/2026-05-15-ogle-12/slide-N.png`
yolundan bekler; relay görselleri tam o yola commit'ler.

### text-preview/
Görsel pipeline ve Türkçe font render'ı doğrulamak için, ham illüstrasyon
yerine düz HARDAL (#F5C82E) zemin kullanılarak üretilmiş tipografi önizlemesi.
Bunlar **final değildir** — Higgsfield illüstrasyonları gelince
`layout.json` ile gerçek slide'lar üretilecek.
