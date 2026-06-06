# Sincap Kitap IG — 2026-06-06 Öğle 12:00

## Konu
**diş fırçalatmama** (çocuğun diş fırçalamaya direnci)

## Karakter
Sevimli **kunduz yavrusu** (baby beaver) — 5 slide'da sabit. Belirgin ön dişleri konuyla doğrudan eşleşiyor.

## Palette — HARDAL
- Arka plan: `#F5C82E` (hardal sarısı)
- Aksan: `#8E4FAA` (mor)
- Metin: `#3D2817` (koyu kahve)

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık: **Diş Fırçası**
- Aksan: **İstemem!**
- Alt başlık: *Minik dişler büyük bir macera ister.*

### Slide 2 — Çocuğun Sesi (sevgi)
> "Annemle banyoda kıkır kıkır gülerken zamanı unutuyorum."

### Slide 3 — Çocuğun Sesi (ihtiyaç)
> "Fırça köpürünce karnım gıdıklanıyor, biraz korkuyorum biraz da merak ediyorum."

### Slide 4 — Ebeveyn Notu
> Diş fırçalama bir savaş değil, küçük bir oyun olabilir. Çocuğunuza fırçayı tanıtın, kendisi denesin.
>
> **İpucu:** Aynanın önünde birlikte fırçalayın, taklit en hızlı öğretmen.

### Slide 5 — Kapanış
> "Şimdi yumuşacık dişlerimi parlatmaya gidiyorum! Sincap Kitap'ı takip et 🐿️"

## Higgsfield Prompt'ları (ortak iskelet + slide sahnesi)

**Ortak iskelet:**
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute baby beaver character, soft brown fur, large front teeth gently visible,
big round black eyes, fluffy round body, paddle tail, rosy blush cheeks,
warm painterly palette, solid #F5C82E mustard yellow background,
Marc Boutavant and Oliver Jeffers style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation,
```

**Slide bazlı sahneler:**

1. **Kapak:** baby beaver in dynamic expressive pose holding a tiny purple toothbrush, playfully turning head away with cheeky smile, decorative elements around: soft white toothpaste bubbles, sparkles, mint leaves, tiny stars, 5 to 8 floating accents
2. **Sevgi:** baby beaver and parent beaver in warm loving interaction, giggling together in a cozy bathroom moment, snuggled cheek to cheek with soft towels and tiny purple toothbrush nearby, glowing tender mood
3. **İhtiyaç:** isolated tiny baby beaver, small scale against vast empty mustard background, looking up curiously at a giant floating toothbrush above, vulnerable wide-eyed pose, dwarfed by the brush, a tiny foam bubble drifting nearby
4. **Ebeveyn Notu:** calm cozy bathroom bonding scene, parent beaver sitting on a small wooden stool, baby beaver standing in front of a round mirror, both holding tiny purple toothbrushes, soft warm painterly light, gentle chatting moment, no chaos
5. **Kapanış:** baby beaver waving goodbye with cheerful sparkling smile, tiny purple toothbrush in one paw, standing next to a small neat stack of children's books, happy farewell pose, a couple of mint sparkles around

## Görsel Üretim Durumu — ÖNEMLİ

Bu çalıştırmada **Higgsfield raw görselleri üretilemedi**. Routine sandbox'ının egress allowlist'i, Vercel relay host'unu (`vercel-hf-probe.vercel.app`) bloklayarak `403 host_not_allowed` döndürdü; ayrıca Higgsfield ve Vercel API'ları da aynı sebeple erişilemez durumda.

Mevcut çıktıdaki slide PNG'leri, **placeholder** raw'lar üzerine metin bindirilerek üretildi:
- `assets/gorseller/2026-06-06-ogle-12/slide-{1..5}.png` → solid HARDAL palette + `assets/character-reference.png` (kompozisyon konumu sahneye göre değişir)
- Tipografi, palette ve metin yerleşimi production'a hazır.

**Raw'ları gerçek Higgsfield çıktılarıyla değiştirmek için:**
1. Relay host'una erişimi olan bir ortamdan `prompts.json` ile ADIM 4b'yi tekrar çalıştır:
   ```bash
   SLOT="2026-06-06-ogle-12"
   BRANCH="claude/confident-dijkstra-Ym5bT"
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<gerçek değer>" \
   python3 scripts/relay_api.py submit-batch \
       --slot "$SLOT" --branch "$BRANCH" \
       --prompts-file outputs/2026-06-06-ogle-12/prompts.json
   ```
2. `git pull` ile webhook commit'lerini çek.
3. Aynı `layout.json` ile overlay'i yeniden çalıştır:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-06-06-ogle-12/layout.json
   ```
   Aynı dosyalar üzerine prod kalitesi PNG'ler yazılır — caption, metinler ve layout değişmez.

## Dosyalar
- `outputs/2026-06-06-ogle-12/slide-1.png` … `slide-5.png` — final (placeholder raw üzerine overlay)
- `outputs/2026-06-06-ogle-12/raw/slide-1.png` … `slide-5.png` — placeholder raw'lar
- `outputs/2026-06-06-ogle-12/caption.txt` — Instagram caption + hashtag'ler
- `outputs/2026-06-06-ogle-12/layout.json` — overlay config
- `outputs/2026-06-06-ogle-12/prompts.json` — Higgsfield batch input
- `assets/gorseller/2026-06-06-ogle-12/slide-1..5.png` — raw klasörü (real raw'lar buraya commit'lenecek)
