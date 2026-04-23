# Sincap Kitap IG — 2026-04-23 Öğle 12:00

## Meta
- **Konu:** Diş fırçalatmama
- **Palette:** HARDAL #F5C82E (bg) + MOR #7E5BA0 (accent) + #3D2817 (text)
- **Karakter:** Yavru kedi (kitten)
- **Ton:** Çocuk odaklı, eğlenceli, oyunsu — çocuk ağzından alıntı ağırlıklı

## Slide Metinleri

### Slide 1 — KAPAK
- **Ana başlık:** Dişlerim
- **Aksan başlık:** Fırçalanmak İstemiyor!
- **Alt metin:** Minik bir kedi, kocaman bir inat.

### Slide 2 — ÇOCUĞUN SESİ (sevgi)
> "Seninle yaptığım her şey güzel anne, fırçayı birlikte tutalım mı?"

### Slide 3 — ÇOCUĞUN SESİ (ihtiyaç)
> "Fırça kocaman, ağzım minicik. Biraz daha yavaş olsak olur mu?"

### Slide 4 — EBEVEYN NOTU
Direnç inat değil, kontrol ihtiyacıdır. Fırçalamayı oyuna çevirin: aynada gülücük yarışı, "hadi çürük avına!" şarkısı. **İpucu:** çocuğa fırçayı seçtirin, ilk sırayı ona verin.

### Slide 5 — KAPANIŞ
Yarın gece yine birlikte fırçalarız! Sincap Kitap'ı takip et 🐿️

## Dosyalar
- `caption.txt` ✅
- `layout.json` ✅
- `icerik.md` ✅
- `slide-1.png` … `slide-5.png` ⏳ (raw görseller üretilmedi)
- `raw/slide-{1..5}-raw.png` ⏳

## ⚠️ Durum Notu — 2026-04-23

Bu Routine çalıştırıldığında Higgsfield API **`platform.higgsfield.ai` Host not in allowlist (HTTP 403)** hatası döndü. Claude Code cloud ortamının outbound proxy'si bu host'a erişime izin vermiyor. `dangerouslyDisableSandbox` yerel sandbox'ı kapatır ama cloud proxy'yi etkilemez.

**Çözüm seçenekleri:**
1. Ortamın outbound allowlist'ine `platform.higgsfield.ai` eklensin (altyapı/settings)
2. Higgsfield adımları lokalde çalıştırılıp `raw/slide-{N}-raw.png` dosyaları repo'ya yüklensin — sonra `python3 scripts/overlay_text.py outputs/2026-04-23-ogle-12/layout.json` ile tamamlanır
3. Higgsfield'ı kullanan ikinci bir pipeline (MCP tool'u olan ortam) tetiklensin

**Bu koşu:** Metin artefaktları (layout, caption, icerik, log) hazır. Raw illüstrasyonlar eklendiği anda overlay adımı tek komutla biter.

