# Sincap Kitap IG — 2026-06-03 Sabah 09:00

## Konu
**öfke nöbetleri** (tantrums)

## Palette
**AHUDUDU** — Arka plan: `#E63B5C`, Aksan: `#C5E86C` (yeşil), Metin: `#FFFFFF` (beyaz)

## Karakter
bear cub (5 slide boyunca sabit)

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Anne, Beni
- **Başlık (aksan):** Anla.
- **Alt başlık:** Öfke nöbeti, duyulmak isteyen küçük bir kalbin sesidir.

### Slide 2 — TANIDIK SAHNE
> Markette küçük omuzları titriyor, gözyaşları sel oluyor. Etraftan bakanlar var. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "İçimde kocaman bir fırtına var, ama nasıl söyleyeceğimi bilmiyorum."

### Slide 4 — UNUTMAYIN!
- **Başlık:** UNUTMAYIN!
- **Gövde:** Öfke nöbetleri, küçük beyinlerin büyük duygularla baş etme denemesidir. Yargılamadan yanında durmak en güçlü destektir. Bugün: Çömelin, göz hizasında "Yanındayım, geçecek" deyin.

### Slide 5 — KAPANIŞ
> O fırtınalı anların elinizden tutacak hikayeler için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (5 slide, AHUDUDU + bear cub)

Ortak iskelet:
> `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #E63B5C background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

Sahneler:
1. big bear cub standing on a small hill, decorative leaves and stars around, looking hopeful
2. bear cub with mother bear, warm hugging interaction, cozy indoor scene
3. small isolated bear cub, emotional vulnerable pose, vast empty space around, scale contrast, looking up
4. family scene, mother bear and cub reading book together, warm cozy bedroom setting
5. bear cub waving goodbye, smiling, sitting on a book stack

## Çalıştırma Notu — Relay Allowlist Engeli

Bu run'da Higgsfield görsel üretim adımı (ADIM 4b) **gerçekleşmedi**. Sebep:

```
POST https://vercel-hf-probe.vercel.app/api/hf/submit
HTTP 403 "Host not in allowlist"
```

Aynı 403 auth header'ı olmadan da dönüyor — yani sorun `RELAY_SHARED_SECRET` değil, Vercel relay'in kendi **host/IP allowlist**'i. Bu Claude Code on the web egress host'u relay'in allowlist'inde değil.

### Yeniden çalıştırmak için

1. Vercel dashboard → Project `vercel-hf-probe` → relay'in host allowlist konfigürasyonuna bu ortamın egress host'unu ekleyin (veya allowlist'i geçici olarak kapatın).
2. Routine prompt'undaki `RELAY_SHARED_SECRET` placeholder değerini Vercel'deki gerçek değerle değiştirin.
3. Aşağıdaki komutu tekrar çalıştırın:

```bash
SLOT="2026-06-03-sabah-9"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot    "$SLOT" \
    --branch  "$BRANCH" \
    --prompts-file /tmp/prompts.json
```

4. Görseller commit'lendikten sonra `git pull --ff-only` ile çekip:

```bash
python3 scripts/overlay_text.py outputs/2026-06-03-sabah-9/layout.json
```

ile final slide'ları oluşturun. `layout.json` bu klasörde hazır.
