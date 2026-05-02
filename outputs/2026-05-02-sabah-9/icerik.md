# Sincap Kitap IG — 2026-05-02 Sabah 09:00

## Konu
**Kardeş kıskançlığı**

Anne odaklı, sıcak, empatik, yargısız ton. "Yalnız değilsin" hissi.

## Palette
**AHUDUDU**

| Rol | Hex |
|---|---|
| Arka plan | `#E63B5C` |
| Aksan | `#C5E86C` (yeşil) |
| Metin | `#FFFFFF` (beyaz) |

## Karakter
Bear cub (yavru ayı) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — Kapak
- **Başlık (ana):** Sevgi Tükenir mi?
- **Başlık (aksan):** Asla.
- **Alt başlık:** Kardeş kıskançlığı, küçük bir kalbin büyük korkusu.

### Slide 2 — Tanıdık Sahne
> Bebeği kucağa alınca, büyük çocuğun gözleri buğulanıyor. Kollarını uzatıyor: "Beni de tut." Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun Sesi (alıntı)
> Sen onu kucaklayınca, ben kalbimde bir şey kaybediyorum.

### Slide 4 — UNUTMAYIN!
> Çocuğunuz kötü değil, sadece korkuyor. Kıskançlık, sevginin paylaşılınca azalacağına dair masum bir inanç. Bugün: yalnız ona ait, telefonsuz 10 dakikalık bir "sadece sen ve ben" anı yaratabilirsiniz.

### Slide 5 — Kapanış
> Kalbinde herkese yer var; hem ona, hem sana. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları (5 slide ortak iskelet)

```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly
palette, solid #E63B5C background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading,
portrait orientation, {SAHNE}
```

| Slide | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | bear cub character with mother bear character, warm hugging interaction, cozy indoor scene |
| 3 | small isolated bear cub character, emotional vulnerable pose, vast empty space around (scale contrast), looking up |
| 4 | family scene, parent bear and bear cub reading book together, warm cozy bedroom setting |
| 5 | bear cub character waving goodbye, smiling, sitting on a book stack |

## Üretim Durumu

⚠️ **ENGELLENDİ — Vercel relay 403 host_not_allowed**

Higgsfield görselleri üretilemedi. Tüm POST/GET istekleri Vercel relay'in
edge middleware'inde reddedildi:

```
HTTP/2 403
x-deny-reason: host_not_allowed
content-length: 21
content-type: text/plain
Host not in allowlist
```

Sebep adayları:
1. `RELAY_SHARED_SECRET` Routine prompt'unda placeholder hex
   (`78e1e7737...0e34645a4`) olarak kalmış olabilir; Vercel'deki gerçek
   değerle değiştirilmemiş.
2. Vercel relay'in source-IP / host allowlist'inde Anthropic Routine
   runner'ının çıkış IP'si yok.

İkinci adımda relay'in içindeki middleware Higgsfield'a hiç çağrı atamadan
isteği reddediyor — bu mevcut runner ortamından çözülemez.

### Manuel Devam Etmek İçin

Relay düzeltildikten sonra (gerçek secret + allowlist), aşağıdaki komutlar
elinizdeki makinada çalıştırılarak görseller üretilip overlay yapılabilir:

```bash
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<vercel'deki gerçek secret>"
export SLOT="2026-05-02-sabah-9"
export BRANCH="claude/quirky-mendel-jnAuT"

# /tmp/prompts.json bu repo'ya 'outputs/2026-05-02-sabah-9/prompts.json'
# olarak commit'lendi.
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" \
    --branch "$BRANCH" \
    --prompts-file outputs/2026-05-02-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"

python3 scripts/overlay_text.py outputs/2026-05-02-sabah-9/layout.json
```
