# Sincap Kitap IG — 2026-06-14 Sabah 09:00

## Konu
**öfke nöbetleri** (tantrums) — 0-6 yaş

## Palette
**AHUDUDU**
- Arka plan: `#E63B5C`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
**bear cub** (ayı yavrusu) — tüm slide'larda sabit

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Küçük Kalp,
- **title_accent:** Büyük Dalga!
- **subtitle:** Öfke nöbetleri, henüz kelimesi olmayan duygulardır.

### Slide 2 — TANIDIK SAHNE
> Markette sıraya girerken aniden yere atıyor kendini. Etraf size bakıyor, kalbiniz daralıyor. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "İçimde büyük bir dalga var; durduramıyorum, sadece bağırabiliyorum."

### Slide 4 — UNUTMAYIN
- **title:** UNUTMAYIN!
- **body:** Öfke nöbeti yaramazlık değil, gelişimin doğal bir parçasıdır. Siz sakin kaldıkça çocuğunuz da öğreniyor. Bugün: nöbet geçerken sessizce yanına oturup elini tutmayı deneyebilirsiniz.

### Slide 5 — KAPANIŞ
> Bu duygu kasırgasında yalnız değilsin. Birlikte yumuşatabiliriz. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar (5 slide)

Ortak iskelet — `solid #E63B5C background`, `bear cub` karakter, watercolor gouache, Oliver Jeffers + Marc Boutavant stili.

1. **Slide 1:** big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful
2. **Slide 2:** bear cub character with mother bear character, warm hugging interaction, cozy indoor scene
3. **Slide 3:** small isolated bear cub character, emotional vulnerable pose, vast empty space around with scale contrast, looking up
4. **Slide 4:** family scene, mother bear and bear cub reading book together, warm cozy bedroom setting
5. **Slide 5:** bear cub character waving goodbye, smiling, sitting on a stack of books

## Durum
⚠️ **Higgsfield görselleri üretilemedi.** Vercel relay host (`vercel-hf-probe.vercel.app`) bu environment'ın egress allowlist'inde değil — submit anında HTTP 403 ("Host not in allowlist") döndü. Bu yüzden `assets/gorseller/2026-06-14-sabah-9/slide-*.png` dosyaları henüz oluşturulmadı ve `scripts/overlay_text.py` çalıştırılmadı.

### Devam etmek için
1. Routine environment'ının network egress allowlist'ine `vercel-hf-probe.vercel.app` host'unu ekle.
2. Bu prompt'u tekrar çalıştır — `/tmp/prompts.json` ve `layout.json` aynı içerikle yeniden üretilebilir.
3. Alternatif: yerel makinede `python3 scripts/relay_api.py submit-batch --slot 2026-06-14-sabah-9 --branch claude/quirky-mendel-vylwvd --prompts-file /tmp/prompts.json` (env'leri set ettikten sonra) çalıştır → görseller branch'e commit'lenince `python3 scripts/overlay_text.py outputs/2026-06-14-sabah-9/layout.json` ile metni bindir.
