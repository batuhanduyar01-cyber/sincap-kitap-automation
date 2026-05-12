# Sincap Kitap IG — Öğle 12:00 — 2026-05-12

## Özet
- **Tarih:** 2026-05-12
- **Slot:** öğle 12:00
- **Konu:** diş fırçalatmama
- **Ton:** ÇOCUK ODAKLI, EĞLENCELİ, OYUNSU
- **Karakter:** tilki yavrusu (fox cub) — 5 slide boyunca sabit
- **Palette:** HARDAL — bg `#F5C82E` / aksan `#8E4FAA` / metin `#3D2817`

## 5 Slide Metinleri

### Slide 1 — KAPAK
- title_main: **Fırçayı Görünce**
- title_accent: **Saklanıyorum!**
- subtitle: Köpük, fısıltı, biraz da kahkaha...

### Slide 2 — ÇOCUĞUN SESİ (sevgi)
> "Sen yanımdayken fırçam bile yumuşacık oluyor."

### Slide 3 — ÇOCUĞUN SESİ (ihtiyaç)
> "Köpüğün tadı tuhaf; biraz şarkı söylesek olmaz mı?"

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**
Fırçalama bir savaş değil, küçük bir ritüel. Aynı saat, aynı şarkı. Bugün önce kendi dişinizi çocuğunuza fırçalatın — taklit, sözden güçlüdür.

### Slide 5 — KAPANIŞ
Yarın yine birlikte fırçalayalım! Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (5/5)

Tüm prompt'lar 1152x1536, quality 1080p. Ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute little fox cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F5C82E background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, no borders, portrait orientation, **{SAHNE}**

- **Slide 1:** fox cub peeking from behind a giant friendly toothbrush, surprised playful pose, decorative elements around (foam bubbles, sparkles, tiny stars, dots), 6 decorative items scattered
- **Slide 2:** fox cub with parent fox character in warm loving interaction, hugging while holding tiny toothbrushes together, giggling, cozy bathroom scene
- **Slide 3:** isolated tiny fox cub, small scale against vast background, emotional vulnerable pose, sitting next to an enormous toothbrush, looking up curiously, lots of empty space
- **Slide 4:** calm parent fox and fox cub cozy bonding moment, brushing teeth together in front of a small round mirror, warm soft glow, chatting
- **Slide 5:** fox cub waving goodbye, cheerful smile, holding a tiny toothbrush, standing next to a small stack of books

`prompts.json` dosyası bu klasörde — relay'e gönderime hazır.

## ⚠️ Önemli — Raw Görseller Placeholder

Bu çalıştırmada **Higgsfield illüstrasyonları üretilemedi**:

- Vercel relay (`https://vercel-hf-probe.vercel.app`) bu sandbox'un IP'sini allowlist dışı bularak `403 "Host not in allowlist"` döndürdü (hem `/api/hf/submit` hem `/api/hf/status` için).
- Doğrudan Higgsfield (`platform.higgsfield.ai`) da Anthropic Routine WAF bloğu nedeniyle `403` döndürüyor.

Bu yüzden `assets/gorseller/2026-05-12-ogle-12/slide-{1..5}.png` ve `outputs/.../raw/slide-{1..5}-raw.png` **#F5C82E düz arka planlı placeholder PNG'lerdir**. Overlay + caption + metin tasarımı tamamlanıp `outputs/2026-05-12-ogle-12/slide-{1..5}.png` üretildi, dolayısıyla layout doğrulanabilir.

### Görselleri Üretmek İçin Yapılacak

Routine UI'den (allowlist'te olan ortamdan) aşağıyı koş ve `git pull` ile çek:

```bash
SLOT="2026-05-12-ogle-12"
BRANCH="claude/confident-dijkstra-FcDN6"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<GERÇEK_DEĞER>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-12-ogle-12/prompts.json
```

Relay 5/5 PNG'yi `assets/gorseller/$SLOT/slide-{1..5}.png` yoluna commit'ledikten sonra:

```bash
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-12-ogle-12/layout.json
```

## Caption / Hashtag
Bkz. `caption.txt`.

## Dosyalar
- `slide-1.png` … `slide-5.png` — overlay'li final (placeholder raw üzerine yazılı)
- `raw/slide-1-raw.png` … `raw/slide-5-raw.png` — placeholder ham
- `caption.txt` — Instagram caption + 20 hashtag
- `layout.json` — overlay konfigürasyonu
- `prompts.json` — Higgsfield için 5 prompt (relay submit için hazır)
- `icerik.md` — bu rapor
