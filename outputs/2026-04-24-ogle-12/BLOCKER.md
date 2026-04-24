# BLOCKER — Higgsfield Görselleri Üretilemedi

**Tarih:** 2026-04-24 — Öğle 12:00
**Konu:** Karanlık korkusu

## Sorun

Sandbox egress proxy `vercel-hf-probe.vercel.app` ve `platform.higgsfield.ai`
hostlarını engelliyor — tüm outbound isteklere **HTTP 403 "Host not in
allowlist"** dönüyor:

```
curl https://vercel-hf-probe.vercel.app/api/hf/status  → 403 Host not in allowlist
curl https://platform.higgsfield.ai/                   → 403 Host not in allowlist
```

Bu nedenle `scripts/relay_api.py submit-batch` çağrısı submit aşamasında
başarısız oldu (exit 3).

## Geçici Çözüm

Bu routine çalıştırmasında `assets/gorseller/2026-04-24-ogle-12/slide-*.png`
dosyaları, sahnelerin üretilemediği gerçeğini yansıtmak için **düz mor arka plan**
(#7E5BA0) ile oluşturuldu. Metin overlay'i bu düz arka planlara uygulandı — yani
`outputs/2026-04-24-ogle-12/slide-*.png` posta hazır DEĞİL; yalnızca text katmanı
doğru.

## Yeniden Üretim Adımları (manuel, allowlist düzeltildikten sonra)

1. `vercel-hf-probe.vercel.app`'i Claude Code sandbox egress allowlist'ine ekle
   (veya routine'i DNS'i açık olan bir host'ta çalıştır).
2. `/tmp/prompts.json` dosyası bu çalıştırmadan kayıtlı değil, ancak promptlar
   `outputs/2026-04-24-ogle-12/icerik.md` ve aşağıdaki JSON ile tekrar üretilebilir:

```json
[
  {"prompt": "Children's book illustration, watercolor gouache painting, textured brush strokes, cute little bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, wearing cozy pajamas, warm painterly palette, solid #7E5BA0 purple background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, bear cub in dynamic expressive pose looking up with wide curious eyes at a starry night, holding a tiny glowing lantern, nighttime magical scene, 5-8 decorative elements around (stars, sparkles, moons, tiny clouds, fireflies)", "width_and_height": "1152x1536", "quality": "1080p"},
  {"prompt": "Children's book illustration, watercolor gouache painting, textured brush strokes, cute little bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, wearing cozy pajamas, warm painterly palette, solid #7E5BA0 purple background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, bear cub hugged warmly by a bigger parent bear, both smiling tenderly, holding hands under a soft night sky, cozy loving interaction, gentle sparkles around them", "width_and_height": "1152x1536", "quality": "1080p"},
  {"prompt": "Children's book illustration, watercolor gouache painting, textured brush strokes, cute little bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, wearing cozy pajamas, warm painterly palette, solid #7E5BA0 purple background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, isolated tiny bear cub standing small against a vast dark bedroom with huge exaggerated wall shadows, emotional vulnerable pose, little paws clutching a blanket, big eyes", "width_and_height": "1152x1536", "quality": "1080p"},
  {"prompt": "Children's book illustration, watercolor gouache painting, textured brush strokes, cute little bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, wearing cozy pajamas, warm painterly palette, solid #7E5BA0 purple background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, calm adult bear reading a bedtime storybook to the small bear cub tucked in bed, soft night lamp glowing, cozy bonding moment, warm blanket, peaceful atmosphere", "width_and_height": "1152x1536", "quality": "1080p"},
  {"prompt": "Children's book illustration, watercolor gouache painting, textured brush strokes, cute little bear cub character with soft brown fur, large expressive eyes, rosy blush cheeks, wearing cozy pajamas, warm painterly palette, solid #7E5BA0 purple background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, bear cub waving goodbye with a cheerful sleepy smile, standing next to a small stack of picture books, crescent moon and little stars in background, pajamas, holding a teddy", "width_and_height": "1152x1536", "quality": "1080p"}
]
```

3. Allowlist düzeltildikten sonra:

```bash
SLOT="2026-04-24-ogle-12"
BRANCH="claude/confident-dijkstra-JQpE0"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-04-24-ogle-12/layout.json
```

`layout.json` değişmeden kullanılabilir — overlay raw slide'ları üzerine yeniden
çizer ve `outputs/2026-04-24-ogle-12/slide-*.png` dosyalarını günceller.
