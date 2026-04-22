# Routine Prompt: Sincap Kitap IG — Sabah 09:00
# ANNE ODAKLI, SICAK EMPATİK TON

Sincap Kitap (0-6 yaş çocuk kitabı yayınevi) Instagram hesabı için sabah 09:00 carousel postu üret. Ton: ANNE ODAKLI, SICAK, EMPATİK, YARGISIZ.

## ADIM 1 — KONU SEÇİMİ

Aşağıdaki 0-6 yaş sorunlarından son 14 günde kullanılmamış olan bir konu seç:

seçici yeme, uyku direnci, tuvalet eğitimi, kardeş kıskançlığı, ekran bağımlılığı, öfke nöbetleri, ayrılık kaygısı, karanlık korkusu, yalan söyleme, paylaşmamak, diş fırçalamaya direnç, 3 yaş korku dönemi, inatlaşma, "hayır" dönemi, "neden" dönemi, banyoya direnç, kıyafet inadı, aşırı bağlılık, dikkat dağınıklığı, dil gelişimi, empati gelişimi, yemeği fırlatma, emzik/parmak bırakma, tuvalet kazaları.

**Tekrar kontrolü:** `logs/sabah-9.md` dosyasını oku. Son 14 günün konularını listele. Tekrar olmayan konu seç. Seçilen konuyu `logs/sabah-9.md` dosyasına bugünün tarihi ile ekle (format: `- 2026-04-19: ayrılık kaygısı`).

## ADIM 2 — METİN ÜRETİMİ (Türkçe, anne empati tonu)

5 slide'lık carousel metni yaz. Ton: "Yalnız değilsin" hissi, "...yapmalısınız" yerine "...deneyebilirsiniz".

- **Slide 1 KAPAK:** Dikkat çekici başlık (4-7 kelime) + alt başlık (5-8 kelime). Aksan kelime belirle (farklı renkte render edilecek). Örn başlık: "Anne, Beni Bırakma!" (aksan: "Bırakma!"). Alt başlık: "Ayrılık kaygısı, sevginin derin kanıtıdır."
- **Slide 2 TANIDIK SAHNE:** 2-3 cümle empatik betimleme. "Bu sahne tanıdık geliyor mu?"
- **Slide 3 ÇOCUĞUN SESİ:** Birinci ağızdan 1-2 cümlelik alıntı. Örn: "Seni göremeyince kalbim hızlı atıyor."
- **Slide 4 UNUTMAYIN:** "UNUTMAYIN!" başlığı + 3-4 satırlık sakin paragraf + 1 pratik mikro ipucu.
- **Slide 5 KAPANIŞ:** Motive edici 1-2 cümle + "Sincap Kitap'ı takip et 🐿️"

Her slide max 40 kelime.

