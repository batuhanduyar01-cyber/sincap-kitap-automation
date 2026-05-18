# Sincap Kitap IG — 2026-05-18 Öğle 12:00

- **Konu:** karanlık korkusu
- **Ton:** Çocuk odaklı, eğlenceli, oyunsu — alıntı ağırlıklı
- **Karakter:** Minik kirpi (baby hedgehog), 5 slide boyunca aynı
- **Palette:** MOR — arka plan `#7E5BA0` / aksan `#C5E86C` (yeşil) / metin `#FFFFFF` (beyaz)

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): **Karanlıkta**
- Başlık (aksan): **Kim Var?**
- Alt başlık: Işıklar sönünce odam başka bir yer oluyor.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Sen elimi tuttuğunda karanlık bile gülümsüyor."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Minik bir gece lambası ve senin uyku masalın bana yeter."

### Slide 4 — EBEVEYN NOTU
- Başlık: **Ebeveyn Notu**
- Metin: Karanlık korkusu, hayal gücünün büyüdüğünün işaretidir. Korkuyu küçümsemeyin, ona bir isim verin. İpucu: Yatmadan önce odanın gündüz halini birlikte hatırlayın.

### Slide 5 — KAPANIŞ
- Metin: İyi geceler! Karanlık artık benim minik dostum. Sincap'ın maceraları için Sincap Kitap'ı takip et.
- Not: 🐿️ emojisi caption'da kullanılır; slide görseline gömülmez (font emoji glyph'i içermiyor).

## Higgsfield Görsel Prompt'ları (slot: 2026-05-18-ogle-12)

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute baby hedgehog character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #7E5BA0 background, Marc Boutavant and Oliver Jeffers style, storybook art, no text, no frames, portrait orientation, {SAHNE}`

- **Slide 1:** baby hedgehog holding a tiny glowing night light in a dynamic curious brave pose, cozy nighttime bedroom, 6 decorative elements around (stars, crescent moon, sparkles, fireflies), hopeful expression
- **Slide 2:** baby hedgehog snuggled close with a gentle parent hedgehog in a warm loving bedtime hug, cozy nighttime interaction, both giggling with gentle smiles
- **Slide 3:** one tiny isolated baby hedgehog at small scale against a vast dark starry night sky background, emotional vulnerable pose, clutching a tiny blanket and looking up at the darkness
- **Slide 4:** calm cozy scene of a parent hedgehog and baby hedgehog reading a bedtime storybook together by soft warm lamplight, peaceful bonding moment in bed
- **Slide 5:** baby hedgehog waving goodbye with a cheerful sleepy smile, standing next to a small stack of books, holding a softly glowing night light

5 prompt JSON: bu repodaki çalışma sırasında `/tmp/prompts.json` olarak hazırlandı (1152x1536, 1080p).

## Hashtagler

#sincapkitap #çocukkitabı #resimlikitap #okulöncesi #06yaş #karanlıkkorkusu #gecelambası #uykurutini #çocukgelişimi #ebeveynlik #masalsaati #yatmazamanı #çocukpsikolojisi #annelik #babalık #korkularlabaşaçıkma #birliktebüyüyoruz #çocukkitapları

## Üretim Durumu

- ADIM 1-3 (konu, metin, palette): tamamlandı.
- ADIM 4 (Higgsfield görselleri): **tamamlanamadı.** Vercel relay (`vercel-hf-probe.vercel.app`)
  bu ortamın ağ politikası tarafından bloklandı (HTTP 403 "Host not in allowlist").
  Test edilen hostlardan yalnızca `github.com` erişilebilir; `*.vercel.app`,
  `higgsfield.ai` ve diğerleri 403 veriyor.
- ADIM 5 (metin bindirme): ham görseller gelmediği için final slide'lar üretilemedi.
- `preview/slide-1..5.png`: ham görsel yerine düz MOR arka plan kullanılarak üretilen
  **metin/yerleşim önizlemesi** (final post değildir — karakter illüstrasyonu eksik).

### Postu tamamlamak için

1. Ortamın ağ politikasına `vercel-hf-probe.vercel.app` host'unu ekleyin
   (Claude Code on the web → environment network policy).
2. ADIM 4b'deki relay submit komutunu yeniden çalıştırın — görseller
   `assets/gorseller/2026-05-18-ogle-12/slide-1..5.png` olarak commit'lenir.
3. `git pull --ff-only` sonrası overlay'i çalıştırın:
   `python3 scripts/overlay_text.py outputs/2026-05-18-ogle-12/render-layout.json`
   → final `outputs/2026-05-18-ogle-12/slide-1..5.png` üretilir.

`render-layout.json` bu klasörde hazır bekliyor (palette MOR, 5 slide metni gömülü).
