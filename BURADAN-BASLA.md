# Sincap Kitap Instagram Routine Kurulum Rehberi

Bu klasör, Claude Code Routines üzerinde günlük 3 Instagram carousel postu otomasyonunu kurman için gereken her şeyi içeriyor.

## Sırayla Yapılacaklar

### ADIM 1 — Ön Hazırlık (tek seferlik, 15-20 dk)

Bu dosyaları bir GitHub repo'suna yükle (Routine'ler bu repo'ya bağlanacak):

```
sincap-kitap-automation/
├── assets/
│   ├── logo.png                      ← Sincap Kitap baykuş logosu (transparan PNG)
│   ├── character-reference.png       ← Master karakter referansı (Adım 3'te üreteceksin)
│   └── fonts/
│       ├── BagelFatOne-Regular.ttf   ← Google Fonts'tan indir
│       └── Baloo2-Regular.ttf        ← Google Fonts'tan indir
├── scripts/
│   └── overlay_text.py               ← Bu klasördeki scripts/overlay_text.py
├── outputs/                          ← Routine buraya kaydedecek
└── logs/                             ← Konu tekrar kontrolü için
    ├── sabah-9.md
    ├── ogle-12.md
    └── ikindi-15.md
```

**Detay:**
- `logo.png`: Mevcut Sincap Kitap logosunu transparan PNG olarak ~400x400 boyutunda kaydet
- `character-reference.png`: Adım 3'te Higgsfield ile üreteceğiz
- Fontlar: https://fonts.google.com/specimen/Bagel+Fat+One ve https://fonts.google.com/specimen/Baloo+2
- `logs/*.md`: Boş dosya oluştur (içine `# Kullanılan Konular` yaz)

---

### ADIM 2 — Connector'ları Bağla

`claude.ai/code` → Settings → Connectors:
- ✅ Higgsfield MCP (bağlı olmalı)
- ✅ GitHub (repo bağlantısı için)

---

### ADIM 3 — Master Karakter Referansı Üret (tek seferlik)

Claude Code CLI'da veya web UI'da şu prompt'u çalıştır:

```
higgsfield_soul_text_to_image tool'u ile tek bir karakter üret:

prompt: "Cute brown owl character with large round glasses, children's book mascot, watercolor gouache painting, soft textured brush strokes, large expressive eyes, rosy blush cheeks, friendly warm expression, standing portrait pose, front facing, solid cream background, Oliver Jeffers illustration style, storybook art, no text, painterly shading, high detail"

aspect_ratio: "1:1"
resolution: "1080p"
quality: "high"
```

Çıkan URL'i kaydet ve `character-reference.png` olarak GitHub repo'suna yükle. Bu URL 3 routine'e de referans olarak verilecek.

---

### ADIM 4 — Routine'leri Oluştur (her biri ~2 dk)

`claude.ai/code/routines` → "New routine" → 3 kez tekrar:

| Routine Adı | Cron | Prompt Dosyası |
|---|---|---|
| Sincap Kitap IG — Sabah 09:00 | `0 9 * * *` | `prompts/routine-sabah-9.md` |
| Sincap Kitap IG — Öğlen 12:00 | `0 12 * * *` | `prompts/routine-ogle-12.md` |
| Sincap Kitap IG — İkindi 15:00 | `0 15 * * *` | `prompts/routine-ikindi-15.md` |

Her routine için:
1. **Name** alanına yukarıdaki adı yaz
2. **Prompt** alanına ilgili dosyanın TAM İÇERİĞİNİ yapıştır
3. **Repository** alanında yukarıda oluşturduğun `sincap-kitap-automation` repo'sunu seç
4. **Connectors:** Higgsfield'ın işaretli olduğundan emin ol
5. **Model:** Claude Opus 4.6 öner (metin kalitesi için)
6. **Trigger:** Scheduled → Daily → Saat seç
7. **Save**
8. Saved routine sayfasında CLI benzeri cron ayarı için: `/schedule update <routine-name>` ile yukarıdaki cron ifadesini gir (eğer UI'da direkt saat seçilebildiyse gerek yok)

---

### ADIM 5 — Test Et

Her routine'in detay sayfasında **"Run now"** butonu var. Önce sabah-9 routine'ini manuel tetikle:
1. Çıktıyı bekle (~3-5 dk)
2. GitHub repo'sunda `outputs/YYYY-MM-DD-sabah-9/` klasörüne bak
3. 5 PNG + caption.txt + icerik.md olmalı
4. PNG'leri kontrol et — beğendiysen diğer 2 routine'i kur
5. Beğenmediysen sadece o routine'in prompt'unu edit et, tekrar test et

---

### ADIM 6 — Dikkat Edilecekler

- **Pro plan**: günde 5 routine run hakkı var → 3 post/gün rahat sığar
- **Max plan**: 15 run/gün
- **Konu tekrarını önleme**: Her routine çalıştığında `logs/{dilim}.md` dosyasını okur ve son 14 günde olmayan konu seçer. İlk 14 gün dolana kadar tekrar olmaz
- **Karakter tutarlılığı**: 3 routine de aynı `character-reference.png` URL'ini Higgsfield'a referans veriyor → tüm postlarda aynı Sincap maskotu

---

## Dosya Listesi

- `BURADAN-BASLA.md` ← bu dosya
- `prompts/routine-sabah-9.md` ← Routine 1 prompt (kopyala-yapıştır)
- `prompts/routine-ogle-12.md` ← Routine 2 prompt (kopyala-yapıştır)
- `prompts/routine-ikindi-15.md` ← Routine 3 prompt (kopyala-yapıştır)
- `scripts/overlay_text.py` ← Python PIL metin bindirme scripti (repo'ya yükle)
- `assets-needed/CHECKLIST.md` ← Repo'ya yüklenmesi gereken asset listesi

Kurulum sırasında takıldığın yerde sorabilirsin.
