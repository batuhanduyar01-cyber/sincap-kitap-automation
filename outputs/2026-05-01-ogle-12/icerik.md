# Sincap Kitap IG — 2026-05-01 Öğle 12:00

## Konu
**Yatmayı istememe** (çocuk perspektifinden, eğlenceli/oyunsu ton)

## Palette
**MOR** — bg `#7E5BA0` / accent `#C5E86C` (yeşil) / text `#FFFFFF` (beyaz)

(Konu eşleştirmesi: gece / uyku → MOR. Sıcak yıldızlı gece hissi.)

## Karakter
Yavru sincap (baby squirrel) — mini çizgili pijamayla; 5 slide boyunca aynı.

## Slide Metinleri

### Slide 1 — KAPAK
- **title_main:** Daha
- **title_accent:** Uykum Yok!
- **subtitle:** Küçük bir sincabın geceyle imtihanı.

### Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Seninle bir öykü daha okusak olur mu? Sesini dinlemek bana huzur veriyor."

### Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Gözlerim yumulmuyor çünkü bu kocaman dünyayı doyasıya keşfetmek istiyorum."

### Slide 4 — EBEVEYN NOTU
**Ebeveyn Notu**

Çocuğunuz uykuya direnmiyor; yalnızca güne veda etmekte zorlanıyor. Aynı saat, aynı ritüel ve aynı sıcak ses güveni büyütür.

İpucu: Yatmadan önce 10 dakikalık "sessiz oda" başlatın; ışıkları kısın, ses tonunuzu yumuşatın.

### Slide 5 — KAPANIŞ
"İyi geceler! Yarın yine en güzel maceralarla buluşmak üzere. Sincap Kitap'ı takip et 🐿️"

## Higgsfield Görsel Durumu

`assets/gorseller/2026-05-01-ogle-12/slide-1..5.png` üretimi **bekliyor**.

Vercel relay (`https://vercel-hf-probe.vercel.app`) bu Routine ortamının IP'sini (`64.29.17.131`) host allowlist'inde reddetti (HTTP 403, "Host not in allowlist"). 5 prompt JSON'u `outputs/2026-05-01-ogle-12/prompts.json` içinde hazır; relay ortamına o dosya verilerek üretim tamamlanabilir.

İlerletmek için:
- Vercel relay allowlist'ine `64.29.17.131` ekle, sonra bu Routine'i tekrar çalıştır, **veya**
- Relay'in çağrılmasına izin verilen başka bir ortamdan `scripts/relay_api.py submit-batch --slot 2026-05-01-ogle-12 --branch claude/confident-dijkstra-6Bqfm --prompts-file outputs/2026-05-01-ogle-12/prompts.json` komutunu çalıştır.

Görseller `assets/gorseller/2026-05-01-ogle-12/` klasörüne commit'lenince `python3 scripts/overlay_text.py outputs/2026-05-01-ogle-12/layout.json` ile final 5 slide üretilebilir.
