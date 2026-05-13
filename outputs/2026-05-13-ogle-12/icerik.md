# Sincap Kitap IG — 2026-05-13 Öğlen 12:00

**Konu:** Diş Fırçalatmama (çocuk ağzından)
**Ton:** Çocuk odaklı, eğlenceli, oyunsu — çocukla birlikte okunabilir
**Karakter:** Sevimli tavşan yavrusu (iki minik ön diş, krem rengi yumuşak tüy)

## Palette

| Rol     | Hex       | Ad                |
|---------|-----------|-------------------|
| bg      | `#C9DDEC` | Toz Mavisi (zemin)|
| accent  | `#F08A7B` | Mercan            |
| text    | `#3D2817` | Sıcak koyu kahve  |

5 slide boyunca aynı palette sabit kullanılır. Toz mavisi banyo / tazelik / sakinlik çağrışımı; mercan vurgular için sıcak kontrast verir.

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** "Dişlerimi"
- **title_accent:** "Fırçalamak İstemiyorum!"
- **subtitle:** "...ama belki birazcık."
- *(çocuğun pofuduk, isteksiz ama sevimli iç sesi)*

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Annemle yan yana fırçalayınca gülüyoruz, bu en sevdiğim an."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Dişlerim küçücük, fırçam koskoca... yalnız başaramıyorum."

### Slide 4 — EBEVEYN NOTU
- **title_accent:** "Ebeveyn Notu"
- **body:** "Diş fırçalama bir savaş değil, küçük bir oyun olabilir. Şarkıyla, aynanın önünde birlikte mikrop kovalayın. İpucu: kendi fırçasını çocuğunuz seçsin; sahiplenme direnci eritir."

### Slide 5 — KAPANIŞ
> "Artık dişlerim parıl parıl! Sincap Kitap'ı takip et 🐿️"

## Higgsfield Görsel Prompt'ları

Her prompt ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute fluffy bunny rabbit character, two small visible front teeth, soft cream-white fur,
pink rosy cheeks, big shiny eyes, large expressive eyes, rosy blush cheeks,
warm painterly palette, solid #C9DDEC background,
Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames,
portrait orientation, {SAHNE}
```

| Slide | Sahne |
|-------|-------|
| 1 | bunny in dynamic pose, holding tiny toothbrush at arm's length, playful pouting hesitant expression, 6 dekoratif öğe (köpük baloncuk, parıltı, minik diş şekli, mavi damla) |
| 2 | bebek tavşan + anne tavşan yan yana fırçalıyor, köpük bıyıkları, kıkırdayarak yanak yanağa, etrafta kalpler ve baloncuklar |
| 3 | tek başına minik tavşan, devasa fırçanın önünde, bol negatif alan, çekingen büyük gözlerle yukarı bakıyor |
| 4 | anne tavşan diz çökmüş, çocuğun elini fırçada nazikçe yönlendiriyor, sıcak gece banyosu, küçük tabure ve fırça bardağı |
| 5 | tavşan el sallıyor, gururlu gülümseme, iki pırıl pırıl ön diş, yanında 3 kitaplık küçük yığın |

## Higgsfield Submit Notu

Bu çalıştırmada `https://vercel-hf-probe.vercel.app` relay'i HTTP 403 `x-deny-reason: host_not_allowed` döndürdü (POST /api/hf/submit, GET /api/hf/status ve GET / hepsi). Relay'in Vercel tarafındaki host/IP allowlist'i bu oturumun kaynak IP'sini kapsamıyor; auth/secret değil edge'deki engelleme. Görsel üretimi atlandı, metin pipeline'ı yine de commit'lendi.

Relay açıldığında /tmp/prompts.json zaten hazır (bkz. `raw/prompts.json`). Pipeline:
```
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
  --slot 2026-05-13-ogle-12 \
  --branch claude/confident-dijkstra-lpajt \
  --prompts-file outputs/2026-05-13-ogle-12/raw/prompts.json
```

Submit OK'lendikten sonra:
```
python3 scripts/overlay_text.py outputs/2026-05-13-ogle-12/raw/layout.json
```
