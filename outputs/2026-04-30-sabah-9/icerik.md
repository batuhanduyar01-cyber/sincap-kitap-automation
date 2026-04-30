# Sincap Kitap IG — 2026-04-30 Sabah 09:00

## Konu
**Kardeş kıskançlığı** (0-6 yaş, anne odaklı sıcak empatik ton)

## Palette
**AHUDUDU**
- bg: `#E63B5C`
- accent: `#C5E86C` (yeşil)
- text: `#FFFFFF`

## Karakter
Yavru ayı (bear cub) — 5 slide boyunca aynı.

## Slide Metinleri

### Slide 1 — KAPAK
- **Title (main):** Ben de Buradayım
- **Title (accent):** Anne!
- **Subtitle:** Kardeş kıskançlığı, sevilmeye duyulan açlıktır.

### Slide 2 — TANIDIK SAHNE
> Yeni doğan kardeş kucağınızdayken büyük çocuğun gözündeki o tanıdık gölge... Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "O gelince herkes onu seviyor. Ya ben, anne?"

### Slide 4 — UNUTMAYIN!
**UNUTMAYIN!**

Kardeş kıskançlığı sevgi rekabeti değil, yer arayışıdır. Büyük çocuğunuz kalbinizdeki yerini hâlâ arıyor olabilir. Bugün: günde 10 dakika sadece ona ait, telefonsuz bir 'ikimizin zamanı' yaratabilirsiniz.

### Slide 5 — KAPANIŞ
> Bu yolculukta kalbine eşlik edecek hikayeler için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (5 adet)

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette,
solid #E63B5C background, Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

Sahneler:
1. big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful
2. older bear cub watching as mother bear gently holds a tiny newborn baby bear, slightly sad longing expression on the older cub, cozy warm indoor scene
3. small isolated bear cub, emotional vulnerable pose looking up, vast empty space around with subtle scale contrast, single tear shimmering
4. warm family scene of mother bear cuddling older cub and baby cub together, all three reading a picture book, cozy bedroom setting
5. bear cub waving goodbye, smiling brightly, sitting on a small stack of colorful books

Boyut: `1152x1536`, kalite: `1080p`.

## ⚠️ Higgsfield Üretimi Hakkında Önemli Not

Bu çalıştırmada Higgsfield illüstrasyonları **üretilemedi**. Vercel relay
(`https://vercel-hf-probe.vercel.app`) çağrısı `HTTP 403 "Host not in allowlist"`
ile reddedildi: routine prompt'undaki `RELAY_SHARED_SECRET` placeholder hash'i
(`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`) Vercel'deki
gerçek secret değeriyle eşleşmiyor.

`assets/gorseller/2026-04-30-sabah-9/slide-1.png ... slide-5.png` dosyaları
**düz #E63B5C arka plan placeholder PNG'leri**dir (1152x1536). Bunlar overlay
tarafından final dosyalara dönüştürüldüğünden caption ve metin tasarımı tamamen
hazır; ancak watercolor karakter illüstrasyonları yoktur.

### Çalıştırmayı tamamlamak için
1. Vercel dashboard → Project `vercel-hf-probe` → Settings → Environment Variables → `RELAY_SHARED_SECRET` değerini al.
2. Aşağıdaki komutu o gerçek değerle çalıştır:

```bash
cd /home/user/sincap-kitap-automation
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<GERÇEK_SECRET>" \
SLOT="2026-04-30-sabah-9" \
BRANCH="claude/quirky-mendel-XnQJo" \
python3 scripts/relay_api.py submit-batch \
    --slot    "$SLOT" \
    --branch  "$BRANCH" \
    --prompts-file /tmp/prompts.json
```

3. Webhook 5 PNG'yi commit'leyince `git pull --ff-only origin claude/quirky-mendel-XnQJo` ve `python3 scripts/overlay_text.py outputs/2026-04-30-sabah-9/layout.json` ile final slide'lar yeniden render edilir.

`/tmp/prompts.json` bu çalıştırmadan kalmış olabilir; yoksa yukarıdaki sahnelerden tekrar üretilebilir.

## Çıktı Dosyaları

```
outputs/2026-04-30-sabah-9/
├── slide-1.png            # final (placeholder bg + overlay metin)
├── slide-2.png
├── slide-3.png
├── slide-4.png
├── slide-5.png
├── raw/
│   ├── slide-1-raw.png    # düz #E63B5C placeholder (Higgsfield yok)
│   ├── slide-2-raw.png
│   ├── slide-3-raw.png
│   ├── slide-4-raw.png
│   └── slide-5-raw.png
├── caption.txt            # Instagram caption + 20 hashtag
├── icerik.md              # bu dosya
└── layout.json            # overlay config
```

## Caption İlk 3 Satır

```
"Anne, ben de buradayım..." 🐻💞

Bazen bir bakış yetiyor. Yeni doğan kardeşi kucağınızda iken büyük çocuğunuzun gözünde beliren o ince gölge, kalbinizi sıkıştırıyor. "Ben fark edilmedim mi?" diyen sessiz bir bakış. Bu yazıyı, o gölgeyi tanıyan her anneye yazıyoruz: yalnız değilsin.
```
