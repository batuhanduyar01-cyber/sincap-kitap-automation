# Sincap Kitap IG — 2026-06-21 Öğle 12:00

## Konu
**Diş fırçalatmama** (çocuğun bakış açısından)

## Karakter
Tavşan (uzun yumuşak kulaklı, büyük gözlü)

## Palette — HARDAL
| Rol | Hex |
|---|---|
| Arka plan | `#F5C82E` (hardal sarısı) |
| Aksan | `#8E4FAA` (mor) |
| Metin | `#3D2817` (koyu kahve) |

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Dişlerim Pırıl
- **title_accent:** Pırıl Parlasın!
- **subtitle:** Tavşan bile fırçasını çok seviyor.

### Slide 2 — ÇOCUĞUN SESİ (sevgi)
> "Sen bana fırçayı uzatınca gülümsüyorum, çünkü her şeyi seninle yapmak güzel."

### Slide 3 — ÇOCUĞUN SESİ (ihtiyaç)
> "Bazen acelem var, bazen köpük gözüme kaçıyor. Bana biraz zaman ver."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**
Diş fırçalamak bir görev değil, küçük bir oyun olabilir. Ayna karşısında birlikte fırçalayın, kısa bir şarkı söyleyin.

**İpucu:** Çocuğunuza kendi fırçasını seçtirin, bu sorumluluğu sahiplenmesini kolaylaştırır.

### Slide 5 — KAPANIŞ
Yarın dişlerim yine parıl parıl olacak! Daha fazla macera için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bunny character with long soft ears, large expressive eyes, rosy blush cheeks,
warm painterly palette, solid #F5C82E mustard yellow background,
Marc Boutavant and Oliver Jeffers style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation,
{SAHNE}
```

| # | Sahne |
|---|---|
| 1 | Bunny in dynamic joyful pose holding a giant purple toothbrush, mouth open showing sparkling clean teeth, decorative tiny bubbles, sparkles, mint leaves and toothpaste swirls floating around |
| 2 | Child bunny and parent bunny brushing teeth together in front of a small bathroom mirror, both giggling warmly, parent gently guiding child's hand, foam puffs around their mouths, cozy loving interaction |
| 3 | Tiny isolated bunny holding a single toothbrush, small scale against vast empty mustard yellow space, looking down hesitantly, ears slightly drooped, emotional vulnerable pose |
| 4 | Calm cozy scene of parent bunny and child bunny at a small wooden sink, parent kneeling at eye level, both smiling, toothpaste tube and a tiny cup nearby, soft warm light |
| 5 | Bunny waving goodbye with one paw, cheerful big smile showing pearly teeth, standing next to a small stack of storybooks, toothbrush tucked behind one ear |

JSON formundaki tam prompt seti: `raw/higgsfield-prompts.json`

## Hashtag'ler

`#sincapkitap #çocukkitabı #resimlikitap #okulöncesi #06yaş #dişfırçalama #çocukbakımı #ebeveynipuçları #çocukgelişimi #çocukrutini #özbakım #sağlıklıçocuk #küçükkahraman #masalkitabı #çocukpsikolojisi #anneblog #babablog #okumakeyfi #yumuşakebeveynlik #çocuklaokuma`

## Üretim Durumu

**HİGGSFIELD GÖRSELLERİ ÜRETİLEMEDİ** — Vercel relay (`vercel-hf-probe.vercel.app`) bu remote execution environment'ın network egress allowlist'inde yok:

```
[relay_api] submit HTTP 403:
{"_raw": "Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access."}
```

Yapılması gereken: Routine ortamı network egress ayarlarına `vercel-hf-probe.vercel.app` host'unun eklenmesi. Sonra bu branch'te tek başına relay komutu yeniden çalıştırılabilir:

```bash
SLOT="2026-06-21-ogle-12"
BRANCH="claude/confident-dijkstra-lxshow"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file outputs/$SLOT/raw/higgsfield-prompts.json
```

5 PNG `assets/gorseller/2026-06-21-ogle-12/slide-{1..5}.png` olarak commit'lendikten sonra:

```bash
python3 scripts/overlay_text.py outputs/2026-06-21-ogle-12/layout.json
```
