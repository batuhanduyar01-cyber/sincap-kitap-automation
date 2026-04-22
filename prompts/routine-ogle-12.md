# Routine Prompt: Sincap Kitap IG — Öğlen 12:00
# ÇOCUK ODAKLI, EĞLENCELİ, OYUNSU TON

Sincap Kitap (0-6 yaş çocuk kitabı yayınevi) Instagram hesabı için öğlen 12:00 carousel postu üret. Ton: ÇOCUK ODAKLI, EĞLENCELİ, OYUNSU — çocuklarla birlikte okunabilir.

## ADIM 1 — KONU SEÇİMİ

Çocuk perspektifinden ele alınacak durumlardan son 14 günde kullanılmamış olanı seç:

diş fırçalatmama, yatmayı istememe, oyuncak paylaşmama, banyo direnci, yemeği reddetme, karanlık korkusu, hayvan korkusu, kreşe gitmek istememe, "benim" dönemi, kıyafet inadı, sabırsızlık, sıra bekleyememe, kardeşle paylaşım, öfke patlaması, üzülünce vurma, çizgi film bitince ağlama, tablet isteme, yeni yemek denememe, "ben yaparım" ısrarı, utangaçlık, komşuya selam vermeme, kreş ilk günü, yeni kardeş gelişi, anne işe giderken ağlama.

**Tekrar kontrolü:** `logs/ogle-12.md` dosyasını oku. Tekrar olmayan konu seç. Seçilen konuyu logu güncelle (format: `- 2026-04-19: diş fırçalatmama`).

## ADIM 2 — METİN ÜRETİMİ (Türkçe, çocuk ağzından ALINTI AĞIRLIKLI)

5 slide metni yaz. Ton: Çocuğun iç sesinden alıntılarla ilerle.

- **Slide 1 KAPAK:** Çocuk ağzından sevimli başlık. Örn: "Bebekler Dünyayı Nasıl Keşfeder?" (aksan: "Nasıl Keşfeder?")
- **Slide 2 ÇOCUĞUN SESİ 1 (sevgi):** Birinci ağızdan alıntı. Örn: "Seninle oyun oynamak en sevdiğim şey."
- **Slide 3 ÇOCUĞUN SESİ 2 (ihtiyaç):** Birinci ağızdan alıntı. Örn: "Minik minik adımlar atabilirim ama kocaman bir dünyam var."
- **Slide 4 EBEVEYN NOTU:** "Ebeveyn Notu" başlığı + 2-3 cümle + 1 pratik ipucu.
- **Slide 5 KAPANIŞ:** Çocuktan veda + "Sincap Kitap'ı takip et 🐿️"

Her slide max 35 kelime.

