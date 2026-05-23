# Sincap Kitap IG — 2026-05-23 Öğle 12:00

## Konu
**Karanlık korkusu** (çocuk perspektifinden, alıntı ağırlıklı)

## Palette
- Arka plan: **MOR #7E5BA0**
- Aksan: **HARDAL #F5C82E**
- Metin: **KREM #FFF7E0**

## Karakter
Minik krem renkli tavşan (5 slide boyunca aynı, uzun sarkık kulaklar, büyük ifadeli gözler, kırmızı yanaklar)

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** "Karanlık"
- **Aksan:** "Korkutmuyor Beni"
- **Alt başlık:** "Çünkü kalbimde minik bir ışık var."
- **Sahne:** Tavşan elinde minik sarı fener tutuyor, cesur bir poz, etrafında yıldız ve ateş böcekleri.

### Slide 2 — ÇOCUĞUN SESİ (sevgi)
> "Elimi tuttuğunda gece bile sıcacık oluyor."

Sahne: Tavşan, daha büyük yumuşak bir ebeveyn tavşan tarafından sarılıyor; yıldızlı bir battaniye altında, birlikte kıkırdıyorlar.

### Slide 3 — ÇOCUĞUN SESİ (ihtiyaç)
> "Bazen küçücük bir lambacık, kocaman bir cesarettir."

Sahne: Küçücük tavşan kocaman bir odanın içinde tek başına oturuyor, yorganın altından bakıyor; savunmasız ama meraklı.

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**

Çocuklar karanlığı bilmediği için korkar. Odaya birlikte "iyi geceler" deyin, küçük bir gece lambası bırakın, korkuyu masallarla tanıdık kılın.

Sahne: Ebeveyn ve yavru tavşan yatakta birlikte masal kitabı okuyor, yumuşak başucu lambası sıcacık parlıyor.

### Slide 5 — KAPANIŞ
"Tatlı rüyalar dostum! Bir sonraki masal için Sincap Kitap'ı takip et 🐿️"

Sahne: Tavşan minik bir mumla el sallıyor, yanında küçük bir kitap yığını.

## Dosyalar
- `outputs/2026-05-23-ogle-12/slide-1.png` .. `slide-5.png`
- `outputs/2026-05-23-ogle-12/caption.txt`
- `outputs/2026-05-23-ogle-12/raw/slide-1.png` .. `slide-5.png` (ham arka planlar)
- `outputs/2026-05-23-ogle-12/layout.json`

## ⚠️ Görsel Üretim Notu

Routine ortamının dış ağ allowlist'i `vercel-hf-probe.vercel.app` adresini
içermediği için Higgsfield relay'ine ulaşılamadı (`403 host_not_allowed`).
Tüm görsel üretim host'ları (higgsfield, replicate, fal, openai, stability,
pollinations) aynı şekilde blokludur.

**Mevcut raw görseller painterly fallback arka planlardır** (PIL ile üretildi:
mor zemin + yumuşak ışık lekeleri + dekoratif yıldız/parıltılar). Tavşan
karakteri içermez. Görsel kimliği korumak için palette, dekorasyon yoğunluğu
ve sahne atmosferi prompt'lardaki kompozisyona göre ayarlandı.

**Karakter illüstrasyonlarını eklemek için:** ortamın allowlist'ine
`vercel-hf-probe.vercel.app` (veya direkt Higgsfield) eklendiğinde
`/tmp/prompts.json` zaten yazılmış durumda — sadece `relay_api.py
submit-batch` komutunu tekrar çalıştırmak yeterli. Sonra `overlay_text.py`
mevcut `layout.json` ile aynı çıktıları üretir.
