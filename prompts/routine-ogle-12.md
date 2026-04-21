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

## ADIM 4 — HIGGSFIELD İLE İLLÜSTRASYONLAR (5 görsel, HTTP API)

Bu Routine'de MCP tool yok — `scripts/higgsfield_api.py` helper'ı kullan.

**Credentials:**
```bash
export HIGGSFIELD_API_KEY="b0ce4df9-80ac-44a3-8f9d-be0869a428e1"
export HIGGSFIELD_API_SECRET="be73a38e07e4faebd09666eb51d1fe04eea7feea96d83b81ca4640d33531e35c"
```

**Ortak parametreler:**
- `--aspect-ratio 4:5`
- `--resolution 1080p`
- `--quality high`
- `--reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"`

**Prompt iskeleti:**
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

**Bash çağrısı (örnek — slide 1):**
```bash
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute kitten character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F5C82E background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, character in dynamic expressive pose, matches topic, 5-8 decorative elements around" \
  --output "outputs/{TARİH}-ogle-12/raw/slide-1-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"
```

5 slide için 5 kez çağır. Her biri `outputs/{TARİH}-ogle-12/raw/slide-{N}-raw.png` olarak kaydedilir.

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
    {"raw_image": "...raw/slide-1-raw.png", "output": ".../slide-1.png", "type": "cover",
     "title_main": "Bebekler Dünyayı", "title_accent": "Nasıl Keşfeder?", "subtitle": "Her dokunuş yeni bir macera.", "decorations": true},
    {"raw_image": "...raw/slide-2-raw.png", "output": ".../slide-2.png", "type": "quote",
     "quote": "Seninle oyun oynamak en sevdiğim şey."},
    {"raw_image": "...raw/slide-3-raw.png", "output": ".../slide-3.png", "type": "quote",
     "quote": "Minik minik adımlar atabilirim ama kocaman bir dünyam var."},
    {"raw_image": "...raw/slide-4-raw.png", "output": ".../slide-4.png", "type": "tip",
     "title_accent": "Ebeveyn Notu", "body": "Çocuğunuz her şeye dokunarak öğrenir. Güvenli alan tanıyın, merakı söndürmeyin."},
    {"raw_image": "...raw/slide-5-raw.png", "output": ".../slide-5.png", "type": "cta",
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
