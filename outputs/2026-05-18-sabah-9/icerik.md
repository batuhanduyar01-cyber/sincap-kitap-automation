# Sincap Kitap IG — 2026-05-18 Sabah 09:00

## Konu

**Kardeş kıskançlığı** (0-6 yaş)

Tekrar kontrolü: `logs/sabah-9.md` okundu — log boştu, son 14 günde kullanılmış konu yok. Konu loga eklendi.

## Palette

**AHUDUDU**

| Rol | Renk |
|---|---|
| Arka plan | `#E63B5C` |
| Aksan | `#C5E86C` (yeşil) |
| Metin | `#FFFFFF` (beyaz) |

Gerekçe: Kardeş kıskançlığı sıcak, duygusal bir konu → AHUDUDU. Beyaz metin koyu ahududu zemininde 5 slide boyunca yüksek kontrast sağlıyor (alıntı slide'ı dahil).

## Karakter

**Bear cub (ayı yavrusu)** — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): `Bir De Ben`
- Başlık (aksan): `Varım!`
- Alt başlık: `Kıskançlık, 'beni unutma' demenin bir yoludur.`

### Slide 2 — TANIDIK SAHNE
> Kucağınız yeni bebekle doluyken, büyük çocuğunuzun o buruk bakışını yakalıyorsunuz. İçiniz ikiye bölünüyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> Ben de küçükken bana böyle sarılıyordun. Hâlâ senin bebeğin miyim?

### Slide 4 — UNUTMAYIN!
> Kıskançlık sevgisizlik değildir; sevgiyi kaybetme korkusudur. Büyük çocuğunuza 'sadece sana ait' küçük anlar yaratın, kıyaslamadan uzak durun. Bugün: 10 dakika telefonsuz, yalnızca onunla bir oyun zamanı geçirin.

### Slide 5 — KAPANIŞ
> Kalbin büyür, anne; iki çocuğa da yeter, hatta artar. Bu yolculukta size eşlik edecek kitaplar için Sincap Kitap'ı takip et.

(Görsele bindirilen metinden 🐿️ emojisi çıkarıldı — Baloo 2 fontunda emoji glifi yok, "tofu" kutusu olarak render oluyordu. Emoji caption'da korundu; Instagram caption'ı emojiyi doğal render eder.)

## Higgsfield Prompt'ları

Karakter: bear cub · Palette hex: `#E63B5C` · 1152x1536 · 1080p

**Slide 1:**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #E63B5C background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, big character standing on a small hill, decorative leaves and stars around, looking hopeful

**Slide 2:**
> ... portrait orientation, character with mother/parent character, warm hugging interaction, cozy indoor scene

**Slide 3:**
> ... portrait orientation, small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up

**Slide 4:**
> ... portrait orientation, family scene, parent and child reading book together, warm cozy bedroom setting

**Slide 5:**
> ... portrait orientation, character waving goodbye, smiling, sitting on a book stack

(Slide 2-5 prompt'larının baş kısmı slide 1 ile aynı iskelet; sadece sahne tanımı farklı. Tam JSON: repo `/tmp/prompts.json` formatında, bu dosyanın altındaki "Görsel üretim notu"na bakınız.)

## Görsel Üretim Notu — ÖNEMLİ

ADIM 4 (Higgsfield görselleri) bu Routine ortamında **tamamlanamadı**.

- Higgsfield doğrudan Anthropic IP'lerini blokluyor → Vercel relay tasarlandı.
- Bu ortamın ağ politikası `vercel-hf-probe.vercel.app` host'una da izin vermiyor:
  `HTTP 403 — Host not in allowlist` (hem çıplak endpoint hem `/api/hf/submit`).
- `scripts/relay_api.py submit-batch` çalıştırıldı → `exit 3` (submit başarısız).

Bu yüzden `assets/gorseller/2026-05-18-sabah-9/slide-*.png` ve `outputs/.../raw/`
dosyaları **placeholder** — düz `#E63B5C` AHUDUDU zemin (Higgsfield watercolor
karakter illüstrasyonu YOK). `outputs/.../slide-*.png` final dosyaları bu
placeholder'lar üzerine metin/logo/dekorasyon bindirilerek üretildi; yerleşim
ve tipografi doğru, sadece boyalı karakter sanatı eksik.

**Gerçek görsellerle tamamlamak için:** relay host'u (`vercel-hf-probe.vercel.app`)
ağ allowlist'ine ekleyin VEYA ağ erişimi olan bir ortamdan şunu çalıştırın:

```bash
SLOT="2026-05-18-sabah-9"
BRANCH="claude/quirky-mendel-knlRU"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek-secret>" \
python3 scripts/relay_api.py submit-batch --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file /tmp/prompts.json
```

Relay PNG'leri `assets/gorseller/$SLOT/slide-N.png` yoluna commit'ledikten sonra
`python3 scripts/overlay_text.py layout.json` yeniden çalıştırılarak final
slide'lar gerçek illüstrasyonlarla üretilir (layout.json hazır).

## Caption

`caption.txt` — Instagram caption (samimi anne dili) + 20 hashtag.
