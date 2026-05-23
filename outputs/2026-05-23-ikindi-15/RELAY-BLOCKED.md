# Görsel üretimi BLOKLANDI — Relay 403

**Tarih:** 2026-05-23
**Slot:** 2026-05-23-ikindi-15
**Branch:** claude/zen-wozniak-cOnvT

## Hata

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
```

Submit request:
- URL: `https://vercel-hf-probe.vercel.app/api/hf/submit`
- Method: POST
- Body: 5 prompt (slot=2026-05-23-ikindi-15)

## Sebep

Bu remote execution environment'ın çıkış IP'si Vercel relay'in (`vercel-hf-probe`)
host/origin allowlist'inde değil. Relay, 403 ile "Host not in allowlist"
döndürdü — Higgsfield'a hiç submit edilmedi.

## Çözüm

Aşağıdakilerden birini yapın:

1. **Relay allowlist güncelle:** Vercel → `vercel-hf-probe` →
   Environment Variables → caller IP/host allowlist'ine bu session'ın
   çıkış IP'sini ekleyin. (IP'yi öğrenmek için: relay loglarına bakın
   ya da bu session'da `curl ifconfig.me` çalıştırın.)

2. **Routine UI'den tekrar çalıştırın:** Bu prompt'u Anthropic Routine
   üzerinden çalıştırın; Routine runner IP'si büyük ihtimalle relay
   allowlist'inde zaten ekli.

3. **Manuel submit:** Prompt JSON'u (`/tmp/prompts.json` veya
   ekteki versiyonu) elle relay'e POST'layın.

## Üretilen Metinler

- `icerik.md` — 5 slide metinleri
- `caption.txt` — Instagram caption (~470 kelime) + hashtag'ler
- `prompts.json` (bu klasörde) — Higgsfield prompt'ları, hazır
- `logs/ikindi-15.md` — 2026-05-23 satırı eklendi

Görseller geldiğinde `assets/gorseller/2026-05-23-ikindi-15/slide-{1..5}.png`
yoluna düşecek. Sonra:

```bash
python3 scripts/overlay_text.py outputs/2026-05-23-ikindi-15/layout.json
```

ile metin bindirme yapılabilir.
