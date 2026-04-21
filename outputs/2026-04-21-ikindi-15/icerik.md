# Sincap Kitap IG — İkindi 15:00 — 2026-04-21

## Konu
**cesaret** (pedagojik ipucu ağırlıklı, anne-bilge arkadaş tonu)

## Palette
**MERCAN**
- Arka plan: `#F08A7B`
- Aksan: `#FFF4E6` (krem)
- Metin: `#3A2418` (koyu kahve)

## Karakter
hedgehog (kirpi) — 5 slide boyunca sabit

## Slide metinleri

### Slide 1 — KAPAK
- Başlık: **Küçük Kalplerde**
- Aksan: **Büyük Cesaret**
- Alt başlık: "Her büyük adımın öncesinde küçük bir titreme vardır."

### Slide 2 — ÇERÇEVE
"Cesaret, korkusuzluk değildir; korkuya rağmen adım atabilmektir. Çocuğunuzun her 'ben yaparım' demesi, minik bir kahramanlıktır."

### Slide 3 — ANAHTAR KAVRAM
- Başlık: **Cesaret**
- Gövde: "Cesaret öğretilmez, örneklenerek büyür. Sizin sakinliğiniz, onun güveni olur."

### Slide 4 — UNUTMAYIN!
"Her çocuk kendi hızında cesaretlenir. Zorlamak değil, güvenle yanında durmak yeterlidir. Bu akşam: 'Bugün hangi küçük şeyi denemeye cesaret ettin?' diye sorun."

### Slide 5 — KAPANIŞ
"Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️"

## Higgsfield prompt iskeleti
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute hedgehog character in rich scene, multiple storybook characters, large expressive eyes,
rosy cheeks, warm painterly palette, solid #F08A7B background,
Oliver Jeffers and Marc Boutavant style, storybook art, no text, no frames,
portrait orientation, {SAHNE}
```

Slide-bazlı sahne değişkenleri:
- **Slide 1:** central hedgehog on coral background, 2-3 small side objects (pencil, book, music note)
- **Slide 2:** hedgehog with small parent hedgehog, warm tender interaction, cozy indoor setting
- **Slide 3:** small hedgehog looking into a tiny mirror held by a bigger animal friend, curious expression, abstract "cesaret" feeling
- **Slide 4:** parent-child hedgehog scene, reading a storybook together, warm bedroom with a soft lamp
- **Slide 5:** hedgehog smiling and waving, surrounded by small books and warm objects (cup, leaf, star)

## Higgsfield üretimi — not
Routine ortamında `platform.higgsfield.ai` host'u sandbox/proxy tarafından engellendiği için (`403 Host not in allowlist`), Higgsfield API'ye HTTP erişimi sağlanamadı. Pipeline'ı tamamlamak adına MERCAN paletli, karakter siluetli ve dekoratif motifli **PIL ile üretilen placeholder raw görseller** kullanıldı (`outputs/2026-04-21-ikindi-15/raw/slide-*-raw.png`). Yukarıdaki prompt iskeleti, host erişimi açıldığında olduğu gibi Higgsfield'a gönderilebilir ve aynı dosya adlarıyla raw görseller değiştirilip `overlay_text.py` yeniden çalıştırılabilir.

Ayrıca `assets/fonts/` altında Bagel Fat One ve Baloo 2 TTF dosyaları bulunmadığı için `overlay_text.py` PIL default font'u kullandı. Font'lar eklendikten sonra script yeniden çalıştırılarak tipografik son hâl elde edilebilir.

## Dosyalar
- `outputs/2026-04-21-ikindi-15/slide-1.png` — kapak
- `outputs/2026-04-21-ikindi-15/slide-2.png` — çerçeve
- `outputs/2026-04-21-ikindi-15/slide-3.png` — anahtar kavram
- `outputs/2026-04-21-ikindi-15/slide-4.png` — unutmayın + mikro aktivite
- `outputs/2026-04-21-ikindi-15/slide-5.png` — kapanış CTA
- `outputs/2026-04-21-ikindi-15/raw/slide-*-raw.png` — ham görseller
- `outputs/2026-04-21-ikindi-15/caption.txt` — Instagram caption + hashtag'ler
- `outputs/2026-04-21-ikindi-15/layout.json` — overlay config

## Kısıt kontrolü
- [x] Türkçe, sıcak bilge anne dili
- [x] Pedagojik ipucu + somut mikro aktivite (Slide 4)
- [x] 5 slide AYNI palette (MERCAN)
- [x] Tasarımda ok/nokta/sayı YOK
- [x] Sincap Kitap logosu sol altta
- [x] Aynı gün sabah/öğle postlarıyla konu çakışması YOK (her iki log da boş)
- [x] 14 gün içinde konu tekrarı YOK (log boştu, `cesaret` yeni eklendi)
