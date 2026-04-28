# Sincap Kitap IG — 2026-04-28 İkindi 15:00

**Konu:** Duygu adlandırma
**Palette:** MERCAN
- Arka plan: `#F08A7B`
- Aksan: `#FFF5E6` (krem)
- Metin: `#3B2413` (koyu kahve)

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Çocuklar Duygularını
- **title_accent:** Nasıl Tanır?
- **subtitle:** İçindeki fırtınayı kelimelere döken küçük yollar.

### Slide 2 — ÇERÇEVE
> Çocuğunuz bazen ağlar, bazen tepiniyor; aslında içinde adı henüz konulmamış fırtınalar var. Duyguya isim koymak, o fırtınayı dindirmenin ilk adımıdır.

### Slide 3 — ANAHTAR KAVRAM
- **Başlık:** İsim
- **Body:** Bir duygu adlandırıldığında çocuk yalnız hissetmez. "Üzgünüm" demek artık tehlikeli değil; gücüne dönüşür.

### Slide 4 — UNUTMAYIN!
- **Başlık:** UNUTMAYIN!
- **Body:** Çocuğunuz öfkelendiğinde önce duygusunu söyleyin: "Şu an çok kızgınsın, anlıyorum." Yargılamadan önce isim verin. Bu akşam deneyin: Yatmadan önce "Bugün üç duygu hissettim" oyunu oynayın; her birinize sıra gelsin.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Prompts (1152x1536, 1080p)

1. **Slide 1 (Kapak):** Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby fox character in rich scene, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F08A7B coral background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, central baby fox character holding a tiny mirror reflecting a smile, 2-3 small floating side objects (a heart shape, a small open book, a tear droplet), gentle sunset glow.
2. **Slide 2 (Çerçeve):** ... rich kindergarten classroom scene with four small animal children expressing different emotions: a happy bunny smiling, a sad bear with a tear, an angry hedgehog with crossed arms, a surprised mouse with wide eyes, sitting in a circle on a rug, soft afternoon light.
3. **Slide 3 (Kavram — İsim):** ... small fox character with a soft thought bubble above its head containing three little floating face icons (happy, sad, angry) like tiny clouds, surrounded by gentle painterly stars and warm coral light.
4. **Slide 4 (UNUTMAYIN!):** ... mother rabbit gently hugging her crying baby rabbit on a cozy living room couch, a small open storybook beside them, a steaming cup of warm milk on a low table, soft golden afternoon light, tender comforting moment.
5. **Slide 5 (Kapanış):** ... friendly squirrel character standing center, surrounded by small floating storybooks, a tiny acorn, a heart shape, and a warm tea cup, gentle sunset glow, inviting closing scene.

> Tam prompt JSON: `outputs/2026-04-28-ikindi-15/prompts.json`

## Üretim Notu

Bu çalıştırmada Vercel relay (`vercel-hf-probe.vercel.app`) ve Higgsfield platformuna doğrudan istekler sandbox network allowlist'i tarafından `403 Host not in allowlist` ile reddedildi. Görseller üretilemedi; metin paketi, prompt JSON'u ve `layout.json` commit'lendi. Görsel akışı, allowlist'li bir ortamdan şu komutla tekrar tetiklenebilir:

```bash
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
  --slot 2026-04-28-ikindi-15 \
  --branch claude/zen-wozniak-0HlKS \
  --prompts-file outputs/2026-04-28-ikindi-15/prompts.json
```

Görseller `assets/gorseller/2026-04-28-ikindi-15/slide-{1..5}.png` olarak commit'lendiğinde, `python3 scripts/overlay_text.py outputs/2026-04-28-ikindi-15/layout.json` ile final slide'lar oluşur.
