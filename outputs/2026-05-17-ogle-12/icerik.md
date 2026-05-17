# Sincap Kitap IG — Öğle 12:00 — 2026-05-17

## Konu
**diş fırçalatmama** (çocuğun diş fırçalamaya direnç göstermesi)

Ton: çocuk odaklı, eğlenceli, oyunsu — çocukla birlikte okunabilir, alıntı ağırlıklı.

## Palette
**HARDAL**
- Arka plan (bg): `#F5C82E`
- Aksan (accent): `#8E4FAA` (mor)
- Metin (text): `#3D2817` (koyu kahve)

Konu-palette eşleştirmesi: diş fırçalama neşeli, enerjik ve oyunsu bir konu;
HARDAL'ın güneşli sarısı bu eğlenceli tonu taşıyor.

## Karakter
Konunun kahramanı: **sevimli yavru timsah** (baby crocodile) — dişleriyle ünlü,
diş fırçalama temasına oyunsu biçimde bağlanıyor. 5 slide boyunca aynı karakter.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): "Fırça Geliyor,"
- Başlık (aksan): "Ben Kaçıyorum!"
- Alt başlık: "Ama köpükler beni gıdıklayınca bayılıyorum."

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Diş fırçam minik bir sihirli değnek; ağzımda köpükten yıldızlar parlatıyor."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Bazen fırça bana garip geliyor, kaçmak istiyorum. Elimi tutup şarkı söylersen korkum köpük gibi uçup gidiyor."

### Slide 4 — EBEVEYN NOTU
- Başlık: "Ebeveyn Notu"
- Metin: "Diş fırçalamak bir görev değil, paylaşılan bir oyun olabilir. Direnç çoğu zaman korkudan değil, kontrol isteğinden doğar. İpucu: Fırçayı çocuğa seçtirin, birlikte 'köpük şarkısı' söyleyip iki dakika sayın."

### Slide 5 — KAPANIŞ
- Metin: "Bugün dişlerimi pırıl pırıl yaptım, sıra sende! Daha çok eğlenceli macera için Sincap Kitap'ı takip et 🐿️"
- Not: 🐿️ emojisi caption'da kalır; slide görselinde font emoji glyph'i içermediği için bindirilmez.

## Higgsfield Görsel Prompt'ları

Ortak iskelet (her slide): watercolor gouache, textured brush strokes,
cute baby crocodile, large expressive eyes, rosy blush cheeks,
solid `#F5C82E` background, Marc Boutavant + Oliver Jeffers style,
storybook art, no text, no frames, portrait orientation.

- **Slide 1:** baby crocodile in dynamic playful pose holding a toothbrush, joyful giggling, 5-8 decorative elements around (soap bubbles, sparkles, tiny stars)
- **Slide 2:** baby crocodile hugging and playing with a friendly smiling toothbrush character, warm loving interaction, foamy bubbles around
- **Slide 3:** isolated baby crocodile, small scale against vast empty background, peeking shyly, emotional vulnerable pose
- **Slide 4:** parent crocodile and baby crocodile brushing teeth together in a cozy bathroom, gentle bonding moment
- **Slide 5:** baby crocodile waving goodbye with a cheerful smile showing clean sparkly teeth, next to a small book stack

Tam prompt'lar: `raw/higgsfield-prompts.json`

## Caption
`caption.txt` — 300-400 kelime + 20 hashtag. "Çocuğunuzla birlikte okuyun" çağrısı içeriyor.

## ÜRETİM NOTU — Görseller (ÖNEMLİ)

Bu çalışmada Higgsfield watercolor illüstrasyonları **üretilemedi**.

- ADIM 4'teki Vercel relay'e (`vercel-hf-probe.vercel.app`) erişim,
  bu Routine ortamının ağ politikası tarafından engellendi:
  `HTTP 403 — Host not in allowlist`.
- Aynı engel Higgsfield için de geçerli (`higgsfield.ai` → 403).
- `relay_api.py submit-batch` submit aşamasında exit 3 ile durdu;
  Higgsfield'a hiçbir iş gönderilmedi.

**Çözüm:** Ortamın ağ politikası allowlist'ine `vercel-hf-probe.vercel.app`
host'u eklenmeli. Sonra bu Routine yeniden çalıştırılınca gerçek görseller
`outputs/.../raw/` altına gelir ve `overlay_text.py` yeniden çalıştırılır.

**Bu çalışmadaki görseller:** `raw/slide-1..5.png` dosyaları, doğru HARDAL
palette ile üretilmiş **placeholder (geçici) arka planlardır** — metin
yerleşimi, font ve kompozisyon önizlemesi içindir. Higgsfield'ın boyalı
kitap stili yavru timsah illüstrasyonlarının yerini tutmaz.
