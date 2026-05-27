# Sincap Kitap IG — 2026-05-27 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4A2C1A` (koyu kahve)

## Karakter
Bear cub (ayı yavrusu), küçük çizgili pijamalı, uykulu büyük gözler — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Anne, Bir
- **Başlık (aksan):** Masal Daha!
- **Alt başlık:** Uyku direnci, seninle bir an daha kalma isteğidir.

> Not: Bagel Fat One Turkish glyph desteğinde `Ğ/ğ/Ş/ş/İ` eksik;
> bu yüzden kapak aksan kelimesi `Uyumayacağım!`tan `Masal Daha!`a
> çevrildi (yatak öncesi klasik müzakereyi yansıtıyor, kitap markası
> için bonus olarak konuyla uyumlu).

### Slide 2 — TANIDIK SAHNE
> Işıklar yumuşadı, oda sessizleşti ama o hâlâ yatakta zıplıyor. Minik gözler "henüz hazır değilim" diyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerim kapanıyor ama seni kaybetmek istemiyorum."

### Slide 4 — UNUTMAYIN!
**UNUTMAYIN!**

Uyku direnci tembellik değil, bağlanmanın bir biçimidir. Sabit bir rutin geceyi güvenli bir limana dönüştürür.

**Bugün:** Yatmadan önce 10 dakikalık "sessiz buluşma" deneyin.

### Slide 5 — KAPANIŞ
> Yorgun geceleri kucaklayan kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute small bear cub character, soft cream-brown fur, large expressive sleepy eyes,
rosy blush cheeks, wearing tiny striped pajamas, warm painterly palette,
solid #C9DDEC dusty blue background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading,
portrait orientation, {SAHNE}
```

| Slide | {SAHNE} |
|---|---|
| 1 | big bear cub character standing on a small grassy hill at dusk, decorative crescent moon and tiny stars scattered around the sky, looking hopeful and curious upward |
| 2 | small bear cub with gentle mother bear character holding him in a warm hug, cozy indoor bedroom scene with soft blanket and tiny pillow, tender bedtime moment |
| 3 | tiny isolated bear cub sitting alone on the floor, emotional vulnerable pose, vast empty space around the character creating scale contrast, looking up at the ceiling with big shiny eyes |
| 4 | family bear scene, parent bear and bear cub reading a small picture book together in a warm cozy bedroom setting, soft bedside lamp glow, tucked-in blanket |
| 5 | bear cub waving goodbye with a small smile, sitting on a tidy stack of three storybooks, tiny stars and dots floating around playfully |

## Hashtag Seti
`#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #uyku #uykudirenci #çocukgelişimi #annebebek #uykurutini #pozitifebeveynlik #annelikrehberi #çocukpsikolojisi #yatakvakti #annenotları #çocuğumlaokuyorum #bebekuykusu #ebeveynlikipuçları #annekızı #anneoğlu`

## Üretim Notu — Higgsfield İllüstrasyonları Eksik

Bu çalıştırmada **Higgsfield illüstrasyonları üretilemedi.** Vercel relay
(`https://vercel-hf-probe.vercel.app`) hem `/api/hf/submit` hem
`/api/hf/status` endpoint'lerinde `403 host_not_allowed` döndü:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

Yani routine runner'ın çıkış IP'si relay'in allowlist'inde değil.
Bu Adım 4'ün premise'inin tersi — normalde relay Higgsfield WAF'ını
bypass ediyordu, ama bu sefer relay'in kendisi runner'ı blokluyor.

Sonuç olarak `assets/gorseller/2026-05-27-sabah-9/slide-*.png`
dosyaları **#C9DDEC düz palette arka planı** (1152×1536) olarak
yerleştirildi ki Adım 5'teki PIL overlay'i tam pipeline boyunca
koşturabileyim ve metin/yerleşim/font çıktısını doğrulayabilesin.

**Bear cub illüstrasyonu eklemek için:**
1. Allowlist'li bir ortamdan veya local'den
   `scripts/relay_api.py submit-batch ...` çalıştır (yukarıdaki
   prompt'lar `/tmp/prompts.json` formatında).
2. Webhook commit'lerini `git pull --ff-only origin
   claude/quirky-mendel-biaxI` ile çek.
3. Aynı `layout.json`'la `python3 scripts/overlay_text.py
   outputs/2026-05-27-sabah-9/layout.json` komutunu yeniden çalıştır
   — overlay zaten `assets/gorseller/2026-05-27-sabah-9/slide-*.png`'yi
   ham görsel olarak okuduğu için, dosyalar Higgsfield çıktısıyla
   değişince final PNG'ler bear cub'lı sürüm olur.
