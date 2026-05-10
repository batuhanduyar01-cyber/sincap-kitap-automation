# Relay engellemesi — manuel çalıştırma gerekiyor

Bu post için tüm metin içerikleri (caption, icerik, slide metinleri, layout, prompts.json) hazırlandı; ancak Higgsfield görsel üretimi **çalıştırılamadı**.

## Sebep

`https://vercel-hf-probe.vercel.app` adresine yapılan herhangi bir istek (auth header olsun olmasın, hatta basit `GET /`) `403 Host not in allowlist` ile reddediliyor. Relay'in IP allowlist'i bu Claude Code çalıştırma ortamının IP'sini içermiyor — sadece Anthropic Routine runner IP'lerini kabul edecek şekilde yapılandırılmış görünüyor.

```
$ curl https://vercel-hf-probe.vercel.app/
Host not in allowlist
HTTP 403
```

## Manuel çalıştırma

Routine UI üzerinden veya allowlist'te olan başka bir ortamdan:

```bash
SLOT="2026-05-10-ikindi-15"
BRANCH="claude/zen-wozniak-bJ5Ro"
cp outputs/2026-05-10-ikindi-15/raw/prompts.json /tmp/prompts.json

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek RELAY_SHARED_SECRET>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file /tmp/prompts.json
```

PNG'ler `assets/gorseller/2026-05-10-ikindi-15/slide-{1..5}.png` olarak commit'lenince:

```bash
git pull --ff-only origin claude/zen-wozniak-bJ5Ro
python3 scripts/overlay_text.py outputs/2026-05-10-ikindi-15/layout.json
```
