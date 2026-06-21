# Sincap Kitap IG Post — 2026-06-21 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş tantrum yönetimi)

## Palette
**AHUDUDU** — bg `#E63B5C`, accent `#C5E86C` (yeşil), text beyaz

## Karakter
Bear cub (5 slide boyunca sabit)

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** İçindeki **Fırtına**
- **Alt başlık:** Öfke nöbeti, küçük yüreğin büyük yüküdür.

### Slide 2 — TANIDIK SAHNE
Markette istediği oyuncağı alamadı. Yere yattı, çığlık attı. Tüm gözler üzerinizde. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ (alıntı)
"İçimde kocaman bir öfke var, ama ona ne yapacağımı bilmiyorum."

### Slide 4 — UNUTMAYIN!
Öfke nöbeti çocuğun inadı değil, gelişen beyninin işidir. 6 yaş öncesi duyguları düzenleyen alan henüz olgunlaşmamıştır. Bugün: diz çöküp göz hizasına inin, "Buradayım, seni anlıyorum" deyin. Çözüm sonradan gelir.

### Slide 5 — KAPANIŞ (CTA)
Fırtınadan sonra gökkuşağı gelir, sevgili anne. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompts
Bkz. `prompts.json` — 5 slide için ortak iskelet (watercolor gouache, AHUDUDU `#E63B5C` arka plan, bear cub karakter), her slide farklı sahne (hopeful hill / mother hug / vulnerable alone / family reading / waving goodbye).

## ⚠️ ÇALIŞMA DURUMU — BLOKLANDI

**ADIM 4b başarısız.** Higgsfield relay'i (`vercel-hf-probe.vercel.app`) bu Routine ortamının network egress allowlist'inde değil. Submit denemesi 403 döndü:

```
Host not in allowlist: vercel-hf-probe.vercel.app. Add this host to your network egress settings to allow access.
```

### Çözüm yolu
Routine'ın çalıştığı ortamın network policy ayarlarına `vercel-hf-probe.vercel.app` host'unu allowlist olarak ekle. Sonra:

1. Bu repo'nun bu branch'ini güncel tut: `claude/quirky-mendel-s8r95s`
2. Routine'ı tekrar tetikle (veya manuel olarak):

```bash
SLOT="2026-06-21-sabah-9"
BRANCH="claude/quirky-mendel-s8r95s"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel'deki gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot   "$SLOT" \
    --branch "$BRANCH" \
    --prompts-file outputs/2026-06-21-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-06-21-sabah-9/layout.json
```

Hazır olan dosyalar (`outputs/2026-06-21-sabah-9/`):
- `prompts.json` — Higgsfield için 5 prompt
- `layout.json` — overlay konfigürasyonu
- `caption.txt` — Instagram caption + hashtag'ler
- `icerik.md` — bu dosya
