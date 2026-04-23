# Routine Prompt: Sincap Kitap IG — İkindi 15:00
# ANNE ODAKLI, PEDAGOJİK İPUCU AĞIRLIKLI TON

Sincap Kitap (0-6 yaş çocuk kitabı yayınevi) Instagram hesabı için ikindi 15:00 carousel postu üret. Ton: SICAK ANNE + BİLGE ARKADAŞ — uygulanabilir pedagojik ipucu ağırlıklı.

## ADIM 1 — KONU SEÇİMİ

Gelişim ve davranış konularından son 14 günde kullanılmamış olanı seç:

duygu düzenleme, öfke yönetimi, sınır koyma, "hayır" öğretimi, özgüven, empati gelişimi, sosyal beceri, arkadaşlık kurma, paylaşma öğretimi, rutin oluşturma, uyku rutini, sabah rutini, ekran süresi yönetimi, aile zamanı, kitap okuma alışkanlığı, hayal gücü, dil gelişimi, motor beceri, yaratıcılık, sebat, dayanıklılık, başarısızlıkla başa çıkma, özür dileme kültürü, teşekkür etme, duygu adlandırma, korkularla başa çıkma, merak, cesaret, okul öncesi hazırlık.

**Tekrar kontrolü:**
1. `logs/ikindi-15.md` oku
2. Aynı gün `logs/sabah-9.md` ve `logs/ogle-12.md` dosyalarının son satırlarını da oku (aynı gün çakışmasın)
3. Tekrar olmayan konu seç
4. Logu güncelle (format: `- 2026-04-19: sınır koyma`)

## ADIM 2 — METİN ÜRETİMİ (Türkçe, bilge anne-arkadaş tonu)

- **Slide 1 KAPAK:** İlham veren veya meraklandıran başlık. Örn: "Çocukların Okulun İlk Günü Ne Hisseder?" / "4-6 Yaş Anaokuluna Başlangıç Süreci". Aksan kelime belirle.
- **Slide 2 ÇERÇEVE:** 2-3 cümle anne diliyle konu özeti.
- **Slide 3 ANAHTAR KAVRAM:** Tek kelime başlık (örn. "Merak" / "Cesaret" / "Güven") + 1-2 cümle açıklama.
- **Slide 4 UNUTMAYIN!:** Başlık + 3-4 satır + 1 somut mikro aktivite ("Bu akşam şunu deneyin:...").
- **Slide 5 KAPANIŞ:** "Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️"

Her slide max 40 kelime.

