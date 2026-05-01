# 2026-05-01 — İkindi 15:00 — Hayal Gücü

**Slot:** `2026-05-01-ikindi-15`
**Konu:** Hayal Gücü (0-6 yaş)
**Palette:** TURUNCU — bg `#E97E28`, accent `#FFFFFF`, text `#2A1810`
**Ton:** Sıcak anne + bilge arkadaş, pedagojik ipucu ağırlıklı

## Slide metinleri

### Slide 1 — KAPAK
- **title_main:** Çocuğunuzun Hayal Gücü
- **title_accent:** Bir Hazinedir
- **subtitle:** Küçük zihinlerin sınırsız dünyası nasıl beslenir.

### Slide 2 — ÇERÇEVE
> Çocuklar hayalleriyle dünyayı yeniden kurar. Bir karton kutu uzay gemisi, bir sopa sihirli değnek olur. Bu güç, geleceğin yaratıcı aklını yetiştirir.

### Slide 3 — ANAHTAR KAVRAM: Yaratıcılık
> Hayal gücü, problem çözmenin tohumudur. "Olmayanı düşünme" yeteneği, hayatta yeni yollar açar.

### Slide 4 — UNUTMAYIN!
> Hayalin yanlışı yoktur. "Gerçekten öyle olmaz" demek yerine hikayesine eşlik edin. **Bu akşam:** Birlikte bir kutudan ev yapın ve içinde bir maceraya çıkın.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Görsel sahneleri (Higgsfield için)

| # | Sahne |
|---|-------|
| 1 | Sincap karakter elinde kağıt gemiyle, etrafında küçük yıldız/tüy/kitap |
| 2 | Karton kutu içinde tilki yavrusu (uzay gemisi), tavşan arkadaş tahta kaşıkla mikrofon, oyuncaklar |
| 3 | Ayı yavrusu dev bir gökkuşağı boyuyor, kirpi boya karıştırıyor, kuş boya damlaları arasından uçuyor |
| 4 | Anne tavşan ve yavrusu birlikte battaniyelerden kale kuruyor, peri ışıkları |
| 5 | Sıcak gülümseyen sincap, küçük kitap yığını, sıcak süt |

## Durum: ⚠️ ADIM 4 BLOKLU

Higgsfield görsel üretimi tamamlanamadı. Routine sandbox'ının outbound HTTP allowlist'i `vercel-hf-probe.vercel.app` host'unu engelliyor:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
```

Aynı blok `*.vercel.app`, `higgsfield.ai`, `api.higgsfield.ai` için de geçerli (curl HTTP 403 döndü).

**Çözüm:** Routine sandbox'ının outbound proxy konfigürasyonuna `vercel-hf-probe.vercel.app` (en azından `*.vercel.app`) eklenmesi gerekiyor. Eklendikten sonra `outputs/2026-05-01-ikindi-15/prompts.json` ve `outputs/2026-05-01-ikindi-15/layout.json` ile tekrar çalıştırma:

```bash
export SLOT="2026-05-01-ikindi-15"
export BRANCH="claude/zen-wozniak-ts8Rs"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<vercel env değeri>"

python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-01-ikindi-15/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-01-ikindi-15/layout.json
```

## layout.json (gitignore'da olduğu için içerik buraya gömüldü)

Yeniden çalıştırma öncesi `outputs/2026-05-01-ikindi-15/layout.json` dosyasını şu içerikle oluşturun:

```json
{
  "output_dir": "outputs/2026-05-01-ikindi-15",
  "palette": {
    "bg": "#E97E28",
    "accent": "#FFFFFF",
    "text": "#2A1810"
  },
  "slides": [
    {
      "raw_image": "assets/gorseller/2026-05-01-ikindi-15/slide-1.png",
      "output": "outputs/2026-05-01-ikindi-15/slide-1.png",
      "type": "cover",
      "title_main": "Çocuğunuzun Hayal Gücü",
      "title_accent": "Bir Hazinedir",
      "subtitle": "Küçük zihinlerin sınırsız dünyası nasıl beslenir.",
      "decorations": true
    },
    {
      "raw_image": "assets/gorseller/2026-05-01-ikindi-15/slide-2.png",
      "output": "outputs/2026-05-01-ikindi-15/slide-2.png",
      "type": "inner",
      "body": "Çocuklar hayalleriyle dünyayı yeniden kurar. Bir karton kutu uzay gemisi, bir sopa sihirli değnek olur. Bu güç, geleceğin yaratıcı aklını yetiştirir."
    },
    {
      "raw_image": "assets/gorseller/2026-05-01-ikindi-15/slide-3.png",
      "output": "outputs/2026-05-01-ikindi-15/slide-3.png",
      "type": "concept",
      "title_accent": "Yaratıcılık",
      "body": "Hayal gücü, problem çözmenin tohumudur. 'Olmayanı düşünme' yeteneği, hayatta yeni yollar açar."
    },
    {
      "raw_image": "assets/gorseller/2026-05-01-ikindi-15/slide-4.png",
      "output": "outputs/2026-05-01-ikindi-15/slide-4.png",
      "type": "tip",
      "title_accent": "UNUTMAYIN!",
      "body": "Hayalin yanlışı yoktur. 'Gerçekten öyle olmaz' demek yerine hikayesine eşlik edin. Bu akşam: Birlikte bir kutudan ev yapın ve içinde bir maceraya çıkın."
    },
    {
      "raw_image": "assets/gorseller/2026-05-01-ikindi-15/slide-5.png",
      "output": "outputs/2026-05-01-ikindi-15/slide-5.png",
      "type": "cta",
      "body": "Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️"
    }
  ]
}
```