Ayrıca üret:
- Instagram caption (400-500 kelime, samimi anne dili)
- 15-20 hashtag (#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik + konu spesifik)

## ADIM 3 — PALETTE SEÇİMİ

Konuya uygun TEK palette seç, 5 slide boyunca sabit kullan:

| Palette | Arka plan | Aksan | Metin |
|---|---|---|---|
| AHUDUDU | #E63B5C | #C5E86C yeşil | beyaz |
| MOR | #7E5BA0 | #C5E86C yeşil | beyaz |
| HARDAL | #F5C82E | #8E4FAA mor | koyu kahve |
| TURUNCU | #E97E28 | beyaz | koyu mor |
| TOZ MAVİSİ | #C9DDEC | #E97E28 turuncu | koyu kahve |
| MERCAN | #F08A7B | krem | koyu kahve |

Örnek eşleştirmeler: ayrılık kaygısı/korkular → MOR, merak/sorular → HARDAL, sıcak duygu → AHUDUDU, okul/kreş → TURUNCU, sakinlik/uyku → TOZ MAVİSİ.

## ADIM 4 — HIGGSFIELD GÖRSELLERİ (Vercel relay üzerinden)

> **Neden relay?** Higgsfield'ın Cloudflare WAF'ı Anthropic Routine IP'lerini blokluyor (403 host_not_allowed). Onun için Routine, Vercel'deki bir aracıya çağrı atar. Aracı, Higgsfield'a submit eder ve üretilen PNG'leri doğrudan bu repo'nun aktif branch'ine `assets/gorseller/<slot>/slide-<N>.png` yoluna commit'ler.

**Gerekli env (Routine secrets'te ayarlı olmalı — prompt içinde hardcode ETME):**
- `RELAY_URL` → örn. `https://vercel-hf-probe.vercel.app`
- `RELAY_SHARED_SECRET`

**Prompt iskeleti (her slide için, TEK STRING halinde):**
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute {KARAKTER} character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid {PALETTE_HEX} background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

**{KARAKTER}** konuya göre tek hayvan seç ve 5 slide'da aynı kalsın: mole (köstebek) / bear cub / kitten / little spider / baby squirrel / panda cub / fawn / hedgehog.

**{SAHNE} her slide için farklı:**
- Slide 1: "big character standing on a small hill, decorative leaves and stars around, looking hopeful"
- Slide 2: "character with mother/parent character, warm hugging interaction, cozy indoor scene"
- Slide 3: "small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up"
- Slide 4: "family scene, parent and child reading book together, warm cozy bedroom setting"
- Slide 5: "character waving goodbye, smiling, sitting on a book stack"

**Adım 4a — 5 prompt'u JSON olarak yaz:**

```bash
SLOT="{TARİH}-sabah-9"
BRANCH=$(git rev-parse --abbrev-ref HEAD)

python3 - <<'PY'
import json, os
slot = os.environ.get("SLOT") or "{TARİH}-sabah-9"
prompts = [
    # 5 prompt — her biri yukarıdaki iskelet + o slide'a özel sahne.
    # Aynı PALETTE_HEX ve aynı KARAKTER kullan.
    {"prompt": "Children's book illustration, ... solid #7E5BA0 background ... big character standing on a small hill, decorative leaves and stars around, looking hopeful",
     "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 2 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 3 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 4 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
    {"prompt": "... slide 5 sahnesi ...", "width_and_height": "1080x1350", "quality": "1080p"},
]
open("/tmp/prompts.json","w",encoding="utf-8").write(json.dumps(prompts, ensure_ascii=False))
print("wrote /tmp/prompts.json")
PY
```

**Adım 4b — Relay'e submit et ve görsellerin GitHub'a commit'lenmesini bekle:**

```bash
python3 scripts/relay_api.py submit-batch \
    --slot    "$SLOT" \
    --branch  "$BRANCH" \
    --prompts-file /tmp/prompts.json
```

Bu komut:
1. `/api/hf/submit`'e POST atar → relay 5 iş Higgsfield'a gönderir (webhook dahil).
2. Higgsfield her slide bittikçe `/api/hf/hook`'u çağırır → relay PNG'yi indirir ve `assets/gorseller/$SLOT/slide-N.png` yoluna branch'e commit'ler.
3. Script `/api/hf/status`'ı ~10s aralıkla poll eder; 5/5 hazır olunca exit 0.
4. Hata durumunda exit 3/4/5 döner ve routine durur.

**Adım 4c — Webhook commit'lerini local'e çek:**

```bash
git pull --ff-only origin "$BRANCH"
ls -la assets/gorseller/"$SLOT"/
# Beklenen: slide-1.png ... slide-5.png
```

## ADIM 5 — PYTHON PIL İLE METİN BİNDİRME

Bash üzerinden `scripts/overlay_text.py` scriptini çalıştır. Önce bir `layout.json` config dosyası hazırla:

```json
{
  "output_dir": "outputs/{TARİH}-sabah-9",
  "palette": {
    "bg": "#7E5BA0",
    "accent": "#C5E86C",
    "text": "#FFFFFF"
  },
  "slides": [
    {
      "raw_image": "assets/gorseller/{TARİH}-sabah-9/slide-1.png",
      "output": "outputs/{TARİH}-sabah-9/slide-1.png",
      "type": "cover",
      "title_main": "Anne, Beni",
      "title_accent": "Bırakma!",
      "subtitle": "Ayrılık kaygısı, sevginin derin kanıtıdır.",
      "decorations": true
    },
    {
      "raw_image": "assets/gorseller/{TARİH}-sabah-9/slide-2.png",
      "output": "outputs/{TARİH}-sabah-9/slide-2.png",
      "type": "inner",
      "body": "Annesinden ayrılırken ağlayan çocuğu görünce içiniz sıkışıyor. Bu sahne tanıdık geliyor mu?"
    },
    {
      "raw_image": "assets/gorseller/{TARİH}-sabah-9/slide-3.png",
      "output": "outputs/{TARİH}-sabah-9/slide-3.png",
      "type": "quote",
      "quote": "Seni göremeyince kalbim hızlı atıyor."
    },
    {
      "raw_image": "assets/gorseller/{TARİH}-sabah-9/slide-4.png",
      "output": "outputs/{TARİH}-sabah-9/slide-4.png",
      "type": "tip",
      "title_accent": "UNUTMAYIN!",
      "body": "Ayrılık kaygısı gelişimin bir parçası. Kısa ama net vedalar, güvenli bir geçişi kurar. Bugün: 'Seni saat 3'te alacağım' gibi somut bir söz verin."
    },
    {
      "raw_image": "assets/gorseller/{TARİH}-sabah-9/slide-5.png",
      "output": "outputs/{TARİH}-sabah-9/slide-5.png",
      "type": "cta",
      "body": "Bu süreçte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️"
    }
  ]
}
```

Sonra çalıştır:
```bash
python3 scripts/overlay_text.py layout.json
```

Script her slide için:
- Higgsfield görselini yükler
- Başlık metnini Bagel Fat One ile bindirir (aksan kelime farklı renkte)
- Alt metni Baloo 2 ile bindirir
- Sincap Kitap logosunu sol alta yerleştirir (130px yükseklik, 50px margin)
- Kapakta kompozisyonlu dekorasyonlar ekler (yıldız, yaprak, nokta)
- **YAPMAZ:** < > okları, slide noktaları, slide numarası eklemez

## ADIM 6 — ÇIKTI VE RAPOR

Kaydedilecek dosyalar (`outputs/{TARİH}-sabah-9/`):
- `slide-1.png` ... `slide-5.png` (final)
- `raw/slide-*-raw.png` (ham Higgsfield çıktıları)
- `caption.txt` (Instagram caption + hashtag'ler)
- `icerik.md` (konu, tüm metinler, palette, higgsfield prompt'lar)
- `layout.json` (kullanılan config)

**Rapor (markdown):**
- Seçilen konu
- Seçilen palette adı
- 5 görsel için dosya yolları
- Caption ilk 3 satırı

GitHub'a commit ve push et (Routine ortamında git credentials varsa). Commit mesajı: `"Sincap Kitap IG post: {TARİH} sabah 09:00 - {KONU}"`

## KISITLAR

- Türkçe, yargısız destekleyici dil
- Tıbbi/psikolojik tavsiye YOK, genel pedagojik ipucu
- 5 slide AYNI palette'te
- Tasarımda ok, nokta, slide numarası YOK
- Karakter çerçevesiz, doğrudan arka plan üzerinde
- Profesyonel boyalı kitap stili (Higgsfield watercolor/gouache)
- Sincap Kitap logosu sol altta
- 14 gün içinde konu tekrarı YOK
