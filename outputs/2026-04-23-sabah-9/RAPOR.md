# Rapor — Sincap Kitap IG Sabah 09:00 (2026-04-23)

## ⚠️ Sandbox Kısıtı — Higgsfield API Bloke

Routine bu seferinde **Higgsfield API'ye ulaşamadı**: sandbox HTTP çıkışı bir host-allowlist ile sınırlı ve `platform.higgsfield.ai` listede değil.

```
[higgsfield_api] POST https://platform.higgsfield.ai/v1/text2image/soul
[higgsfield_api] HTTP 403 Forbidden — Host not in allowlist
```

**Sonuç:** Final slide'lar gerçek watercolor illüstrasyonlar yerine TOZ MAVİSİ solid arka planlı **placeholder raw'lar** üzerine bindirildi (metin + dekorasyon + logo akışı bozulmasın diye). Layout, tipografi, palette ve kompozisyon **tam şekilde** önizlenebilir.

**Çözüm (elle):** Aşağıdaki 5 komutu, Higgsfield'ın erişilebildiği bir makinede sırayla çalıştırın; sonra `overlay_text.py`'yi tekrar çağırın.

```bash
export HIGGSFIELD_API_KEY="b0ce4df9-80ac-44a3-8f9d-be0869a428e1"
export HIGGSFIELD_API_SECRET="be73a38e07e4faebd09666eb51d1fe04eea7feea96d83b81ca4640d33531e35c"

# Slide 1
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, big bear cub standing on a small hill at night, decorative stars and little clouds around, looking hopeful, soft moonlight" \
  --output "outputs/2026-04-23-sabah-9/raw/slide-1-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"

# Slide 2
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, bear cub with mother bear, warm hugging interaction, cozy bedroom scene with pillow" \
  --output "outputs/2026-04-23-sabah-9/raw/slide-2-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"

# Slide 3
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, small isolated bear cub in pajamas, emotional vulnerable pose, vast empty room around (scale contrast), looking up with wide eyes" \
  --output "outputs/2026-04-23-sabah-9/raw/slide-3-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"

# Slide 4
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, bear cub family scene, parent bear and cub reading book together on bed, warm cozy bedroom setting, lamp glow" \
  --output "outputs/2026-04-23-sabah-9/raw/slide-4-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"

# Slide 5
python3 scripts/higgsfield_api.py \
  --prompt "Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, bear cub waving goodbye, smiling softly, sitting on a stack of storybooks" \
  --output "outputs/2026-04-23-sabah-9/raw/slide-5-raw.png" \
  --aspect-ratio 4:5 --resolution 1080p --quality high \
  --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"

# Sonra metinleri yeniden bindir:
python3 scripts/overlay_text.py outputs/2026-04-23-sabah-9/layout.json
```

---

## Seçilen Konu
**Uyku Direnci** (0-6 yaş çocuklarda yatma vakti direnci, uykuya geçişte zorluk)

Son 14 günde kullanılmamış. `logs/sabah-9.md` güncellendi (`- 2026-04-23: uyku direnci`).

## Seçilen Palette
**TOZ MAVİSİ** — sakinlik/uyku teması ile doğrudan eşleşir
- bg `#C9DDEC`, accent `#E97E28` (turuncu), text `#4A2E1A` (koyu kahve)

## Karakter
**Bear cub** (ayı yavrusu) — 5 slide'da sabit

## 5 Görsel — Dosya Yolları
- `outputs/2026-04-23-sabah-9/slide-1.png` — Kapak: "Anne, Uykum Gelmiyor!"
- `outputs/2026-04-23-sabah-9/slide-2.png` — Tanıdık sahne
- `outputs/2026-04-23-sabah-9/slide-3.png` — Çocuğun sesi (alıntı)
- `outputs/2026-04-23-sabah-9/slide-4.png` — UNUTMAYIN! + mikro ipucu
- `outputs/2026-04-23-sabah-9/slide-5.png` — Kapanış + CTA

Ham Higgsfield çıktıları (bu seferinde placeholder): `outputs/2026-04-23-sabah-9/raw/slide-*-raw.png`

## Caption — İlk 3 Satır
```
Her akşam aynı sahne. Pijaması giyili, dişi fırçalı, ışıklar kısılmış… Ama o hâlâ bir bahane bulur: "Bir bardak su daha alabilir miyim?", "Bir öpücük daha", "Sadece bir kitap daha anne…" 🌙

Sen de yorgun, o da yorgun. Sanki uyku ikinize de küsmüş gibi. İçinden "Ne yapıyorum yanlış?" diye soruyorsun. Cevap: Hiçbir şey.

🐿️ Uyku direnci, inatlaşma değildir.
```

Caption + 20 hashtag tamamı: `outputs/2026-04-23-sabah-9/caption.txt`

## Üretilen Dosyalar
```
outputs/2026-04-23-sabah-9/
├── RAPOR.md                   # bu dosya
├── icerik.md                  # konu + tüm metinler + Higgsfield promptları
├── layout.json                # overlay_text.py config
├── caption.txt                # IG caption + 20 hashtag
├── slide-1.png … slide-5.png  # final carousel görselleri
└── raw/
    ├── slide-1-raw.png        # placeholder (Higgsfield re-run gerekli)
    ├── slide-2-raw.png
    ├── slide-3-raw.png
    ├── slide-4-raw.png
    └── slide-5-raw.png
```

## Kısıtlara Uyum
- [x] Türkçe, yargısız destekleyici dil
- [x] Tıbbi tavsiye yok — pedagojik ipuçları
- [x] 5 slide aynı palette
- [x] Ok/slide numarası/slide noktası YOK
- [x] Sincap Kitap logosu sol altta
- [x] 14 gün içinde konu tekrarı YOK
- [ ] Higgsfield watercolor illüstrasyonları — **sandbox ağ kısıtı nedeniyle yukarıdaki 5 komutla tekrar çalıştırılmalı**
