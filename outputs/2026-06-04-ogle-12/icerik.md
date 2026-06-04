# Sincap Kitap IG — 2026-06-04 Öğle 12:00

## Konu
**Diş fırçalatmama** (refusing to brush teeth) — çocuk perspektifinden, oyunlu, sevgi dolu bir ton.

## Palette — HARDAL
- bg: `#F5C82E`
- accent: `#7E5BA0`
- text: `#3D2817`

## Karakter
Sevimli küçük sincap (Sincap Kitap maskotuyla aynı kimlik), 5 slide boyunca aynı karakter.

## Slide Metinleri

### Slide 1 — KAPAK
- title_main: **Ben Dişlerimi**
- title_accent: **Fırçalamam!**
- subtitle: Çocuğun ağzından küçük bir hikâye

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> Annem benimle birlikte fırçalayınca bu oyun bizim oluyor.

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> Ağzımın içi bana kocaman bir mağara gibi geliyor. Acele etmesek olur mu?

### Slide 4 — EBEVEYN NOTU
> **Ebeveyn Notu**
>
> Diş fırçalamak çocuğa kontrol kaybı gibi gelebilir. Önce siz fırçalayın, sonra çocuk denesin. Birlikte söylenen kısa bir şarkı, direnci oyuna çevirir.

### Slide 5 — KAPANIŞ
> Sincap'ın maceralarının tamamı için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt Stratejisi
Tüm slide'lar aynı sincap karakterini, aynı sulu boya / guaj stili, aynı `#F5C82E` mustard arka plan ile üretir. Sahneler:

1. Sincap dev pembe diş fırçasını tutuyor, kollar bağlı, somurtkan ama sevimli — bubble, sparkle, mint leaf dekoru.
2. Anne sincap ve yavru sincap yan yana, ikisi de fırçalıyor, köpük dolu, gülüyorlar.
3. Yavru sincap dev aynanın önünde minicik, devasa açık ağız yansıması, savunmasız poz.
4. Anne sincap ve yavru, bir minderde, yatmadan önce diş fırçalama hikayesi okuyorlar.
5. Yavru sincap el sallayarak veda, parlak temiz dişler, yanında küçük kitap yığını.

## Status
- Prompts: `raw/prompts.json` — hazır.
- Higgsfield görselleri: **BLOKLU** (relay 403 "Host not in allowlist").
- Layout: `raw/slide-layout.json` — hazır (gitignore'daki `layout.json` paterni nedeniyle yeniden adlandırıldı).
- Caption: `caption.txt` — hazır.
- Slide PNG'leri: Görsel ham PNG'ler geldikten sonra `python3 scripts/overlay_text.py outputs/2026-06-04-ogle-12/layout.json` komutu ile üretilecek.