Ayrıca üret:
- Instagram caption (300-400 kelime, "çocuğunuzla birlikte okuyun" çağrısı)
- 15-20 hashtag (#sincapkitap #çocukkitabı #resimlikitap #okulöncesi #06yaş + konu spesifik)

## ADIM 3 — PALETTE SEÇİMİ

Konuya uygun TEK palette seç, 5 slide boyunca sabit kullan (detay için sabah-9 dosyasındaki tabloya bak):

AHUDUDU #E63B5C / MOR #7E5BA0 / HARDAL #F5C82E / TURUNCU #E97E28 / TOZ MAVİSİ #C9DDEC / MERCAN #F08A7B

## ADIM 4 — HIGGSFIELD GÖRSELLERİ (Vercel relay üzerinden)

> **Neden relay?** Higgsfield'ın Cloudflare WAF'ı Anthropic Routine IP'lerini blokluyor (403 host_not_allowed). Relay, Vercel üzerinde çalışır; 5 prompt'u Higgsfield'a submit eder ve webhook geri dönünce PNG'leri bu branch'e `assets/gorseller/<slot>/slide-<N>.png` olarak commit'ler.

**Gerekli env (Routine secrets'te ayarlı):**
- `RELAY_URL` → `https://vercel-hf-probe.vercel.app`
- `RELAY_SHARED_SECRET`

**Prompt iskeleti (her slide için):**
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute {KARAKTER} character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid {PALETTE_HEX} background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, {SAHNE}
```

**{KARAKTER}:** Konu kahramanı olan sevimli hayvan (konuya göre seç, 5 slide'da aynı).

**{SAHNE} her slide farklı:**
- Slide 1: "character in dynamic expressive pose, matches topic, 5-8 decorative elements around (bubbles, leaves, sparkles)"
- Slide 2: "character with another character in warm loving interaction (hugging, playing, giggling)"
- Slide 3: "isolated character, small scale against vast background, emotional vulnerable pose"
- Slide 4: "calm adult-child scene, cozy bonding moment (reading book, eating, chatting)"
- Slide 5: "character waving goodbye, cheerful smile, standing next to small book stack"

**Adım 4a — 5 prompt'u JSON olarak yaz:**

```bash
SLOT="{TARİH}-ogle-12"
BRANCH=$(git rev-parse --abbrev-ref HEAD)

python3 - <<'PY'
import json
prompts = [
    {"prompt": "Children's book illustration, ... solid #F5C82E background ... slide 1 sahnesi",
     "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 2 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 3 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 4 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 5 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
]
open("/tmp/prompts.json","w",encoding="utf-8").write(json.dumps(prompts, ensure_ascii=False))
PY
```

**Adım 4b — Submit + poll:**

```bash
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
```

Script 5/5 PNG commit'lenene kadar bekler (~2-5 dk). Hatalı exit: 3 (submit fail) / 4 (timeout) / 5 (webhook permanent error).

**Adım 4c — Commit'leri local'e çek:**

```bash
git pull --ff-only origin "$BRANCH"
ls -la assets/gorseller/"$SLOT"/
```

## ADIM 5 — PYTHON PIL İLE METİN BİNDİRME

`scripts/overlay_text.py` kullan. `layout.json` örneği:

```json
{
  "output_dir": "outputs/{TARİH}-ogle-12",
  "palette": {
    "bg": "#F5C82E",
    "accent": "#8E4FAA",
    "text": "#3D2817"
  },
  "slides": [
    {"raw_image": "assets/gorseller/{TARİH}-ogle-12/slide-1.png", "output": ".../slide-1.png", "type": "cover",
     "title_main": "Bebekler Dünyayı", "title_accent": "Nasıl Keşfeder?", "subtitle": "Her dokunuş yeni bir macera.", "decorations": true},
    {"raw_image": "assets/gorseller/{TARİH}-ogle-12/slide-2.png", "output": ".../slide-2.png", "type": "quote",
     "quote": "Seninle oyun oynamak en sevdiğim şey."},
    {"raw_image": "assets/gorseller/{TARİH}-ogle-12/slide-3.png", "output": ".../slide-3.png", "type": "quote",
     "quote": "Minik minik adımlar atabilirim ama kocaman bir dünyam var."},
    {"raw_image": "assets/gorseller/{TARİH}-ogle-12/slide-4.png", "output": ".../slide-4.png", "type": "tip",
     "title_accent": "Ebeveyn Notu", "body": "Çocuğunuz her şeye dokunarak öğrenir. Güvenli alan tanıyın, merakı söndürmeyin."},
    {"raw_image": "assets/gorseller/{TARİH}-ogle-12/slide-5.png", "output": ".../slide-5.png", "type": "cta",
     "body": "Sincap'ın maceralarının tamamı için Sincap Kitap'ı takip et 🐿️"}
  ]
}
```

Çalıştır: `python3 scripts/overlay_text.py layout.json`

## ADIM 6 — ÇIKTI VE RAPOR

`outputs/{TARİH}-ogle-12/` klasörüne: slide-1.png..slide-5.png + caption.txt + icerik.md + raw/*.

GitHub push. Commit: `"Sincap Kitap IG post: {TARİH} öğle 12:00 - {KONU}"`

**Rapor:** Konu + palette + 5 dosya yolu + caption ilk 3 satır.

## KISITLAR

- Türkçe, çocuk dostu dil, alıntılar birinci ağızdan
- 5 slide AYNI palette
- Tasarımda ok/nokta/sayı YOK
- Çerçevesiz karakter, boyalı kitap stili
- Sincap Kitap logosu sol altta sabit
- 14 gün içinde konu tekrarı YOK
