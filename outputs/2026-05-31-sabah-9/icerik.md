# Sincap Kitap IG — 2026-05-31 Sabah 09:00

## Konu
**uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#4A2E1F` (koyu kahve)

## Karakter
panda cub (yumuşak, uyku/sakinlik teması)

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Anne, Daha
- **Başlık (aksan):** Uyumayacağım!
- **Alt başlık:** Uyku direnci, gelişimin doğal bir evresi.

### Slide 2 — TANIDIK SAHNE
> Banyo bitti, kitap okundu, ışıklar kapandı. Ama küçük bir baş hâlâ kalkıp "Bir tane daha anne!" diyor. Tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kapatınca dünya bensiz devam ediyormuş gibi geliyor."

### Slide 4 — UNUTMAYIN!
> Uyku direnci, çocuğunuzun büyüdüğünün ve dünyayı kaçırmak istemediğinin işareti. Sabırlı tekrar güvenli bir ritüel kurar. Bugün: aynı sırayla 3 küçük adım — banyo, kitap, sarılma.

### Slide 5 — KAPANIŞ
> Her uyumayan gece, küçük bir öğrenme. Yalnız değilsin. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Hepsi ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute **panda cub** character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid **#C9DDEC** dusty blue background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, **{SAHNE}**

| Slide | Sahne |
|---|---|
| 1 | big panda cub standing on a small hill, decorative leaves and stars around, looking hopeful, soft moonlight atmosphere |
| 2 | panda cub with mother panda character, warm hugging interaction, cozy indoor bedroom scene, soft pillows and a tiny lamp |
| 3 | small isolated panda cub, emotional vulnerable pose sitting on a big bed, vast empty space around for scale contrast, looking up at the night sky through a window |
| 4 | family scene, parent panda and panda cub reading a storybook together, warm cozy bedroom setting with stars and a soft blanket |
| 5 | panda cub waving goodbye, gently smiling, sitting on a stack of books, small crescent moon nearby |

## Üretim Notu — BLOKE

Bu çalışmada Higgsfield görselleri üretilemedi.

**Sebep:** Routine sandbox'ın outbound network policy'si `vercel-hf-probe.vercel.app` host'unu allowlist'te tutmuyor — `/api/hf/submit`'e yapılan POST `HTTP 403 "Host not in allowlist"` ile geri döndü. Aynı şekilde `api.higgsfield.ai` de bloklu (zaten relay'in var oluş sebebi buydu).

**Reachable görünenler:** sadece `github.com` (git push çalışıyor); `api.github.com`, `higgsfield.ai`, ve Vercel relay hepsi 403.

**Çözüm seçenekleri:**
1. Environment'ın network policy'sine `vercel-hf-probe.vercel.app` host'unu allowlist olarak ekle.
2. Veya bu routine için "broader" network policy seçilen yeni bir environment kullan.
3. Veya secret rotated olduysa (placeholder hala prompt'taysa) Vercel dashboard'daki gerçek `RELAY_SHARED_SECRET` ile prompt'u güncelle — fakat şu anki 403 secret değil, IP/host policy kaynaklı.

İçerik (metin + layout + prompts) hazır. Allowlist düzeldiğinde aynı slot adıyla (`2026-05-31-sabah-9`) tekrar koşmak yeterli.
