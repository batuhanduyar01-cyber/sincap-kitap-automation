# Sincap Kitap IG — 2026-05-05 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

Son 14 günde tekrar yok (log boştu). Konu `logs/sabah-9.md` dosyasına eklendi.

## Palette
**TOZ MAVİSİ** — sakinlik / uyku teması ile uyumlu.

| Rol | Hex |
|---|---|
| Arka plan | `#C9DDEC` |
| Aksan | `#E97E28` (turuncu) |
| Metin | `#3F2A1C` (koyu kahve) |

## Karakter
Bear cub (yavru ayı) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık ana: **Uyumam,**
- Aksan: **Anne!**
- Alt başlık: *Uyku direnci, gelişimin sessiz bir mesajıdır.*
- Dekorasyon: yıldız + nokta + küçük çizgiler (kompozisyonlu)

### Slide 2 — TANIDIK SAHNE
> Saat 21:00, oda kararıyor. Küçük gözler hâlâ pırıl pırıl. 'Bir hikâye daha' diyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "Gözlerim kapanmıyor anne, içimde hâlâ koşuşturan minik bir tay var."

### Slide 4 — UNUTMAYIN!
**Başlık:** UNUTMAYIN!

> Çocuklar gün boyu biriktirdikleri duyguları akşam taşır. Kısa ve öngörülebilir bir uyku rutini, beyne 'güvendesin, dinlenebilirsin' der. Bugün: aynı sırayla 'banyo–kitap–öpücük' deneyebilirsiniz.

### Slide 5 — KAPANIŞ
> Uykudan önce el ele tutuşan kitaplarımız için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (özet)

Ortak iskelet (her slide):
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute **bear cub** character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid **#C9DDEC** background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, *{SAHNE}*

| Slide | Sahne |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | bear cub with mother bear character, warm hugging interaction, cozy indoor scene |
| 3 | small isolated bear cub, emotional vulnerable pose, vast empty space around (scale contrast), looking up |
| 4 | family scene, parent bear and bear cub reading book together, warm cozy bedroom setting |
| 5 | bear cub waving goodbye, smiling, sitting on a book stack |

Tam prompt JSON: bkz. `prompts.json`.

## Çıktılar (planlanan)

- `outputs/2026-05-05-sabah-9/slide-1.png` … `slide-5.png` — final (overlay sonrası)
- `assets/gorseller/2026-05-05-sabah-9/slide-1.png` … `slide-5.png` — Higgsfield ham görseller (relay tarafından commit'lenir)
- `outputs/2026-05-05-sabah-9/caption.txt` — Instagram caption + hashtag
- `outputs/2026-05-05-sabah-9/layout.json` — overlay konfigürasyonu
- `outputs/2026-05-05-sabah-9/icerik.md` — bu dosya
- `outputs/2026-05-05-sabah-9/prompts.json` — Higgsfield prompt JSON

## Çalışma Durumu

- ✅ Konu seçimi & log güncellemesi
- ✅ Metin üretimi (5 slide + caption + hashtag)
- ✅ Palette seçimi
- ✅ Higgsfield prompt'ları hazırlandı (`prompts.json`)
- ❌ **Görsel üretimi (Higgsfield via Vercel relay)** — `403 Host not in allowlist`
- ⏸ Overlay (`overlay_text.py`) — ham görseller gelmediği için atlandı
- ✅ Metin artefaktları commit'lenecek

## Hata Detayı (Adım 4b)

`POST https://vercel-hf-probe.vercel.app/api/hf/submit` → **HTTP 403** `{"_raw": "Host not in allowlist"}`

Relay'in kendi IP allowlist'i var ve bu Routine runner'ın çıkış IP'si listede değil. Bu, relay tarafında bir konfigürasyon sorunu — `RELAY_SHARED_SECRET` doğrulamasının üstünde, daha alt katmanda bir egress IP filtresi var.

### Çözüm seçenekleri (operatör)
1. Vercel `vercel-hf-probe` projesinin host/IP allowlist konfigürasyonunu güncelle (Routine'in bilinen egress IP aralıklarını ekle).
2. Veya allowlist'i kaldır, sadece `RELAY_SHARED_SECRET` ile koruma yap.
3. Allowlist düzeltildikten sonra Adım 4b ve sonrasını yeniden çalıştır:

```bash
SLOT="2026-05-05-sabah-9"
BRANCH="claude/quirky-mendel-8mwtV"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-05-05-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-05-sabah-9/layout.json
```
