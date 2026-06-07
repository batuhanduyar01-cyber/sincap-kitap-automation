# Sincap Kitap — Öğle 12:00 Carousel

- **Tarih:** 2026-06-07
- **Slot:** 2026-06-07-ogle-12
- **Konu:** Diş fırçalatmama
- **Karakter:** Sevimli minik tavşan (baby rabbit)
- **Palette:** HARDAL #F5C82E (bg) / MOR #7E5BA0 (accent) / KAHVE #3D2817 (text)

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Dişimi Fırçalamak
- **Başlık (aksan):** İstemiyorum!
- **Alt başlık:** Bir minik tavşanın bahaneleri.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Anneciğim seninle birlikte fırçalarsam çok mutlu olurum."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Köpük ağzımı gıdıklıyor ve biraz garip hissediyorum."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**

Diş fırçalamak bir görev değil paylaşılan bir oyundur. Aynanın önünde birlikte fırçalayın, komik suratlar yapın, kısa bir şarkı söyleyin.

### Slide 5 — KAPANIŞ
> Pırıl pırıl gülüşler için Sincap Kitap'ı takip et 🐿️

## Üretim Notu — Higgsfield Görselleri Üretilemedi

Bu slot için Higgsfield illüstrasyonları ÜRETİLEMEDİ.

- **Hata:** `https://vercel-hf-probe.vercel.app/api/hf/submit` → HTTP 403 `Host not in allowlist`
- **Sebep:** Bu remote execution ortamının egress proxy'si `*.vercel.app` hostlarını blokluyor. Curl ile doğrulandı: `vercel.com` → 403, `vercel-hf-probe.vercel.app` → 403, `github.com` → 200.
- **Bunun anlamı:** Relay shared secret doğru; ama sandbox dış erişimi blokluyor — `RELAY_SHARED_SECRET` değiştirmek bu hatayı çözmez.
- **Geçici çözüm:** `assets/gorseller/2026-06-07-ogle-12/slide-{1..5}.png` solid HARDAL (#F5C82E) placeholder PNG. Overlay scripti bu placeholder'ların üzerine metinleri bastı, böylece tipografi/yerleşim hâlâ önizlenebilir.

### Üretildiğinde Kullanılacak Higgsfield Promptları

Aşağıdaki 5 prompt `/tmp/prompts.json` içinde de var. Relay'e erişim açıldığında aynı slot ile tekrar submit edilebilir.

```
Common prefix:
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute baby rabbit with soft white fur and floppy ears, large expressive eyes,
rosy blush cheeks, warm painterly palette, solid #F5C82E background,
Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames,
portrait orientation,
```

1. **Slide 1 sahnesi:** rabbit holding a tiny toothbrush in dynamic playful pose, head tilted with stubborn pout, 5-8 decorative elements floating around: white toothpaste bubbles, small sparkles, mint leaves, tiny stars
2. **Slide 2 sahnesi:** rabbit child and parent rabbit cuddling warmly in front of a small mirror, both holding toothbrushes, giggling together in a tender bonding moment, soft cozy bathroom setting
3. **Slide 3 sahnesi:** small isolated baby rabbit looking up at a giant toothbrush, tiny scale against vast empty background, vulnerable hesitant pose, big worried eyes shining with curiosity
4. **Slide 4 sahnesi:** calm parent rabbit reading a picture book to baby rabbit in cozy bedtime moment, snuggled in soft blanket, warm gentle scene of bonding before sleep
5. **Slide 5 sahnesi:** rabbit waving goodbye with a cheerful joyful smile showing tiny shiny teeth, standing next to a small neat stack of storybooks, bright happy farewell pose

## Çıktılar

- `outputs/2026-06-07-ogle-12/slide-1.png` (kapak)
- `outputs/2026-06-07-ogle-12/slide-2.png` (alıntı 1)
- `outputs/2026-06-07-ogle-12/slide-3.png` (alıntı 2)
- `outputs/2026-06-07-ogle-12/slide-4.png` (ebeveyn notu)
- `outputs/2026-06-07-ogle-12/slide-5.png` (kapanış)
- `outputs/2026-06-07-ogle-12/caption.txt`
- `outputs/2026-06-07-ogle-12/layout.json`
- `outputs/2026-06-07-ogle-12/raw/` — ham Higgsfield illüstrasyonları (boş; relay engellenince doldurulamadı)
