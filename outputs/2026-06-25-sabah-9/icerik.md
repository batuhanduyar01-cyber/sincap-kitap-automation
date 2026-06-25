# Sincap Kitap IG — 2026-06-25 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ** — bg `#C9DDEC`, accent `#E97E28` (turuncu), text `#3D2817` (koyu kahve)

## Karakter
**bear cub** (uykulu pijamalı ayı yavrusu) — 5 slide boyunca aynı

## Slide Metinleri

### Slide 1 — KAPAK
- **Title main:** Anne, Daha
- **Title accent:** Uyumam!
- **Subtitle:** Uyku direnci, büyümenin sessiz bir provası.
- **Dekorasyonlar:** evet (yıldız, ay, nokta — TOZ MAVİSİ ile uyumlu)

### Slide 2 — TANIDIK SAHNE
> Saat 21:30. Pijamalar giyildi, ışıklar kısıldı. Ama o yatağa çıktığı an: "Susadım… Tuvaletim var… Bir hikâye daha…" Tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Gözlerimi kapatınca dünya çok büyük oluyor. Yanımda olduğunu hissedince huzur buluyorum."

### Slide 4 — UNUTMAYIN!
> Uyku direnci geçici bir gelişim aşamasıdır. Tutarlı bir rutin, güvenli bir geçiş kurar. Bu gece: aynı sıralamayı izleyin — banyo, kitap, ışık, uyku.

### Slide 5 — KAPANIŞ
> Her yorucu gece, bir gün hatırlanacak bir hikâye olacak. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt İskeleti

Base (her slide aynı):
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character with soft brown-grey fur, large expressive sleepy eyes,
rosy blush cheeks, wearing a tiny pastel pajama, warm painterly palette,
solid #C9DDEC background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading,
portrait orientation, {SAHNE}
```

Sahneler:
1. big bear cub standing on a small hill of fluffy pillows, decorative moons stars and tiny floating clouds around, holding a small teddy, looking hopeful and a bit dreamy
2. bear cub being tucked in by a warm mother bear, mother bear gently patting cub's head, cozy bedroom with soft lamp glow, blanket pulled up, tender hugging interaction
3. small isolated bear cub sitting alone on a vast empty bed, tiny figure in a huge dark room with one small night light, emotional vulnerable pose, looking up with wide eyes, scale contrast emphasising loneliness
4. family scene of mother bear and bear cub reading a bedtime storybook together, warm cozy bedroom setting, soft yellow lamp, blanket and pillows, peaceful loving expressions
5. bear cub waving goodbye with a sleepy smile, sitting cross-legged on a stack of colorful storybooks, holding a tiny moon-shaped pillow, content and ready for sleep

## 🚫 ÇALIŞMA NOTU — Bu run'da görsel üretilemedi

Routine'in atandığı egress proxy politikası `vercel-hf-probe.vercel.app:443` 
hedefine CONNECT'i 403 (policy denial) ile reddetti. Proxy README açık şekilde
"bu durumda retry/by-pass etme; raporla" diyor.

**Proxy log (06:07:23 UTC):**
```
"kind": "connect_rejected",
"detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
"host": "vercel-hf-probe.vercel.app:443"
```

**Düzeltme yolları (en olası → en az):**
1. **Tercih:** Routine'in ağ policy'sine `vercel-hf-probe.vercel.app` (veya `*.vercel.app`)
   allowlist olarak eklensin. Routine settings → Network policy.
2. Relay'i organizasyonun allowlist'inde olan başka bir host'a (örn. Cloudflare 
   Workers, kendi domain'iniz) taşıyın.
3. Higgsfield'ı doğrudan çağıracak bir IP/host policy'de açıksa relay'i atlayıp 
   `scripts/higgsfield_api.py` ile direkt deneyin.

Bu rapor commit'lendiğinde metin deliverable'ları (caption.txt + bu icerik.md) 
hazır kalacak; ağ blockeri çözüldüğünde aşağıdaki tek komutla görseller doldurulabilir:

```bash
SLOT="2026-06-25-sabah-9"
BRANCH="claude/quirky-mendel-gd3qbf"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-deki-değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot   "$SLOT" \
    --branch "$BRANCH" \
    --prompts-file /tmp/prompts.json
```

ve ardından `python3 scripts/overlay_text.py outputs/2026-06-25-sabah-9/layout.json`.