Ayrıca üret:
- Instagram caption (400-500 kelime, ikindi tonu yumuşak dil)
- 15-20 hashtag (+ #pedagoji #ebeveynlik)

## ADIM 3 — PALETTE SEÇİMİ

İkindi teması için TURUNCU / HARDAL / MERCAN / TOZ MAVİSİ tercih et (gün sonu sıcak hissi). Detay tabloya bak (routine-sabah-9.md).

## ADIM 4 — HIGGSFIELD GÖRSELLERİ (Vercel relay üzerinden)

> **Neden relay?** Higgsfield'ın Cloudflare WAF'ı Anthropic Routine IP'lerini blokluyor. Relay Vercel üstünde çalışır, Higgsfield'a submit eder, webhook geri dönünce PNG'leri bu branch'e `assets/gorseller/<slot>/slide-<N>.png` olarak commit'ler.

**Gerekli env (Routine UI'de bu prompt'u paste ederken ADIM 4b'deki `PLACEHOLDER_RELAY_SECRET` ifadesini Vercel'deki gerçek değerle değiştir):**
- `RELAY_URL` → `https://vercel-hf-probe.vercel.app` (sabit, inline yazılı)
- `RELAY_SHARED_SECRET` → Vercel → `vercel-hf-probe` → Env → `RELAY_SHARED_SECRET` değerini kopyala, prompt'a yapıştır.

**Prompt iskeleti (her slide için):**
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute {KARAKTER} character in rich scene, multiple storybook characters, large expressive eyes, rosy cheeks, warm painterly palette, solid {PALETTE_HEX} background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, portrait orientation, {SAHNE}
```

**{SAHNE}** ikindi postunda ZENGİN, KALABALIK sahneler:
- Slide 1: "central character on colorful background, 2-3 small side objects (pencil, book, music note)"
- Slide 2: "rich scene with multiple animal characters interacting in a setting (kindergarten classroom, music corner, art table, playground)"
- Slide 3: "scene representing abstract concept (curiosity = orchestra of animals discovering instruments; courage = small animal taking first step; confidence = animal looking in mirror)"
- Slide 4: "warm parent-child activity scene (cooking, reading, gardening, storytelling)"
- Slide 5: "character smiling and waving, surrounded by small books or warm objects"

**Adım 4a — 5 prompt'u JSON olarak yaz:**

```bash
SLOT="{TARİH}-ikindi-15"
BRANCH=$(git rev-parse --abbrev-ref HEAD)

python3 - <<'PY'
import json
prompts = [
    {"prompt": "Children's book illustration, ... solid #E97E28 background ... slide 1 sahnesi",
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

> Routine UI'ye paste ederken `PLACEHOLDER_RELAY_SECRET` ifadesini Vercel'deki gerçek `RELAY_SHARED_SECRET` değeriyle değiştir.

```bash
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="PLACEHOLDER_RELAY_SECRET" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
```

**Adım 4c — Commit'leri local'e çek:**

```bash
git pull --ff-only origin "$BRANCH"
ls -la assets/gorseller/"$SLOT"/
```

## ADIM 5 — PYTHON PIL METİN BİNDİRME

`scripts/overlay_text.py` ile. `layout.json` örneği:

```json
{
  "output_dir": "outputs/{TARİH}-ikindi-15",
  "palette": {"bg": "#E97E28", "accent": "#FFFFFF", "text": "#2A1810"},
  "slides": [
    {"raw_image": "assets/gorseller/{TARİH}-ikindi-15/slide-1.png", "output": ".../slide-1.png", "type": "cover",
     "title_main": "Çocukların Okulun İlk Günü", "title_accent": "Ne Hisseder?", "subtitle": "Yeni başlangıçlar küçük kalpleri nasıl etkiler.", "decorations": true},
    {"raw_image": "assets/gorseller/{TARİH}-ikindi-15/slide-2.png", "output": ".../slide-2.png", "type": "inner",
     "body": "İlk gün heyecan ve tedirginlik karışımı yaşar. Bu karmaşıklık tamamen doğaldır."},
    {"raw_image": "assets/gorseller/{TARİH}-ikindi-15/slide-3.png", "output": ".../slide-3.png", "type": "concept",
     "title_accent": "Merak", "body": "Yeni sınıfı, kitapları ve oyuncakları keşfetmek isterler."},
    {"raw_image": "assets/gorseller/{TARİH}-ikindi-15/slide-4.png", "output": ".../slide-4.png", "type": "tip",
     "title_accent": "UNUTMAYIN!", "body": "Anaokuluna alışma süreci her çocukta farklıdır. Biraz sabır ve anlayışla bu süreç hem çocuğunuz hem sizin için daha rahat geçer. Bu akşam: 'Bugün yeni ne öğrendin?' diye sorun."},
    {"raw_image": "assets/gorseller/{TARİH}-ikindi-15/slide-5.png", "output": ".../slide-5.png", "type": "cta",
     "body": "Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️"}
  ]
}
```

Çalıştır: `python3 scripts/overlay_text.py layout.json`

## ADIM 6 — ÇIKTI VE RAPOR

`outputs/{TARİH}-ikindi-15/`: slide-1.png..slide-5.png + caption.txt + icerik.md + raw/*.

GitHub push. Commit: `"Sincap Kitap IG post: {TARİH} ikindi 15:00 - {KONU}"`

**Rapor:** Konu + palette + 5 dosya yolu + caption ilk 3 satır.

## KISITLAR

- Türkçe, sıcak bilge anne dili
- Tıbbi tavsiye değil pedagojik ipucu
- 5 slide AYNI palette
- Tasarımda ok/nokta/sayı YOK
- Boyalı kitap stili illüstrasyon (flat vector YOK)
- Sincap Kitap logosu sol altta
- Aynı gün sabah/öğle postlarıyla konu çakışması YOK
- 14 gün içinde konu tekrarı YOK
