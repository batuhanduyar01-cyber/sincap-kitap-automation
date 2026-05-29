# Sincap Kitap IG — 2026-05-29 İkindi 15:00

- **Konu:** Kitap okuma alışkanlığı
- **Ton:** Sıcak anne + bilge arkadaş (pedagojik ipucu ağırlıklı)
- **Palette:** MERCAN — bg `#F08A7B`, accent `#F5E9D4` (krem), text `#2A1810` (koyu kahve)
- **Karakter:** bear cub (ayı yavrusu)

## Slide metinleri

### Slide 1 — KAPAK
- title_main: **Her Akşam**
- title_accent: **Bir Sayfa Yeter**
- subtitle: Kitap sevgisi, küçük anlardan büyür.

### Slide 2 — ÇERÇEVE
> Çocuğun kitapla tanışması, bir kitabı bitirmekten çok onunla geçirilen zamandır. Sayfaların sıcaklığını duyduğunda kitap onun arkadaşı olur.

### Slide 3 — ANAHTAR KAVRAM
- Başlık: **Ritim**
- Açıklama: Her gün aynı saatte, aynı koltukta okumak. Bu küçük ritüel, çocuğun beynine "bu an benim için" der.

### Slide 4 — UNUTMAYIN!
> Okumayı sevdirmek için kitabı bitirmek zorunda değiliz. Bazen tek bir resim de yeter. **Bu akşam deneyin:** Çocuğunuzla bir resimli kitabın sadece kapağını birlikte konuşun, hikâyeyi siz birlikte uydurun.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Hashtag listesi (20)

#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #pedagoji #kitapokumaalışkanlığı #okumakeyfi #kitapsevgisi #çocukgelişimi #okulöncesi #yatakönceokuması #aileokuması #masalvakti #çocuklakitap #küçükokurlar #bilgeebeveyn #sıcakanne #huzurluakşam #okumaritüeli

## Üretim durumu

- ✅ Konu seçimi + log güncellemesi (`logs/ikindi-15.md`)
- ✅ Metin üretimi (5 slide + caption + hashtag'ler)
- ✅ Higgsfield prompt'ları yazıldı (`outputs/2026-05-29-ikindi-15/prompts.json`)
- ⚠️ **Higgsfield illustrasyonları üretilemedi** — Vercel relay 403 "Host not in allowlist" döndü. Bu Claude Code web ortamının IP'si relay allowlist'inde değil ve `RELAY_SHARED_SECRET` prompt'taki placeholder değer (`78e1e773...`) gerçek değil. Yer tutucu olarak palette renginde (`#F08A7B`) düz arka planlı PNG'ler kullanıldı.
- ✅ Layout JSON (`outputs/2026-05-29-ikindi-15/layout.json`)
- ✅ PIL overlay çalıştırıldı, 5 slide üretildi (default font ile — gerçek font'lar `assets/fonts/` içinde mevcut değil)

## Gerçek illüstrasyonları üretmek için (Routine UI'de)

```bash
export SLOT="2026-05-29-ikindi-15"
export BRANCH="claude/zen-wozniak-UFGuM"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<Vercel'deki gerçek değer>"
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-05-29-ikindi-15/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-29-ikindi-15/layout.json
```
