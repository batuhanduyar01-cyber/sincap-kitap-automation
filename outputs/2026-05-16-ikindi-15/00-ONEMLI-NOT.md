# ÖNEMLİ — Görseller Placeholder, Yayına Hazır DEĞİL

Bu klasördeki `slide-1.png` … `slide-5.png` dosyaları **düz HARDAL arka plan
(#F5C82E) üzerine** render edilmiştir. Higgsfield watercolor illüstrasyonları
**içermezler**. Metin, font, Türkçe karakter, yerleşim ve logo doğru; eksik olan
tek şey karakter illüstrasyonudur.

## Neden?

ADIM 4'teki Higgsfield görsel üretimi başarısız oldu. Bu Routine'in çalıştığı
ortamın ağ politikası (network allowlist) yalnızca GitHub host'larına izin
veriyor. Relay'in host'u `vercel-hf-probe.vercel.app` ve `higgsfield.ai`
allowlist'te olmadığı için engellendi:

```
relay submit -> HTTP 403: "Host not in allowlist"
relay_api.py submit-batch exit code: 3
```

Yani sorun relay/secret değil — bu ortamdan dış ağa çıkış kapalı.

## Düzeltmek için

**Seçenek A — Ortam ağ politikasını genişlet (önerilen):**
Bu Routine'i çalıştıran ortamın network allowlist'ine şu host'u ekleyin:
`vercel-hf-probe.vercel.app`. Sonra Routine'i tekrar çalıştırın; ADIM 4 sorunsuz
geçer. (Ortam yapılandırması: https://code.claude.com/docs/en/claude-code-on-the-web)

**Seçenek B — Görselleri manuel üret ve yeniden bindir:**
1. `prompts.json` içindeki 5 prompt'u Higgsfield'da çalıştırın.
2. Çıkan PNG'leri `outputs/2026-05-16-ikindi-15/raw/slide-1-raw.png` …
   `slide-5-raw.png` olarak (mevcut placeholder'ların üzerine) kaydedin.
3. Proje kökünden tekrar çalıştırın:
   ```bash
   python3 scripts/overlay_text.py outputs/2026-05-16-ikindi-15/layout.json
   ```
   `slide-1.png` … `slide-5.png` final olarak yeniden üretilir.

## Bu çalıştırmada hazır olan her şey

- ✅ Konu seçimi + `logs/ikindi-15.md` güncellendi
- ✅ 5 slide metni (`icerik.md`)
- ✅ Instagram caption + 20 hashtag (`caption.txt`)
- ✅ HARDAL palette
- ✅ 5 Higgsfield prompt'u (`prompts.json`) — hazır, kopyala-çalıştır
- ✅ `layout.json` — overlay config
- ✅ Metin/font/logo bindirme pipeline'ı doğrulandı (placeholder arka plan üzerinde)
- ❌ Higgsfield illüstrasyonları — ortam ağ politikası nedeniyle üretilemedi
