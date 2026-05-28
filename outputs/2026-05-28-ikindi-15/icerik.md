# Sincap Kitap IG — İkindi 15:00 — 2026-05-28

## Konu
**Hayal gücü** (yaratıcılık, merak, açık uçlu düşünme)

## Palette: HARDAL
- Arka plan: `#F5C82E` (hardal sarısı)
- Aksan: `#8E4FAA` (mor)
- Metin: `#2A1810` (koyu kahve)

## Karakter
Baby squirrel (5 slide boyunca aynı)

## Slide Metinleri

### Slide 1 — KAPAK
- title_main: "Hayal Gücü"
- title_accent: "Sınır Tanımaz"
- subtitle: "Küçük zihinlerin büyük dünyaları."

### Slide 2 — ÇERÇEVE
> Çocuklar bir kutuyu uzay gemisine, battaniyeyi şato sancağına çevirir. Bu sihir, hayal güçlerinin dünyaya dokunuşudur.

### Slide 3 — ANAHTAR KAVRAM
- Başlık: "Merak"
- Body: "Hayal gücü meraktan beslenir. Sorularını yargılamadan dinleyin, beraber düşünün."

### Slide 4 — UNUTMAYIN!
> Açık uçlu sorular, sade nesneler ve boş zaman hayal gücünü büyütür. Bu akşam deneyin: 'Bir bulut olsaydın nereye giderdin?' diye sorun.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Promptları (her slide için)

**Slide 1 (kapak):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character with large expressive eyes and rosy cheeks, holding a magic paintbrush, 2-3 small side objects floating around (colored pencil, open book, glowing star), warm painterly palette, solid #F5C82E mustard yellow background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, dreamy whimsical atmosphere

**Slide 2 (çerçeve — zengin sahne):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, rich scene with multiple cute animal characters (baby squirrel, little bear cub, kitten, baby fox) sitting around an art table, painting and crafting paper crowns, drawing on big white papers, large expressive eyes, rosy cheeks, warm painterly palette, solid #F5C82E mustard yellow background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, cozy creative classroom setting

**Slide 3 (kavram — soyut):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character with large expressive eyes and rosy cheeks, floating dreamily among colorful soft clouds, surrounded by imaginary creatures (tiny dragon, fish swimming in air, smiling moon), warm painterly palette, solid #F5C82E mustard yellow background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, scene representing imagination and curiosity

**Slide 4 (aktivite):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, warm parent-child storytelling scene, mother squirrel and baby squirrel sitting together on a cozy armchair reading a big open storybook, soft pillows, large expressive eyes, rosy cheeks, warm painterly palette, solid #F5C82E mustard yellow background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, intimate bedtime story moment

**Slide 5 (CTA):**
> Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby squirrel character smiling and waving cheerfully, sitting on a stack of small colorful storybooks, large expressive eyes, rosy cheeks, warm painterly palette, solid #F5C82E mustard yellow background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, warm friendly farewell scene

## Üretim Notu

Bu çalıştırmada relay (`https://vercel-hf-probe.vercel.app`) HTTP 403 "Host not in allowlist" döndürdü — runner IP'si relay tarafında izinli değil. Görseller üretilemediği için yalnızca metin + layout + prompt + caption commit'lendi. Görselleri tetiklemek için aşağıdaki komutu izinli bir ortamdan çalıştır:

```bash
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek_secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot 2026-05-28-ikindi-15 \
    --branch claude/zen-wozniak-dYlKx \
    --prompts-file /tmp/prompts.json

# Sonra:
git pull --ff-only origin claude/zen-wozniak-dYlKx
python3 scripts/overlay_text.py outputs/2026-05-28-ikindi-15/layout.json
```

`/tmp/prompts.json` içeriği için yukarıdaki 5 prompt'u kullan (sıra önemli).
