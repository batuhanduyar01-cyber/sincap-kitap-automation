# Sincap Kitap IG — 2026-05-11 Öğle 12:00

## Meta
- **Tarih / Slot:** 2026-05-11 — öğle 12:00
- **Konu:** Diş fırçalatmama (çocuk perspektifinden)
- **Karakter:** Sevimli genç beyaz tavşan (uzun sarkık kulaklar, pastel pijama)
- **Palette:** MERCAN — bg `#F08A7B`, accent `#8C2E3F`, text `#3D2817`
- **Branch:** `claude/confident-dijkstra-SNaIJ`

## Slide Metinleri

### Slide 1 — KAPAK
- **Ana başlık:** Dişlerimi
- **Aksan:** Fırçalatmam!
- **Alt başlık:** Çocuğun iç sesinden bir sabah.

### Slide 2 — Çocuğun Sesi (sevgi)
> Sabahları seninle uyanmak dünyanın en güzel şeyi anneciğim.

### Slide 3 — Çocuğun Sesi (ihtiyaç)
> Köpük gıdıklıyor, fırça batıyor, her sabah aynı şey neden?

### Slide 4 — Ebeveyn Notu
**Ebeveyn Notu**
Diş fırçalama bir savaş değil, bir oyun olabilir. Fırçayı çocuğunuza seçtirin, yanında siz de fırçalayın; ritim ve eşlik direnci eritir.

### Slide 5 — Kapanış
Pırıl pırıl dişlerle güle güle! Daha çok minik macera için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları (1152x1536, 1080p)

Tüm prompt'larda sabit karakter ve `solid #F08A7B background` kullanıldı. Promptlar `outputs/2026-05-11-ogle-12/prompts.json` dosyasında.

1. **Slide 1 (cover):** rabbit refusing toothbrush, arms crossed, scrunched cheeks, eyes squeezed shut, 5-8 decorative elements (bubbles, sparkles, mini toothbrushes, mint leaves).
2. **Slide 2 (love):** rabbit child snuggled into mama rabbit's chest, both giggling, mama kissing top of head, cozy morning hug.
3. **Slide 3 (need):** isolated small rabbit, tiny scale against vast background, oversized toothbrush, drooping ears, vulnerable shy pose.
4. **Slide 4 (bonding):** cozy bathroom, mama rabbit kneeling next to little rabbit at small sink, brushing teeth together, gentle smiles.
5. **Slide 5 (cta):** rabbit waving goodbye, huge smile with tiny clean teeth, small stack of three storybooks, sparkles.

## Ham Görsel Üretimi — NOT

**Bu çalıştırmada relay erişimi bloklu**: `RELAY_URL=https://vercel-hf-probe.vercel.app` adresine yapılan submit `HTTP 403 — "Host not in allowlist"` döndü. Bu, sandbox/runner IP'sinin Vercel relay'in IP allowlist'inde bulunmadığını gösteriyor (secret kabul edildi; reddedilen IP). Bu nedenle gerçek Higgsfield illüstrasyonları üretilemedi. Yerine `assets/gorseller/2026-05-11-ogle-12/slide-{1..5}.png` olarak **düz `#F08A7B` placeholder PNG'ler** oluşturuldu ve overlay pipeline'ı bunların üzerine çalıştırıldı.

Görseller üretilmek istendiğinde, yetkili bir ortamdan şu komut yeniden çalıştırılabilir:

```bash
SLOT="2026-05-11-ogle-12"
BRANCH="claude/confident-dijkstra-SNaIJ"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-11-ogle-12/prompts.json
```

Sonrasında `git pull` + `python3 scripts/overlay_text.py layout.json` ile final slide'lar yeniden üretilir.

## Çıktılar
- `outputs/2026-05-11-ogle-12/slide-1.png` .. `slide-5.png` (placeholder ham görsel + overlay)
- `outputs/2026-05-11-ogle-12/caption.txt`
- `outputs/2026-05-11-ogle-12/icerik.md` (bu dosya)
- `outputs/2026-05-11-ogle-12/prompts.json` (5 Higgsfield promptu)
- `outputs/2026-05-11-ogle-12/raw/` — boş; gerçek üretim yapıldığında ham PNG'ler buraya kopyalanır
