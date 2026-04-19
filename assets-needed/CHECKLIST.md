# Asset Checklist — Routine'ler Çalışmadan Önce Hazırlanacaklar

GitHub repo'sunda `assets/` klasörü altında şu dosyalar bulunmalı:

## 1. logo.png

**Nerede:** `assets/logo.png`

**Ne:** Sincap Kitap baykuş logosu (gözlüklü kahverengi baykuş + altında "SİNCAP KİTAP" yazısı)

**Nasıl:**
- Transparan arka plan (PNG)
- ~400x400 veya daha büyük (script 140px'e yeniden boyutlandıracak)
- Mevcut dijital dosyadan kullan veya vektörden PNG export et

## 2. character-reference.png

**Nerede:** `assets/character-reference.png`

**Ne:** Sincap maskotunun "master" referans görseli. Higgsfield her slide üretirken bu referansı kullanacak → tüm postlarda aynı karakter stili.

**Nasıl:**

Claude Code CLI'da veya tek seferlik bir sohbette şu prompt'u çalıştır:

```
higgsfield_soul_text_to_image ile tek karakter referansı üret:

prompt: "Cute brown baby squirrel character mascot with large round glasses, children's book style, watercolor gouache painting, soft textured brush strokes, large expressive eyes, rosy blush cheeks, friendly warm smile, standing front-facing portrait pose, solid cream background, Oliver Jeffers and Marc Boutavant illustration style, storybook art, no text, painterly shading, high detail, clean edges"

aspect_ratio: "1:1"
resolution: "1080p"
quality: "high"
```

Çıkan görseli `character-reference.png` olarak repo'ya ekle. Bu URL'i 3 routine prompt'unda `reference_image_urls` alanına yaz.

## 3. Fontlar

**Nerede:** `assets/fonts/BagelFatOne-Regular.ttf` ve `assets/fonts/Baloo2-Regular.ttf`

**Nasıl indir:**

```bash
# Bagel Fat One
curl -L -o assets/fonts/BagelFatOne-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/bagelfatone/BagelFatOne-Regular.ttf"

# Baloo 2
curl -L -o assets/fonts/Baloo2-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/baloo2/Baloo2%5Bwght%5D.ttf"
```

Ya da Google Fonts sayfalarından manuel:
- https://fonts.google.com/specimen/Bagel+Fat+One
- https://fonts.google.com/specimen/Baloo+2

## 4. Python Bağımlılıkları

Repo köküne `requirements.txt`:

```
Pillow>=10.0.0
```

Routine ortamı `pip install -r requirements.txt` komutunu kendi çalıştıracak.

## 5. Boş Log Dosyaları

İlk kurulumda, her biri içinde `# Kullanılan Konular` başlığı olan:

- `logs/sabah-9.md`
- `logs/ogle-12.md`
- `logs/ikindi-15.md`

## Final Klasör Yapısı

```
sincap-kitap-automation/
├── assets/
│   ├── logo.png
│   ├── character-reference.png
│   └── fonts/
│       ├── BagelFatOne-Regular.ttf
│       └── Baloo2-Regular.ttf
├── scripts/
│   └── overlay_text.py
├── logs/
│   ├── sabah-9.md
│   ├── ogle-12.md
│   └── ikindi-15.md
├── outputs/            ← boş başlar, routine doldurur
├── requirements.txt
└── README.md           ← opsiyonel, repo açıklaması
```

Hepsi hazır olduğunda `BURADAN-BASLA.md` dosyasındaki ADIM 4'e geçebilirsin.
