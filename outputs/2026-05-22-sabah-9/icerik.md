# Sincap Kitap IG — 2026-05-22 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

Tekrar kontrolü: `logs/sabah-9.md` son 14 gün boş — tekrar yok. Konu loglandı.

## Palette
**TOZ MAVİSİ** — sakinlik/uyku temasına uygun.

| Rol | Hex |
|---|---|
| Arka plan | `#C9DDEC` |
| Aksan | `#E97E28` (turuncu) |
| Metin | `#4A352A` (koyu kahve) |

## Karakter
**Bear cub (yavru ayı)** — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): **Anne, Uykum**
- Başlık (aksan): **Yok!**
- Alt başlık: Uyku direnci, çoğu zaman bir veda zorluğudur.

### Slide 2 — TANIDIK SAHNE
Gözleri minik minik kapanıyor ama yatağa gelince birden uyanıyor. Bir bardak su, bir masal daha... Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
"Gözlerimi kapatınca seninle geçen gün de bitiyor. Biraz daha kalmak istiyorum."

### Slide 4 — UNUTMAYIN!
Uyku direnci inatçılık değil; günün bitişine karşı küçük bir tereddüt. Aynı sırayla ilerleyen sakin bir gece rutini, çocuğa güven verir. Bugün: yatmadan önce 10 dakikalık sessiz bir sarılma vakti deneyebilirsiniz.

### Slide 5 — KAPANIŞ
Her gece biraz daha kolaylaşacak; sen yanındayken uyku da güvenli bir yer. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları (TOZ MAVİSİ + bear cub)

Ortak iskelet:
`Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

Boyut: `1152x1536` · Kalite: `1080p`

1. `... big character standing on a small hill, decorative leaves and stars around, looking hopeful`
2. `... character with mother/parent character, warm hugging interaction, cozy indoor scene`
3. `... small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up`
4. `... family scene, parent and child reading book together, warm cozy bedroom setting`
5. `... character waving goodbye, smiling, sitting on a book stack`

## Görsel Üretim Durumu — BLOKE

ADIM 4 (Higgsfield görselleri) bu Routine ortamında **tamamlanamadı**.

- Vercel relay (`https://vercel-hf-probe.vercel.app`) ve Higgsfield host'ları,
  bu ortamın egress ağ politikası tarafından engelleniyor:
  `HTTP 403 — Host not in allowlist`.
- `scripts/relay_api.py submit-batch` exit kodu 3 (submit başarısız) döndü.
- Sadece `github.com` / `raw.githubusercontent.com` gibi host'lara çıkış izni var.

**Geçici çözüm:** 5 slide için TOZ MAVİSİ (`#C9DDEC`) düz renkli **placeholder**
arka planlar üretildi ki `overlay_text.py` uçtan uca çalışsın ve metin/yerleşim
kontrolü yapılabilsin. Final görseller karakter illüstrasyonu içermiyor.

**Yapılması gereken:** Ağ politikası `vercel-hf-probe.vercel.app` host'una
izin verecek şekilde güncellendiğinde (veya relay'e erişebilen bir ortamda)
yukarıdaki 5 prompt ile ADIM 4 yeniden çalıştırılmalı, ardından ADIM 5
gerçek ham görsellerle tekrar üretilmeli.

## Caption
`caption.txt` dosyasına yazıldı (~470 kelime + 20 hashtag).
