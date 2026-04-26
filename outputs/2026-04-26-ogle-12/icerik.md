# Sincap Kitap IG Post — 2026-04-26 Öğle 12:00

## Konu
**Yatmayı istememe** (uyku direnci) — çocuk perspektifinden, ayrılık duygusu çerçevesinde.

## Palette
- Background: **MOR `#7E5BA0`**
- Accent:     **HARDAL `#F5C82E`**
- Text:       **`#FFFFFF`**

## Karakter
Pijamalı, küçük, uykulu bir ayı yavrusu (5 slide boyunca aynı).

## Slide Metinleri

### Slide 1 — Kapak
- **Başlık (ana):** "Uyumak"
- **Başlık (aksan):** "İstemiyorum!"
- **Alt başlık:** "Geceler için minik bir hikâye."

### Slide 2 — Çocuğun Sesi 1 (sevgi)
> "Sen masal okuyunca kalbim ısınıyor, mıknatıs gibi yanına gidiyorum."

### Slide 3 — Çocuğun Sesi 2 (ihtiyaç)
> "Karanlık biraz büyük, ben biraz küçüğüm. Elini tutar mısın?"

### Slide 4 — Ebeveyn Notu
Uyku direnci genelde inat değil, ayrılık duygusudur. Aynı sırayla tekrarlanan
kısa ritüel beyne "güvendesin" der. **İpucu:** Yatmadan 10 dakika önce ekran
kapansın, sadece ses ve dokunuş kalsın.

### Slide 5 — Kapanış
"Tatlı rüyalar, küçük dost. Yarın yine maceralar! Sincap Kitap'ı takip et 🐿️"

## Çıktılar
- `outputs/2026-04-26-ogle-12/slide-1.png`
- `outputs/2026-04-26-ogle-12/slide-2.png`
- `outputs/2026-04-26-ogle-12/slide-3.png`
- `outputs/2026-04-26-ogle-12/slide-4.png`
- `outputs/2026-04-26-ogle-12/slide-5.png`
- `outputs/2026-04-26-ogle-12/caption.txt`
- `outputs/2026-04-26-ogle-12/layout.json`
- `outputs/2026-04-26-ogle-12/raw/higgsfield-prompts.json`

## Higgsfield Görsel Üretimi — Durum
**Relay erişilemedi.** `https://vercel-hf-probe.vercel.app` Routine container'ının
giden trafik allowlist'inde değil; `/api/hf/submit` ve `/` dahil tüm path'ler
HTTP 403 `Host not in allowlist` döndürdü (relay/Cloudflare değil, container
egress proxy'sinin verdiği yanıt).

Bu nedenle slide arka planları, palet rengi (#7E5BA0) ile dolu placeholder
PNG'lerle üretildi (üst yarıda hafif noktalar). Hazırlanan 5 Higgsfield prompt'u
`raw/higgsfield-prompts.json` içinde saklandı; relay erişimi açıldığında aynı
slot için yeniden submit edilebilir:

```bash
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
  --slot 2026-04-26-ogle-12 \
  --branch claude/confident-dijkstra-FFkKY \
  --prompts-file outputs/2026-04-26-ogle-12/raw/higgsfield-prompts.json
```

PNG'ler `assets/gorseller/2026-04-26-ogle-12/slide-N.png` dosyalarını
override eder; ardından `python3 scripts/overlay_text.py outputs/2026-04-26-ogle-12/layout.json`
yeniden çalıştırılarak final slide'lar yenilenebilir.
