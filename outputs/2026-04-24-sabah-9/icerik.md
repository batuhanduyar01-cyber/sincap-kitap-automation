# Sincap Kitap IG Post — 2026-04-24 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
`bear cub` (ayı yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Yerde Yatan
- **title_accent:** O Minik Dev
- **subtitle:** Öfke nöbeti, kaybolan kontrolün sesidir.

### Slide 2 — TANIDIK SAHNE
> Markette sıra bekliyorsunuz. Birden yere uzanıp çığlığa başlıyor. Herkes size bakıyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "İçimde büyük bir fırtına var, durduramıyorum."

### Slide 4 — UNUTMAYIN!
> Öfke, kötü bir çocuk işareti değil; gelişmekte olan bir beyin, büyük duyguları taşımayı yeni öğreniyor.
>
> **Bugün:** Yere çöküp "Seninle birlikte nefes alalım mı?" deyin.

### Slide 5 — KAPANIŞ
> Bu fırtınalı günlerde sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Ortak iskelet (tüm slide'larda ortak):
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks,
warm painterly palette, solid #E63B5C background,
Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation,
<SAHNE>
```

Slide bazında `<SAHNE>`:
1. `big character standing on a small hill, decorative leaves and stars around, looking hopeful`
2. `character with mother/parent character, warm hugging interaction, cozy indoor scene`
3. `small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up`
4. `family scene, parent and child reading book together, warm cozy bedroom setting`
5. `character waving goodbye, smiling, sitting on a book stack`

Boyut: `1152x1536`, kalite: `1080p`.

## Instagram Caption
→ `caption.txt` dosyasına bakınız (400-500 kelime, anne dili).

## Durum
⚠️ **Görsel üretimi eksik** — Vercel relay `/api/hf/submit` endpoint'ine atılan istek
`HTTP 403 "Host not in allowlist"` hatası döndürdü. Büyük olasılıkla prompt'ta inline
paste edilen `RELAY_SHARED_SECRET` değeri Vercel dashboard'daki gerçek değerle
değiştirilmemiş ya da relay tarafında ek bir host/origin allowlist check'i hata veriyor.

Relay düzeldiğinde aşağıdaki komutlar yeterlidir:

```bash
SLOT="2026-04-24-sabah-9"
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# 1) Prompt dosyasını yeniden oluştur (zaten repoda: scripts/ içinde değil, aşağıdaki
#    tabloya göre /tmp/prompts.json'u üret) ve relay'e submit et:
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<GERÇEK_VERCEL_DEĞERİ>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file /tmp/prompts.json

# 2) Webhook commit'lerini çek ve text overlay'i uygula:
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-04-24-sabah-9/layout.json
```
