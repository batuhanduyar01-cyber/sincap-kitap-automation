# Sincap Kitap IG — 2026-06-10 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca tutarlı.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Yere Yatıp
- **Aksan kelime:** Patlıyor!
- **Alt başlık:** Öfke, küçük bedende büyük bir duygu.

### Slide 2 — TANIDIK SAHNE
> Markette istediği şekeri alamayınca yere yatıyor, çığlık atıyor. Etraftaki bakışlar üzerinizde, içiniz sıkışıyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> İçimde kocaman bir fırtına var, ama ben çok küçüğüm.

### Slide 4 — UNUTMAYIN!
> Öfke nöbeti şımarıklık değil, gelişimsel bir alarm sistemidir. Çocuk size 'baş edemiyorum' diyor. Bugün deneyebilirsiniz: Sözcüklerden önce sarılın, sakin bir sesle 'Yanındayım' deyin.

### Slide 5 — KAPANIŞ
> Her fırtına geçer, sevgi kalır. Bu süreçte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #E63B5C background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

| Slide | Sahne |
|---|---|
| 1 | big bear cub standing on a small hill, decorative leaves and stars around, looking hopeful with a brave little smile |
| 2 | bear cub being gently held by a calm mother bear, warm hugging interaction during a small storm of emotions, cozy indoor scene |
| 3 | tiny isolated bear cub curled up, emotional vulnerable pose, vast empty space around (scale contrast), tears in expressive eyes, looking up |
| 4 | family bear scene, parent and bear cub reading a picture book together, warm cozy bedroom setting, calm restorative atmosphere |
| 5 | bear cub waving goodbye, smiling softly, sitting on a small stack of storybooks |

Boyut: `1152x1536` (4:5), kalite: `1080p`.

## Çıktı Dosyaları
- `slide-1.png` ... `slide-5.png` — final (metin bindirilmiş)
- `raw/slide-1-raw.png` ... `raw/slide-5-raw.png` — ham (Higgsfield çıktısı)
- `caption.txt` — Instagram caption + hashtag'ler
- `layout.json` — overlay_text.py config'i

## Görsel Üretim Notu
Bu çalıştırmada Vercel relay (`vercel-hf-probe.vercel.app`) tüm istekleri
`403 host_not_allowed` ile reddetti — bu Claude Code on the Web container'ının
çıkış IP'si relay'in allowlist'inde yok. Bu yüzden `raw/` klasörü
geçici **düz AHUDUDU arka planlı** placeholder PNG'ler içeriyor;
overlay metni doğru ama illüstrasyonlar boş.

Düzeltmek için:
1. Vercel dashboard → `vercel-hf-probe` → Settings → relay allowlist'ine
   bu session'ın IP'si veya Routine UI çağrı IP'si eklensin, **veya**
2. Routine UI'nin allowlist'li bir kanaldan tetiklenmesi gerekiyor.

Allowlist düzeltilince:
```bash
SLOT="2026-06-10-sabah-9"
BRANCH="claude/quirky-mendel-mw7vkx"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file /tmp/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/$SLOT/layout.json
```
yapılınca ham PNG'ler ve final slide'lar yenilenir.
