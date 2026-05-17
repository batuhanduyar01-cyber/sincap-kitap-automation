# Sincap Kitap IG — İkindi 15:00 | 2026-05-17

## Konu

**Merak** (çocuğun "neden?" soruları, merakı besleme)

- Slot: `2026-05-17-ikindi-15`
- Ton: Sıcak anne + bilge arkadaş, pedagojik ipucu ağırlıklı
- Tekrar kontrolü: `logs/ikindi-15.md`, `logs/sabah-9.md`, `logs/ogle-12.md` okundu — hepsi boş, çakışma yok.

## Palette — HARDAL

| Rol | Renk |
|---|---|
| Arka plan (bg) | `#F5C82E` |
| Aksan (accent) | `#8E4FAA` (mor) |
| Metin (text) | `#2A1810` (koyu kahve) |

İkindi teması için sıcak/gün sonu hissi veren palettelerden HARDAL seçildi
(merak/sorular eşleştirmesi).

## Slide Metinleri

### Slide 1 — KAPAK (cover)
- Başlık (ana): **Bitmeyen Soruların**
- Başlık (aksan): **Sırrı**
- Alt başlık: Çocuğunuzun her 'neden?'i merakın işaretidir.

### Slide 2 — ÇERÇEVE (inner)
> Çocuğunuz gün boyu 'neden?' diye soruyor ve siz bazen yorgun düşüyorsunuz.
> Aslında bu sorular, dünyayı anlamaya çalışan zihninin sesidir. Her soru,
> büyüyen bir merakın küçük kıvılcımıdır.

### Slide 3 — ANAHTAR KAVRAM (concept)
- Başlık: **Merak**
> Merak, çocuğun öğrenme isteğini canlı tutan içsel bir kıvılcımdır.
> Beslendikçe büyür, susturuldukça söner.

### Slide 4 — UNUTMAYIN! (tip)
- Başlık: **UNUTMAYIN!**
> Her soruya hemen cevap vermek zorunda değilsiniz. Bazen 'Sen ne
> düşünüyorsun?' demek merakı daha da büyütür. Bu akşam: Çocuğunuz bir
> 'neden?' sorduğunda birlikte tahmin oyunu oynayın.

### Slide 5 — KAPANIŞ (cta)
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Prompt'ları (KARAKTER: baby squirrel, PALETTE_HEX: #F5C82E)

Ortak iskelet:
> Children's book illustration, watercolor gouache painting, textured brush
> strokes, cute baby squirrel character in rich scene, multiple storybook
> characters, large expressive eyes, rosy cheeks, warm painterly palette,
> solid #F5C82E background, Oliver Jeffers and Marc Boutavant style,
> storybook art, no text, no frames, portrait orientation, {SAHNE}

| Slide | Sahne |
|---|---|
| 1 | central baby squirrel character holding a small magnifying glass with a curious wide-eyed expression, 2-3 small side objects floating nearby (open book, acorn, leaf) |
| 2 | rich cozy scene with multiple curious animal children exploring a kindergarten classroom, examining books and objects with wonder and amazement |
| 3 | scene representing curiosity, baby squirrel discovering a glowing butterfly and floating sparkles, eyes wide with amazement and wonder |
| 4 | warm parent and child squirrel exploring nature together, looking at a flower through a magnifying glass, gentle storytelling moment in a sunny garden |
| 5 | baby squirrel character smiling and waving happily, surrounded by small books and acorns and warm cozy objects |

Boyut: `1152x1536`, kalite: `1080p`.

## NOT — Görsel Üretimi (ADIM 4) Tamamlanamadı

Higgsfield illüstrasyonları üretilemedi. Vercel relay'e (`vercel-hf-probe.vercel.app`)
yapılan submit isteği bu çalıştırma ortamının ağ allowlist'i tarafından
engellendi:

```
submit HTTP 403: {"_raw": "Host not in allowlist"}
```

GitHub erişilebilir durumda (fontlar başarıyla indirildi) ancak Vercel relay
host'u ortamın ağ politikasında izinli değil. Bu kalıcı bir politika reddi
olduğu için retry denenmedi.

**Çözüm:** Bu repoya bağlı Claude Code on the web ortamının ağ
allowlist'ine `vercel-hf-probe.vercel.app` eklenmeli. Sonrasında ADIM 4
(relay submit) ve ADIM 5 (overlay) yeniden çalıştırılırsa post tamamlanır.

**Geçici çıktı:** Slide'lar, raw illüstrasyon yerine düz HARDAL (`#F5C82E`)
arka plan üzerinde tipografi + logo ile render edildi. Gerçek görseller
geldiğinde `assets/gorseller/2026-05-17-ikindi-15/slide-*.png` dosyaları
değiştirilip `python3 scripts/overlay_text.py layout.json` tekrar
çalıştırılması yeterlidir.

## Bu Çalıştırmada Yapılan Düzeltmeler

- **Fontlar eklendi:** `assets/fonts/BagelFatOne-Regular.ttf` ve
  `Baloo2-Regular.ttf` GitHub'dan indirilip eklendi (önceden eksikti,
  script default fonta düşüyordu).
- **`overlay_text.py` satır yüksekliği düzeltildi:** `draw_multiline_center`
  satır yüksekliğini dar harf bbox'ı yerine font metriklerinden
  (ascent + descent) hesaplıyor. Önceki halinde kapakta aksan kelime ile
  alt başlık üst üste biniyordu.
- **Slide 5 emoji'si görselden çıkarıldı:** Baloo 2 fontu 🐿️ glifini
  içermediği için görselde kutu (tofu) olarak çıkıyordu. Emoji yalnızca
  `caption.txt` içinde tutuldu (Instagram caption'da düzgün render eder).
  Slide üzerindeki marka göndermesini sol alttaki sincap logosu karşılıyor.
