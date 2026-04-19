# Sincap Kitap — Instagram Otomasyonu

Sincap Kitap (0-6 yaş çocuk kitabı yayınevi) Instagram hesabı için her gün
3 carousel postu otomatik üreten Claude Code Routines tabanlı sistem.

## Neler Üretir

- **09:00 Sabah** — Anne odaklı, sıcak empatik ton (5 slide)
- **12:00 Öğle** — Çocuk odaklı, eğlenceli/oyunsu ton (5 slide, alıntı ağırlıklı)
- **15:00 İkindi** — Pedagojik ipucu ağırlıklı ton (5 slide)

Her post: kapak + 4 iç sayfa + caption + hashtag + ham illüstrasyonlar.

## Mimari

```
Claude Routine (cron)
  └─ Konu seç (log'dan tekrar kontrolü)
  └─ Türkçe metin üret (5 slide)
  └─ Higgsfield Soul ile 5 illüstrasyon üret (karakter referansı ile tutarlı)
  └─ Python PIL ile metin + logo bindir
  └─ outputs/ klasörüne kaydet, GitHub'a push
```

## Klasör Yapısı

```
sincap-kitap-automation/
├── assets/
│   ├── logo.png                  # Sincap Kitap baykuş logosu (transparan PNG)
│   ├── character-reference.png   # Higgsfield master karakter referansı
│   └── fonts/
│       ├── BagelFatOne-Regular.ttf
│       └── Baloo2-Regular.ttf
├── scripts/
│   └── overlay_text.py           # Python PIL metin bindirme
├── prompts/
│   ├── routine-sabah-9.md
│   ├── routine-ogle-12.md
│   └── routine-ikindi-15.md
├── logs/
│   ├── sabah-9.md                # 14 gün konu geçmişi
│   ├── ogle-12.md
│   └── ikindi-15.md
├── outputs/                      # Routine günlük doldurur: {TARIH}-{SLOT}/
├── requirements.txt
└── README.md
```

## Hızlı Başlangıç

1. `BURADAN-BASLA.md` dosyasını takip et
2. `assets-needed/CHECKLIST.md`'deki varlıkları tamamla
3. `claude.ai/code/routines` üzerinde 3 Routine oluştur (cron: `0 9 * * *`, `0 12 * * *`, `0 15 * * *`)
4. Her Routine için ilgili `prompts/routine-*.md` içeriğini yapıştır
5. GitHub ve Higgsfield bağlantılarını ekle
6. "Run now" ile test et

## Kullanılan Araçlar

- **Claude Code Routines** — Zamanlayıcı ve ana akış
- **Higgsfield Soul** — Watercolor/gouache stil illüstrasyon üretimi
- **Python PIL (Pillow)** — Türkçe karakter güvenli metin bindirme
- **Google Fonts** — Bagel Fat One (başlık) + Baloo 2 (gövde)

## Kısıtlar

- Her post için 5 slide AYNI palette (6 palette arasından seçim)
- Aynı konu 14 gün içinde tekrar etmez
- Aynı gün 3 post birbirinden farklı konu
- Tasarımda ok/nokta/slide numarası YOK (Instagram zaten ekler)
- Flat vector illüstrasyon YOK — yalnızca boyalı kitap stili

## Lisans ve Kullanım

Sincap Kitap'ın iç kullanımı için. Fontlar: SIL Open Font License.
