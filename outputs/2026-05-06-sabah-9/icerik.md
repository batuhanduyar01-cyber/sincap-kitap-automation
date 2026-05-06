# Sincap Kitap IG — 2026-05-06 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**TOZ MAVİSİ**
- Arka plan: `#C9DDEC`
- Aksan: `#E97E28` (turuncu)
- Metin: `#3E2A1F` (koyu kahve)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — Kapak
- **Ana başlık:** Bir Türlü
- **Aksan:** Uyumuyor mu?
- **Alt başlık:** Direnç değil, dünyaya doyamamak gibi.

### Slide 2 — Tanıdık Sahne
> Saat 22:00 olmuş, sen yorgunsun, ama o hâlâ zıplıyor. "Bir kitap daha," diyor küçük el. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun Sesi
> "Gözlerimi kapatınca, gün hâlâ bitmemiş gibi geliyor."

### Slide 4 — UNUTMAYIN!
> Uykuya direnç, gelişimin doğal bir aşamasıdır. Tutarlı ritüeller küçük bir bedeni güvene davet eder. Bugün: Yatmadan 30 dakika önce ışıkları kıs, sıcak bir hikâye aç.

### Slide 5 — Kapanış
> Her uyku, sevgiyle örülen bir kucaktır. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar

Tüm prompt'lar ortak iskelet + slide'a özel sahneyle. Karakter `bear cub`, arka plan `#C9DDEC`.

**Slide 1:** big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful

**Slide 2:** bear cub character with mother bear character, warm hugging interaction, cozy indoor scene

**Slide 3:** small isolated bear cub character, emotional vulnerable pose, vast empty space around (scale contrast), looking up

**Slide 4:** bear family scene, parent bear and bear cub reading book together, warm cozy bedroom setting

**Slide 5:** bear cub character waving goodbye, smiling, sitting on a book stack

Tam JSON: `outputs/2026-05-06-sabah-9/prompts.json`

## Hashtag'ler
`#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #uykudirenci #çocukuykusu #anneolmak #annelikgünlüğü #çocukgelişimi #okulöncesi #annetavsiyesi #uykurutini #yatmadanönce #çocukpsikolojisi #annebabaolmak #kitapokuyançocuk #pedagoji #sevgidolu #uykumasalı`

## Çıktı Durumu

| Adım | Durum |
|---|---|
| Konu seçimi & log | ✅ `logs/sabah-9.md` güncel |
| Metin üretimi | ✅ |
| Palette seçimi | ✅ TOZ MAVİSİ |
| Higgsfield prompts | ✅ `outputs/2026-05-06-sabah-9/prompts.json` |
| Higgsfield submit (relay) | ❌ **BLOKE** — egress proxy `vercel-hf-probe.vercel.app` host'unu allowlist'te göstermiyor (HTTP 403 "Host not in allowlist") |
| `assets/gorseller/2026-05-06-sabah-9/slide-*.png` | ⏳ Beklemede (relay için) |
| `overlay_text.py` | ⏳ Beklemede (raw görseller için) |
| Final `outputs/2026-05-06-sabah-9/slide-*.png` | ⏳ Beklemede |

## Devam Adımları (Network açıldıktan sonra)

```bash
export SLOT="2026-05-06-sabah-9"
export BRANCH="claude/quirky-mendel-ILujs"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<gerçek-secret>"

python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-06-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-06-sabah-9/layout.json
```
