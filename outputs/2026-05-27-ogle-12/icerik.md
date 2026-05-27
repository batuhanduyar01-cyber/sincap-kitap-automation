# Sincap Kitap IG — 2026-05-27 Öğle 12:00

## Konu
**Banyo direnci** — çocuğun banyoya/duşa gitmek istememesi, su sesi/köpük hissi tetikleyicileri.

## Palette
**TOZ MAVİSİ** — sakin, banyo/su temasına uygun
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3D2817` (koyu kahve)

## Karakter
Sevimli baby hedgehog (minik kirpi) + slide 2'de yardımcı karakter olarak sarı ördek.

## Slide Metinleri

### Slide 1 — KAPAK
- Ana başlık: **Banyo mu?**
- Aksan: **Yine mi?!**
- Alt başlık: "Köpükler gelmeden saklanıyorum."

### Slide 2 — Çocuğun sesi 1 (sevgi)
> "Aslında küvetteki ördekleri çok seviyorum."

### Slide 3 — Çocuğun sesi 2 (ihtiyaç)
> "Suyun şıpır şıpır sesi bana garip geliyor."

### Slide 4 — Ebeveyn Notu
"Banyo direnci çoğu zaman su sesinden ya da köpük hissinden gelir. Aceleye getirmeyin, oyuncak getirin, şarkı söyleyin. Bu akşam: küvet kenarına oturup elini suya değdirmesini bekleyin."

### Slide 5 — Kapanış
"Banyo macerası daha eğlenceli olsun diye Sincap Kitap'ı takip et 🐿️"

## Higgsfield Prompt'lar

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby hedgehog character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #C9DDEC background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation`

- **Slide 1:** + `peeking out from behind a small fluffy towel with a surprised playful expression, 6 decorative bath bubbles and water droplets floating around, small soap suds, dynamic expressive pose`
- **Slide 2:** + `hugging a small yellow rubber duck character in warm loving interaction, both giggling cheek to cheek, cozy bathtime mood`
- **Slide 3:** + `isolated tiny baby hedgehog, sitting on a small folded towel, small scale against vast empty background, emotional vulnerable pose, looking up curiously and a bit unsure`
- **Slide 4:** + `calm adult hedgehog parent and baby hedgehog scene, cozy bonding bathtime moment, parent gently pouring water from a small cup while baby hedgehog smiles, sitting next to a small wooden tub with bubbles`
- **Slide 5:** + `waving goodbye with a cheerful smile, standing next to a small stack of storybooks with a tiny yellow rubber duck perched on top`

Boyut: `1152x1536`, kalite: `1080p`.

## ÖNEMLİ — Görsel Üretimi Yapılamadı (Sandbox Network Bloku)

Bu Routine ortamından **`https://vercel-hf-probe.vercel.app` ve `https://api.higgsfield.ai` HTTPS isteklerine outbound network policy 403 "Host not in allowlist"** dönüyor (sadece github.com erişilebiliyor). Higgsfield submit-batch ADIM 4 başarısız oldu; `assets/gorseller/2026-05-27-ogle-12/` dizini boş.

### Lokal'de tamamlamak için (network erişimi olan terminalden):

```bash
git fetch origin claude/confident-dijkstra-erHMs
git checkout claude/confident-dijkstra-erHMs
git pull --ff-only origin claude/confident-dijkstra-erHMs

# /tmp/prompts.json bu repo'da outputs/2026-05-27-ogle-12/prompts.json olarak da kayıtlı.
cp outputs/2026-05-27-ogle-12/prompts.json /tmp/prompts.json

SLOT="2026-05-27-ogle-12"
BRANCH="claude/confident-dijkstra-erHMs"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel'den-gerçek-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json

git pull --ff-only origin "$BRANCH"

python3 scripts/overlay_text.py outputs/2026-05-27-ogle-12/layout.json
```

Bu komut tamamlanınca `outputs/2026-05-27-ogle-12/slide-1.png ... slide-5.png` üretilir.
