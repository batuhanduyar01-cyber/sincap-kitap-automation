# Sincap Kitap IG — 2026-04-22 İkindi 15:00

**Konu:** Okul öncesi hazırlık
**Ton:** Sıcak anne + bilge arkadaş, pedagojik ipucu ağırlıklı
**Palette:** Turuncu (#E97E28) bg / Beyaz (#FFFFFF) accent / Koyu kahve (#2A1810) text — ikindi sıcak hissi

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** Okul Öncesi
- **Aksan:** Hazırlık
- **Alt başlık:** Küçük adımlarla büyük başlangıçlar.

### Slide 2 — ÇERÇEVE
> Anaokulu çocuğunuz için yepyeni bir dünya. Heyecan ve tedirginlik yan yana büyür. Bu hazırlık dönemi sevgiyle, sabırla ve oyunla şekillenir.

### Slide 3 — ANAHTAR KAVRAM: Güven
> Annesinin hep yanında olduğunu bilen çocuk, yeni dünyalara cesaretle adım atar.

### Slide 4 — UNUTMAYIN!
> Her çocuk farklı hızda hazırlanır. Aceleye getirmeyin, küçük zaferleri kutlayın. Bu akşam yatmadan önce beş dakika ayırın ve "Yarın okulda hangi oyunu seveceksin?" diye sorun.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Dosyalar

- `slide-1.png` … `slide-5.png` (1080×1350 carousel)
- `raw/slide-{1..5}-raw.png` (ham görsel girdileri)
- `layout.json` (overlay konfigürasyonu)
- `caption.txt` (Instagram açıklama metni)

## Önemli Not — Görsel Üretimi

Bu Routine çalıştırıldığı ortamda Higgsfield API host'u (`platform.higgsfield.ai`)
network egress allowlist'inde olmadığı için (HTTP 403 "Host not in allowlist")
gerçek illüstrasyonlar üretilemedi. Ham görseller fallback olarak
`assets/character-reference.png` karakteri sıcak turuncu (#E97E28) zemin üzerine
yerleştirilerek üretildi (bkz. `scripts/generate_placeholder_raws.py`).

Üretim ortamında host allowlist'lendikten sonra `raw/slide-*-raw.png` dosyaları
prompt iskeletindeki orijinal Higgsfield Soul prompt'larıyla yeniden üretilmeli
ve `python3 scripts/overlay_text.py outputs/2026-04-22-ikindi-15/layout.json`
yeniden çalıştırılmalı.
