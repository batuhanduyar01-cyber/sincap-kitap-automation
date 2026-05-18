# Sincap Kitap IG — İkindi 15:00 İçerik Dosyası

- **Tarih:** 2026-05-18
- **Slot:** 2026-05-18-ikindi-15
- **Konu:** kitap okuma alışkanlığı
- **Ton:** Sıcak anne + bilge arkadaş, pedagojik ipucu ağırlıklı
- **Palette:** TURUNCU — arka plan `#E97E28`, aksan `#FFFFFF`, metin `#2A1810`

## Slide Metinleri

**Slide 1 — KAPAK**
- Başlık: "Kitap Sevgisi"
- Aksan: "Nasıl Filizlenir?"
- Alt başlık: "Küçük bir alışkanlık, ömür boyu sürecek bir dostluğa dönüşür."

**Slide 2 — ÇERÇEVE**
> Çocuklar kitapları zorlamayla değil, keyifle sever. Her gün paylaşılan birkaç sayfa, dünyanın keşfedilecek büyülü bir yer olduğunu usulca fısıldar.

**Slide 3 — ANAHTAR KAVRAM: "Tekrar"**
> Aynı kitabı defalarca istemek bir inat değildir. Tekrar, çocuğun dünyayı anlamlandırma ve kendini güvende hissetme yoludur.

**Slide 4 — UNUTMAYIN!**
> Kitap okumak bir görev değil, sıcak bir buluşmadır. Sesinizi karakterlere göre değiştirin, resimleri birlikte keşfedin; mükemmel okumak değil, yan yana olmak önemlidir. Bu akşam: Uyumadan önce kitabı çocuğunuz seçsin, kucağınızda birlikte okuyun.

**Slide 5 — KAPANIŞ**
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Görsel Prompt'ları

Karakter (5 slide sabit): **baby squirrel** (Sincap maskotu). Palette HEX: `#E97E28`.
Tam JSON: `prompts.json`.

1. **Slide 1** — central baby squirrel holding an open picture book, 2-3 small side objects (closed book, pencil, leaf)
2. **Slide 2** — cozy reading-corner with multiple animal characters (bear cub, kitten, hedgehog) sharing picture books
3. **Slide 3** — repetition concept: baby squirrel hugging its favorite worn book, surrounded by identical copies
4. **Slide 4** — mother squirrel and little one reading together in a cozy armchair at bedtime
5. **Slide 5** — baby squirrel smiling and waving, surrounded by a stack of colorful books

## NOT — Higgsfield Görselleri Üretilemedi

ADIM 4'teki Vercel relay'i (`https://vercel-hf-probe.vercel.app`) bu çalıştırma
ortamının ağ allowlist'i tarafından bloklandı (`HTTP 403 — Host not in allowlist`).
Higgsfield watercolor illüstrasyonları bu yüzden üretilemedi.

Geçici çözüm: `assets/gorseller/2026-05-18-ikindi-15/slide-*.png` dosyaları,
overlay pipeline'ının tamamlanabilmesi için TURUNCU palette'inde sıcak bir
suluboya tonunda **placeholder arka plan** olarak üretildi (`raw/` klasöründe
kopyaları var). Relay erişilebilir olduğunda `prompts.json` ile gerçek görseller
üretilip aynı yola konmalı ve `python3 scripts/overlay_text.py layout.json`
yeniden çalıştırılmalı.

## Caption + Hashtag

Tam metin: `caption.txt` (caption ~415 kelime + 20 hashtag).
