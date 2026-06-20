# HATA — Görseller üretilmedi (2026-06-20 ikindi-15)

## Ne oldu
Routine bu sefer sadece metin + prompts üretebildi. Higgsfield görselleri
üretilmedi, çünkü bu sandbox'ın çıkış ağı politikası `vercel-hf-probe.vercel.app`
host'unu (ve `platform.higgsfield.ai`'yi) bloklamış durumda. Yalnızca
`github.com` erişimine izin verildi.

Relay denemesinden dönen cevap:
```
HTTP 403: Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access.
```

## Nasıl düzeltilir
Routine'in çalıştığı ortamın network policy ayarlarına şu host'ları ekle
(Claude Code on the web → environment → network egress allowlist):

- `vercel-hf-probe.vercel.app`
- `platform.higgsfield.ai`
- `cdn.higgsfield.ai` (üretilen PNG'lerin host'u, gerekirse)

Sonraki ikindi-15:00 çalıştırmasında otomatik olarak görsel üretimi de
çalışacaktır.

## Bu çalıştırmada hazır olanlar

- `icerik.md` — 5 slide'ın Türkçe metni
- `caption.txt` — 400-500 kelime Instagram caption + hashtag'ler
- `prompts.json` — 5 slide için Higgsfield prompt'ları (sıcak turuncu #E97E28 palet)
- `layout.json` — overlay_text.py için hazır şablon

## Görseller geldikten sonra elle nasıl tamamlanır
Eğer görselleri local olarak elle üretip `assets/gorseller/2026-06-20-ikindi-15/`
altına slide-1.png .. slide-5.png olarak yerleştirirseniz:

```bash
python3 scripts/overlay_text.py outputs/2026-06-20-ikindi-15/layout.json
```

`outputs/2026-06-20-ikindi-15/slide-1.png` ... `slide-5.png` üretilecektir.

> Not: `assets/fonts/` klasörü hâlâ boş — Bagel Fat One ve Baloo 2 font dosyaları
> repo'ya eklenmediği sürece overlay Pillow default fontunu kullanacak ve
> başlıklar zayıf görünecektir. Detay: `assets/fonts/README.md`.
