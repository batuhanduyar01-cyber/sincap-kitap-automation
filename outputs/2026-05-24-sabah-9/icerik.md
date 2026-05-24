# Sincap Kitap IG — 2026-05-24 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Ton
Anne odaklı, sıcak, empatik, yargısız.

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` turuncu
- Metin: `#4A2E1F` koyu kahve

Konu uykuya/sakinliğe işaret ettiği için palet eşleştirmesi tablo öneriyle birebir.

## Karakter
Bear cub — 5 slide boyunca tutarlı.

## Slide Metinleri

| # | Tip | İçerik |
|---|---|---|
| 1 | cover | Başlık: **"Anne, Bir"** + aksan **"Daha Sarıl!"** / alt başlık: "Uyku direnci, güvende olma ihtiyacının sesidir." |
| 2 | inner | "Saat geç, gözleri kapanıyor ama 'hayır, uyumayacağım' diyor. Bir bardak su, bir öpücük, bir kitap daha... Bu sahne tanıdık geliyor mu?" |
| 3 | quote | "Gözlerimi kapatınca yalnız kalıyorum, oysa gündüz hep birlikteydik." |
| 4 | tip | **UNUTMAYIN!** Uykuya direnç inat değil, gün boyu biriken duyguların boşalmasıdır. Aynı sıralama her gece güveni kurar. Bugün deneyebilirsiniz: 10 dakikalık sessiz kitap zamanı, sonra kısa ama net "iyi geceler". |
| 5 | cta | "Uyku rutinini yumuşatacak kitaplar için Sincap Kitap'ı takip et 🐿️" |

## Higgsfield Prompt'ları

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

Sahneler:
1. *big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful, holding a small crescent moon*
2. *bear cub with mother bear character, warm hugging interaction, cozy indoor bedroom scene with pillow and soft blanket*
3. *small isolated bear cub sitting alone in pajamas, emotional vulnerable pose, vast empty space around with tiny stars (scale contrast), looking up at the sky*
4. *family scene, parent bear and bear cub reading a storybook together in bed, warm cozy bedroom setting with soft lamp glow*
5. *bear cub waving goodbye, smiling, sitting on a stack of colorful storybooks*

## Üretim Durumu

| Adım | Durum |
|---|---|
| 1. Konu seçimi | ✅ Tamamlandı (log güncellendi) |
| 2. Metin üretimi | ✅ Tamamlandı |
| 3. Palette seçimi | ✅ TOZ MAVİSİ |
| 4. Higgsfield görselleri | ❌ **BLOKE** — relay 403 |
| 5. Metin bindirme | ⏸ Beklemede (görsel yok) |
| 6. Çıktı | ⚠ Kısmi (sadece metin) |

### Blokaj Detayı

`scripts/relay_api.py submit-batch` çağrısı `https://vercel-hf-probe.vercel.app/api/hf/submit` adresine POST attı ve **HTTP 403 — "Host not in allowlist"** cevabı aldı. Vercel relay'in middleware'i bu Routine session'ının çıkış IP'sini whitelist'te bulamadı.

**Çözüm önerisi:**
1. Vercel dashboard → `vercel-hf-probe` projesi → Settings → Environment Variables (veya middleware config) → mevcut Anthropic Routine IP aralığını allowlist'e ekle.
2. Bu Routine'i tekrar çalıştır; metin/layout dosyaları hazır olduğu için sadece Adım 4-5-6 çalışacak.

Alternatif: `HIGGSFIELD_API_KEY` + `HIGGSFIELD_API_SECRET` env değişkenlerini Routine ortamına ekle; `scripts/higgsfield_api.py` ile relay'i bypass et (ancak HF'nin Cloudflare WAF'ı yine reddedebilir).
