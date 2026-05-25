# Sincap Kitap IG — Sabah 09:00 (2026-05-25)

## Konu
**uyku direnci** — 0-6 yaş, anne odaklı, sıcak empatik ton.

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4A2E1B` (koyu kahve)

## Karakter
**bear cub** (5 slide boyunca aynı karakter, watercolor/gouache stilinde)

## Slot
`2026-05-25-sabah-9`

---

## Slide Metinleri

### Slide 1 — KAPAK
- **Ana başlık:** Uyumak
- **Aksan kelime:** İstemiyorum!
- **Alt başlık:** Çocuğunun uyku direnci, korku değil ihtiyaçtır.

### Slide 2 — TANIDIK SAHNE
> Saat geç, sen yorgunsun. O hâlâ "bir hikâye daha" diyor. Sabrını topluyorsun. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
> "Karanlık olunca seni unutuyorum gibi geliyor. Yanımda kalır mısın, biraz daha?"

### Slide 4 — UNUTMAYIN
- **Başlık:** UNUTMAYIN!
- **Gövde:** Uyku direnci, çocuğun günü bırakamamasıdır — seni reddetmek değil. Aynı sırayı her gece tekrarlamak, beynine "güvendesin" der. Bugün: ışığı kıs, sesini yumuşat, birlikte üç derin nefes alın.

### Slide 5 — KAPANIŞ
> Bu süreçte sana eşlik edecek sakin uyku hikâyeleri için Sincap Kitap'ı takip et 🐿️

---

## Higgsfield Prompt'lar

**Ortak iskelet:**
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette,
solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

**Sahneler:**
1. big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful and dreamy under a soft moon
2. bear cub character with mother bear character, warm hugging interaction, cozy indoor bedroom scene with a small lantern
3. small isolated bear cub character sitting on a bed, emotional vulnerable pose, vast empty space around (scale contrast), looking up at floating dream stars
4. family scene, mother bear and bear cub reading a bedtime storybook together, warm cozy bedroom setting with pillows and a soft blanket
5. bear cub character waving goodbye, smiling sleepily, sitting on a small stack of books with a tiny crescent moon nearby

---

## Notlar

- Higgsfield batch'i bu çalışmada **gönderilemedi**: bu remote execution ortamının outbound network policy'si `vercel-hf-probe.vercel.app` host'unu allowlist'e almıyor (`HTTP 403 host_not_allowed`). Relay host'u allowlist'e eklendikten sonra `scripts/relay_api.py submit-batch` ile aynı `/tmp/prompts.json` payload'u tekrar gönderilebilir.
- Çıktı slide'ları, placeholder olarak `#C9DDEC` solid arka plan üzerine metin bindirilerek üretildi; gerçek illüstrasyonlar geldiğinde aynı `layout.json` ile `python3 scripts/overlay_text.py outputs/2026-05-25-sabah-9/layout.json` koşulup üzerine yazılabilir.

## Caption
`caption.txt` dosyasındaki ~500 kelimelik anne odaklı caption + 20 hashtag kullanılacak.
