# Fontlar

Bu klasöre iki TTF dosyası eklenmeli:

- `BagelFatOne-Regular.ttf` — başlıklar için (kalın kaligrafi)
- `Baloo2-Regular.ttf` — gövde metinleri için (yumuşak sans)

## Yerel makinede indirme (proxy kısıtlı ortamda çalışmaz)

```bash
cd assets/fonts

curl -L -o BagelFatOne-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/bagelfatone/BagelFatOne-Regular.ttf"

curl -L -o Baloo2-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/baloo2/Baloo2%5Bwght%5D.ttf"
```

## Alternatif: Google Fonts UI

1. https://fonts.google.com/specimen/Bagel+Fat+One → "Get font" → zip indir → `BagelFatOne-Regular.ttf`
2. https://fonts.google.com/specimen/Baloo+2 → "Get font" → zip indir → `Baloo2-Regular.ttf` (sadece Regular ağırlığı)

Dosyaları bu klasöre (`assets/fonts/`) koy, repo'ya commit'le.

## Neden gerekli?

`scripts/overlay_text.py` Türkçe karakter destekli, Sincap Kitap görsel kimliğiyle
uyumlu iki fontu yükler. Font yoksa Pillow default fontuna düşer ve başlıklar
incecik görünür.

## Lisans

SIL Open Font License — ticari kullanıma açık.
