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

## ADIM 4 — HIGGSFIELD İLLÜSTRASYONLAR (5 görsel)

`higgsfield_soul_text_to_image`: aspect_ratio "4:5", resolution "1080p", quality "high", master karakter reference.

**Prompt iskeleti:**
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute {KARAKTER} character in rich scene, multiple storybook characters, large expressive eyes, rosy cheeks, warm painterly palette, solid {PALETTE_HEX} background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, portrait orientation, {SAHNE}
```

**{SAHNE}** ikindi postunda ZENGİN, KALABALIK sahneler:
- Slide 1: "central character on colorful background, 2-3 small side objects (pencil, book, music note)"
- Slide 2: "rich scene with multiple animal characters interacting in a setting (kindergarten classroom, music corner, art table, playground)"
- Slide 3: "scene representing abstract concept (curiosity = orchestra of animals discovering instruments; courage = small animal taking first step; confidence = animal looking in mirror)"
- Slide 4: "warm parent-child activity scene (cooking, reading, gardening, storytelling)"
- Slide 5: "character smiling and waving, surrounded by small books or warm objects"

Görselleri indir: `outputs/{TARİH}-ikindi-15/raw/slide-{N}-raw.png`

## ADIM 5 — PYTHON PIL METİN BİNDİRME

`scripts/overlay_text.py` ile. `layout.json` örneği:

```json
{
  "output_dir": "outputs/{TARİH}-ikindi-15",
  "palette": {"bg": "#E97E28", "accent": "#FFFFFF", "text": "#2A1810"},
  "slides": [
    {"raw_image": "...raw/slide-1-raw.png", "output": ".../slide-1.png", "type": "cover",
     "title_main": "Çocukların Okulun İlk Günü", "title_accent": "Ne Hisseder?", "subtitle": "Yeni başlangıçlar küçük kalpleri nasıl etkiler.", "decorations": true},
    {"raw_image": "...raw/slide-2-raw.png", "output": ".../slide-2.png", "type": "inner",
     "body": "İlk gün heyecan ve tedirginlik karışımı yaşar. Bu karmaşıklık tamamen doğaldır."},
    {"raw_image": "...raw/slide-3-raw.png", "output": ".../slide-3.png", "type": "concept",
     "title_accent": "Merak", "body": "Yeni sınıfı, kitapları ve oyuncakları keşfetmek isterler."},
    {"raw_image": "...raw/slide-4-raw.png", "output": ".../slide-4.png", "type": "tip",
     "title_accent": "UNUTMAYIN!", "body": "Anaokuluna alışma süreci her çocukta farklıdır. Biraz sabır ve anlayışla bu süreç hem çocuğunuz hem sizin için daha rahat geçer. Bu akşam: 'Bugün yeni ne öğrendin?' diye sorun."},
    {"raw_image": "...raw/slide-5-raw.png", "output": ".../slide-5.png", "type": "cta",
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
