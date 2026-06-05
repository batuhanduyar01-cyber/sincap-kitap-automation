# Sincap Kitap IG — 2026-06-05 Sabah 09:00

## Genel Bilgi

- **Tarih / slot:** 2026-06-05 — sabah-9
- **Konu:** Kıyafet inadı (2-4 yaş özerklik dönemi)
- **Ton:** Anne odaklı, sıcak, empatik, yargısız
- **Palette:** AHUDUDU
  - Arka plan: `#E63B5C`
  - Aksan: `#C5E86C` (yeşil)
  - Metin: `#FFFFFF` (beyaz)
- **Karakter:** bear cub (yavru ayı) — 5 slide boyunca aynı

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** "Onu Ben"
- **Aksan:** "Giyeceğim!"
- **Alt başlık:** "Kıyafet inadı, küçük bir kararlılığın ilk sesidir."

### Slide 2 — TANIDIK SAHNE
> Saat sekizi geçiyor, kapıdan çıkmak gerek. O ise üçüncü kez kıyafetini değiştirdi. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Ben artık büyüdüm, kendim seçmek istiyorum."

### Slide 4 — UNUTMAYIN!
- **Başlık:** UNUTMAYIN!
- **Gövde:** Kıyafet seçimi, çocuğunuzun ilk küçük özgürlük alanıdır. İnat değil, "ben de varım" demenin sevimli bir yolu. Bugün: Akşamdan iki kıyafet hazırlayın, sabah o seçsin.

### Slide 5 — KAPANIŞ
> O küçük "ben kendim" anlarına eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Görsel Prompt'ları

Ortak iskelet: `Children's book illustration, watercolor gouache painting, textured brush strokes, cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly palette, solid #E63B5C background, Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}`

| # | Sahne |
|---|---|
| 1 | big bear cub standing on a small hill wearing a tiny crooked hat and mismatched striped scarf, decorative leaves and stars around, looking proud and determined, gentle smile |
| 2 | bear cub with mother bear character, warm hugging interaction beside an open wardrobe with tiny clothes hanging, cozy indoor scene, soft morning light |
| 3 | small isolated bear cub standing among a giant pile of colorful sweaters and pants, emotional vulnerable pose holding one tiny shirt, vast empty space around for scale contrast, looking up hopefully |
| 4 | family scene with mother bear and bear cub reading a storybook together on a cozy bed, two folded outfit options resting beside them, warm cozy bedroom setting, soft lamplight |
| 5 | bear cub waving goodbye wearing a self-chosen mismatched outfit, smiling proudly, sitting on top of a stack of storybooks |

## Çıktı Dosyaları

- `layout.json` — overlay_text.py için kullanılan config
- `caption.txt` — Instagram caption + hashtag'ler
- `icerik.md` — bu dosya
- `slide-1.png` … `slide-5.png` — finalize edilmiş slide'lar *(görsel üretimi tamamlanınca)*
- `raw/slide-*-raw.png` — Higgsfield ham çıktıları *(görsel üretimi tamamlanınca)*

## Üretim Durumu — DİKKAT

Bu routine bu çalıştırmada görsel üretimini **tamamlayamadı**:

- Vercel relay (`https://vercel-hf-probe.vercel.app/api/hf/submit`) bu Routine
  ortamından gelen isteği `HTTP 403 Host not in allowlist` ile reddetti.
- Bu, Vercel projesindeki host-allowlist guard'ı tarafından durduruldu; relay
  secret doğru paste edilmiş olsa bile origin IP'si listede değilse submit
  edilemiyor.
- Sonuç: `assets/gorseller/2026-06-05-sabah-9/slide-*.png` üretilmedi,
  ADIM 5 (overlay) ve `outputs/.../slide-*.png` boş kaldı.

### Yeniden çalıştırma için yapılacaklar

1. Vercel `vercel-hf-probe` projesinde Anthropic Routine runner IP/host range'ini
   allowlist'e ekle (relay'in `Host not in allowlist` döndürdüğü guard).
2. Allowlist güncellendikten sonra bu routine'i yeniden çalıştır — log'daki
   `2026-06-05: kıyafet inadı` satırı tekrar kontrolünü sağlar.
3. Submit tekrar başarılı olursa relay PNG'leri otomatik olarak
   `assets/gorseller/2026-06-05-sabah-9/slide-N.png` yoluna commit'ler;
   ardından `python3 scripts/overlay_text.py outputs/2026-06-05-sabah-9/layout.json`
   ile final slide'lar üretilir.
