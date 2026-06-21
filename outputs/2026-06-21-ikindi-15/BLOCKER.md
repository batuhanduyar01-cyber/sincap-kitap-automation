# BLOKAJ — 2026-06-21 İkindi 15:00

**Durum:** Görseller üretilemedi. Metin, caption, prompt'lar ve layout.json hazır.

## Hata

Vercel relay'e POST atarken Anthropic ortamının egress firewall'ı reddetti:

```
[relay_api] submit HTTP 403:
{"_raw": "Host not in allowlist: vercel-hf-probe.vercel.app.
 Add this host to your network egress settings to allow access."}
```

Yani sorun Higgsfield veya Vercel'de değil — bu Routine container'ının
çıkış (egress) policy'sinde. Relay host'u allowlist'te değil.

## Düzeltme

1. Anthropic Routine ortamının network policy'sine
   `vercel-hf-probe.vercel.app` host'unu allowlist olarak ekle.
   (Veya tüm `*.vercel.app` domain'ini, daha geniş kullanım için.)
   Belge: https://code.claude.com/docs/en/claude-code-on-the-web

2. Allowlist düzeltildikten sonra şu komutu manuel çalıştır:

```bash
cd /path/to/sincap-kitap-automation
git checkout claude/zen-wozniak-fqn3vu
git pull --ff-only origin claude/zen-wozniak-fqn3vu

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "2026-06-21-ikindi-15" \
    --branch "claude/zen-wozniak-fqn3vu" \
    --prompts-file outputs/2026-06-21-ikindi-15/prompts.json

# Görseller branch'e commit'lendikten sonra:
git pull --ff-only origin claude/zen-wozniak-fqn3vu
cp outputs/2026-06-21-ikindi-15/layout.template.json layout.json
python3 scripts/overlay_text.py layout.json
```

3. Sonra final slide-1..5.png `outputs/2026-06-21-ikindi-15/` altında oluşur.

## NOT — Bildirim Eksikliği

Bu routine session'ında `PushNotification` tool aktif değil. Yani normalde
"bana telefonuna bildirim atayım" şeklinde bilgi gönderemedim. Blokaj
sadece bu commit ile (GitHub branch'inde) görünüyor.
