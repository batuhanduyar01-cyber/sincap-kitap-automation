# Rapor — Sincap Kitap IG 2026-04-21 Sabah 09:00

## Seçilen Konu
**Uyku direnci**
(log: son 14 günde tekrar yok — `logs/sabah-9.md` güncellendi.)

## Seçilen Palette
**MOR** — `#7E5BA0` arka plan / `#C5E86C` aksan / beyaz metin.

## 5 Görsel — Dosya Yolları
- `outputs/2026-04-21-sabah-9/slide-1.png`
- `outputs/2026-04-21-sabah-9/slide-2.png`
- `outputs/2026-04-21-sabah-9/slide-3.png`
- `outputs/2026-04-21-sabah-9/slide-4.png`
- `outputs/2026-04-21-sabah-9/slide-5.png`

Ham kaynaklar: `outputs/2026-04-21-sabah-9/raw/slide-{1..5}-raw.png`

## Caption — İlk 3 Satır
```
Bir kitap daha... Bir öpücük daha... Bir su daha...

Yatağın başındaki o sahne tanıdık geliyor mu? 🌙
```

## ⚠️ Higgsfield Üretimi Başarısız — Blokaj

Bu ortamdan `platform.higgsfield.ai` API çağrıları `HTTP 403` ile reddedildi
(response header: `x-deny-reason: host_not_allowed`). Higgsfield tarafındaki
IP allowlist bu runner'ın IP'sini tanımıyor.

**Şu an `raw/slide-*-raw.png` dosyaları solid-MOR placeholder'dır** — pipeline
uçtan uca test edilebilsin diye. Final `slide-*.png` dosyaları doğru metin,
tipografi, logo, dekorasyon ve renkle üretildi; eksik olan tek şey illüstrasyon
katmanı.

### Yapılması gereken
1. Higgsfield'a erişimi olan bir makinede (veya Higgsfield MCP/UI üzerinden)
   `icerik.md` içindeki 5 promptu sırayla çalıştır.
2. Çıktıları `outputs/2026-04-21-sabah-9/raw/slide-{1..5}-raw.png` olarak kopyala
   (placeholder'ların üzerine yaz).
3. `python3 scripts/overlay_text.py outputs/2026-04-21-sabah-9/layout.json` tekrar
   çalıştır. Final slide'lar otomatik yeniden üretilir.

## Üretilen Dosyalar
- `slide-1.png` … `slide-5.png` — final (placeholder raw üzerinden)
- `raw/slide-{1..5}-raw.png` — solid-MOR placeholder'lar
- `caption.txt` — 400-500 kelime caption + 20 hashtag
- `icerik.md` — konu, tüm metinler, palette, Higgsfield promptları
- `layout.json` — overlay config
