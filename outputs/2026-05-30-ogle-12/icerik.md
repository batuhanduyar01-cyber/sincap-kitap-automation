# Sincap Kitap IG — 2026-05-30 Öğle 12:00

## Konu
**Diş fırçalatmama** (çocuğun banyoda diş fırçalamaya direnç göstermesi)

Çocuk perspektifinden, eğlenceli ve oyunsu tonda. Çocuğun iç sesi alıntı ağırlıklı işlendi.

## Palette
**MERCAN** — sıcak, dostane, "tıbbi" hissi vermeyen pembe-mercan.

| Rol | Hex |
|---|---|
| Arka plan (bg) | `#F08A7B` |
| Aksan (accent) | `#FFF4E6` krem |
| Metin (text) | `#3D2817` koyu kahve |

## Karakter
**Baby bear cub** (sevimli ayı yavrusu) — 5 slide boyunca aynı karakter, watercolor/gouache boyalı kitap stili (Marc Boutavant + Oliver Jeffers).

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Dişlerimi
- **Başlık (aksan):** Fırçalamak İstemiyorum!
- **Alt başlık:** Ama belki bir oyun olabilir mi?

### Slide 2 — Çocuğun Sesi 1 (sevgi)
> "Annemle birlikte fırçalarken kahkaha atıyoruz."

### Slide 3 — Çocuğun Sesi 2 (ihtiyaç)
> "Ağzımda köpük olunca biraz korkuyorum, elimi tut."

### Slide 4 — Ebeveyn Notu
- **Başlık:** Ebeveyn Notu
- **Gövde:** Diş fırçalama bir görev değil, küçük bir tören olabilir. Müzik açın, ayna karşısında birlikte fırçalayın. Eğlence, direnci eritir.

### Slide 5 — Kapanış
> Yarın yine birlikte fırçalarız! Sincap Kitap'ı takip et 🐿️

## Higgsfield Görsel Prompt'ları

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #F08A7B coral background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, <SAHNE>
```

| Slide | Sahne |
|---|---|
| 1 | Baby bear in dynamic playful pose with toothbrush like a microphone, 6 decorative elements floating around (bubbles, sparkly stars, tiny soap bubbles, leaves) |
| 2 | Baby bear and mother bear in warm loving interaction, brushing teeth side by side, foam bubbles, laughing together |
| 3 | Isolated small baby bear, small scale against vast empty background, emotional vulnerable pose, reaching out tiny paw, foamy mouth |
| 4 | Calm adult-child bonding moment, parent gently helping baby bear brush teeth in front of a small mirror, soft warm lighting, intimate moment |
| 5 | Baby bear waving goodbye with one paw, cheerful big smile showing clean white teeth, standing next to a small stack of storybooks, holding a tiny toothbrush in the other paw |

Resolution: `1152x1536`, quality `1080p` (her slide için).

## Caption
Tam metin `caption.txt` dosyasında. 300-400 kelime, "çocuğunuzla birlikte okuyun" çağrısı.

## Hashtag'ler
20 adet — `#sincapkitap #çocukkitabı #resimlikitap #okulöncesi #06yaş #dişfırçalama #ebeveynlik #annelik #babalık #çocukgelişimi #pedagoji #sağlıklıalışkanlıklar #çocukrutinleri #anneçocuk #babaçocuk #çocukkitaplari #okuyançocuk #birlikteokuyalım #masal #çocukpsikolojisi`

## Üretim Durumu

| Adım | Durum |
|---|---|
| Konu seçimi + log güncelleme | ✅ |
| Metin üretimi (5 slide + caption + hashtag) | ✅ |
| Palette seçimi (MERCAN) | ✅ |
| `layout.json` | ✅ |
| `caption.txt` | ✅ |
| Higgsfield görselleri (relay üzerinden) | ❌ **NETWORK ALLOWLIST ENGELİ** |
| PIL metin bindirme (overlay_text.py) | ⏸ Görseller bekleniyor |
| Final PNG'ler | ⏸ Görseller bekleniyor |

### Network Engeli Notu
Bu remote execution environment'ın network policy'si `vercel-hf-probe.vercel.app` (ve genel olarak dış host'lar) için outbound trafiği bloke ediyor. Test:

```
$ curl -sI https://vercel-hf-probe.vercel.app/api/hf/status
HTTP/2 403
Host not in allowlist
```

`api.github.com` ve `higgsfield.ai` da aynı şekilde 403 dönüyor. Bu nedenle ADIM 4 (relay submit) ve ADIM 5 (overlay — ham görsel yok) bu session'da koşulamadı.

### Çözüm Yolları
1. Environment'ın network policy'sini Claude Code Web settings'ten genişletip `vercel-hf-probe.vercel.app` host'unu allowlist'e ekleyin, sonra bu prompt'u tekrar çalıştırın.
2. Veya bu repo'yu local'de açıp aynı `RELAY_URL` + `RELAY_SHARED_SECRET` env'leri ile şu komutu çalıştırın:
   ```bash
   SLOT="2026-05-30-ogle-12"
   BRANCH="claude/confident-dijkstra-ZeYok"
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<gerçek_secret>" \
   python3 scripts/relay_api.py submit-batch \
       --slot "$SLOT" --branch "$BRANCH" \
       --prompts-file /tmp/prompts.json
   ```
   `/tmp/prompts.json` içeriği bu dosyadaki "Higgsfield Görsel Prompt'ları" tablosundan üretilebilir; aynısı `outputs/2026-05-30-ogle-12/prompts.json` olarak da bu commit'e konuldu.
3. Görseller `assets/gorseller/2026-05-30-ogle-12/slide-{1..5}.png` olarak commit'lendikten sonra:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-05-30-ogle-12/layout.json
   ```
