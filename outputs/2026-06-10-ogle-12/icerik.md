# Sincap Kitap IG — 2026-06-10 Öğle 12:00

**Konu:** Yatmayı istememe
**Karakter:** Sevimli uykulu ayı yavrusu (pijamalı)
**Palette:** MOR — bg `#7E5BA0` / accent `#F5C82E` (hardal) / text `#FFF4D6` (krem)

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık: **Niye Hep Yatmalıyım?**
- Vurgu: "Yatmalıyım?" (hardal renkte)
- Alt başlık: "Uyku zamanı çocuğun gözünden."

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Senin yanında uyumak en güvenli yerim."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Gözlerim yoruldu ama beynim hâlâ koşuyor."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu:** Çocuğunuz yatmak istemez çünkü günü bitirmek, sizinle vedalaşmak demektir. Sakin bir rutin (banyo, kitap, kısık ışık) güven verir.
**İpucu:** Her gece aynı kitabı okuyun; tekrar uyutur.

### Slide 5 — KAPANIŞ
"İyi geceler! Yarın yine birlikte oynayalım. Sincap Kitap'ı takip et 🐿️"

## Görseller (Higgsfield)

Slide bazlı sahneler (karakter: sleepy bear cub, palette bg: `#7E5BA0`):

1. Pijamalı ayıcık esnerken, ufak teddy, etrafta ay/yıldız/parıltı dekorasyonları.
2. Ayıcık + anne ayı kucaklaşma, sıcak yatak anı.
3. Yalnız ayıcık devasa yatağın üstünde, dizlerini sarılmış, savunmasız.
4. Anne ayı yatak başında kitap okuyor, yumuşak abajur ışığı.
5. Ayıcık el sallıyor, küçük kitap yığını yanında.

## Dosyalar

- `slide-1.png` … `slide-5.png`
- `caption.txt`
- `layout.json`
- `raw/` — ham Higgsfield çıktıları (regenerate edildiğinde kopyalanır)

## ⚠️ Üretim Notu — Higgsfield Relay

Bu çalışmada Higgsfield illüstrasyonları **üretilemedi**. Vercel relay'e
yapılan istek `403 "Host not in allowlist"` ile reddedildi. Sebebi:
routine prompt'undaki `RELAY_SHARED_SECRET` değeri hâlâ placeholder
string (`78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4`).
Bu değer, Routine UI'de prompt yapıştırılırken Vercel
(`vercel-hf-probe` → Env → `RELAY_SHARED_SECRET`) gerçek değeriyle
değiştirilmemiş.

**Yapılması gereken:**
1. Vercel'den gerçek `RELAY_SHARED_SECRET` değerini al, Routine prompt'unda
   placeholder ile değiştir.
2. Aşağıdaki komutu tekrar çalıştır:
   ```bash
   RELAY_URL="https://vercel-hf-probe.vercel.app" \
   RELAY_SHARED_SECRET="<GERCEK_DEGER>" \
   python3 scripts/relay_api.py submit-batch \
     --slot 2026-06-10-ogle-12 \
     --branch claude/confident-dijkstra-axm0e6 \
     --prompts-file /tmp/prompts.json
   ```
3. PNG'ler `assets/gorseller/2026-06-10-ogle-12/slide-*.png` üzerine yazılır
   (mevcut placeholder solid-color dosyaları override edilir).
4. `python3 scripts/overlay_text.py outputs/2026-06-10-ogle-12/layout.json`
   yeniden çalıştırılarak final carousel üretilir.

Şu anki `outputs/2026-06-10-ogle-12/slide-*.png` dosyaları **solid mor
background + metin** taşıyor; final illüstrasyonlu hâli değil.
