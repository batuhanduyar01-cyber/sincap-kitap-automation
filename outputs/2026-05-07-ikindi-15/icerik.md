# Sincap Kitap IG — 2026-05-07 İkindi 15:00

## Konu
**duygu adlandırma** — 0-6 yaş çocuklar için duyguları kelimelere dökme pratiği. Pedagojik temel: "name it to tame it" — bir duyguyu adlandırmak, onu yumuşatmanın en sevecen yolu.

## Palette: HARDAL
| Rol     | Renk    |
|---------|---------|
| Arka plan | `#F5C82E` |
| Aksan   | `#8E4FAA` (mor) |
| Metin   | `#2A1810` (koyu kahve) |

## Karakter
Yavru tilki (little fox cub) — 5 slide boyunca aynı karakter, sıcak turuncu kürk + beyaz karın + kehribar gözler.

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Duyguya İsim
- **title_accent:** Vermek
- **subtitle:** İçimizdeki fırtınaya isim koymak, sakinleşmenin ilk adımıdır.

### Slide 2 — ÇERÇEVE
> Üzgün mü, kızgın mı, yorgun mu? Çocuklar bazen içlerindeki dalgalanmayı tarif edemez. Adı bilinmeyen duygu, en zorlayan olur.

### Slide 3 — ANAHTAR KAVRAM: "Adlandırma"
> Bir duyguya isim vermek, onu yumuşatmanın en sevecen yoludur.

### Slide 4 — UNUTMAYIN!
> Çocuğunuzun yerine duygusunu siz adlandırabilirsiniz: "Şu an hayal kırıklığı yaşıyor olabilirsin." Bu küçük cümle, koca bir iç dünyayı görünür kılar.
>
> **Bu akşam:** Yatmadan önce "Bugün seni en çok ne mutlu etti, ne üzdü?" diye sorun.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Prompts

Ortak iskelet (her slide):
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute little fox cub character with soft orange fur and white belly, large expressive amber eyes, rosy blush cheeks, warm painterly palette, **solid #F5C82E mustard yellow background**, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation 1152x1536.

Slide-spesifik sahneler:

1. **Kapak:** Central fox cub standing gently smiling with hand on heart, 2-3 floating side objects (storybook, tiny heart, sparkle), warm afternoon light.
2. **Tanıdık sahne:** Multiple animal characters (fox cub, baby bear, tiny rabbit, hedgehog) sitting on a soft round rug in a kindergarten feelings circle, holding small colorful emotion cards (sun, cloud, tear).
3. **Anahtar kavram:** Fox cub on tiptoes touching one of several pastel emotion clouds floating in the sky (peach, lilac, sage, sky blue) — represents naming an emotion.
4. **Ebeveyn ipucu:** Parent fox and cub sitting on cozy floor cushion with a small storybook between them, soft lamp glow, evening heart-to-heart moment, tea cup nearby.
5. **Kapanış:** Fox cub on a small stack of colorful storybooks, waving with one paw, holding a tiny red heart, golden hour glow.

## Üretim Notu

Vercel relay (`https://vercel-hf-probe.vercel.app`) bu çalışma ortamından **HTTP 403 "Host not in allowlist"** ile reddetti — bu sebeple `assets/gorseller/2026-05-07-ikindi-15/slide-{1..5}.png` dosyaları gerçek Higgsfield çıktısı değil, **HARDAL arka plan rengiyle düz placeholder PNG**'ler. Layout ve metin bindirme akışı tamamen çalıştırıldı; gerçek görseller geldikten sonra `python3 scripts/overlay_text.py outputs/2026-05-07-ikindi-15/layout.json` komutu yeniden üretmek için yeterli. Routine ortamından (allowlisted IP) submit edildiğinde aynı `prompts.json` 5 görseli aynı slot dizinine commit'leyecek.

`prompts.json` orijinal içeriği bu dosya ile birlikte saklı (`outputs/2026-05-07-ikindi-15/prompts.json`).

## Çıktı dosyaları

- `outputs/2026-05-07-ikindi-15/slide-1.png` ... `slide-5.png` — final
- `outputs/2026-05-07-ikindi-15/raw/slide-{1..5}-raw.png` — ham (placeholder)
- `outputs/2026-05-07-ikindi-15/caption.txt` — IG caption + hashtag'ler
- `outputs/2026-05-07-ikindi-15/layout.json` — overlay config
- `outputs/2026-05-07-ikindi-15/prompts.json` — Higgsfield prompts (5 slide)
