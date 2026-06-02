# ADIM 4 ve ADIM 5 BEKLEMEDE — Network allowlist sorunu

**Tarih:** 2026-06-02
**Slot:** 2026-06-02-ikindi-15
**Branch:** claude/zen-wozniak-xd0tq

## Sorun

`scripts/relay_api.py submit-batch` çağrısı, Vercel relay'e bağlanmadan
**bu Routine ortamının kendi egress proxy'si** tarafından 403 ile reddedildi:

```
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist"}
```

Aynı hata `vercel-hf-probe.vercel.app`, `platform.higgsfield.ai` ve hatta
`api.ipify.org` için de döner — yani Higgsfield WAF'ı değil, Routine
sandbox'ının kendi outbound allowlist'i bu hostları engelliyor.

Ulaşılabilir hostlar:

| Host | Durum |
|---|---|
| github.com | HTTP 200 |
| raw.githubusercontent.com | HTTP 301 |
| api.github.com | 403 (proxy block) |
| platform.higgsfield.ai | 403 (proxy block) |
| **vercel-hf-probe.vercel.app** | **403 (proxy block)** |

## Çözüm (kullanıcı tarafı)

Routine ortamının network policy ayarlarına aşağıdaki host'u eklemek gerekiyor:

- `vercel-hf-probe.vercel.app` (relay)
- (opsiyonel) `platform.higgsfield.ai` (direkt API'ye düşmek istenirse)

Bkz. https://code.claude.com/docs/en/claude-code-on-the-web → network policies.

## Bu post için tamamlanan iş

- [x] Konu seçimi: **Merak**
- [x] Palette: **HARDAL** (bg `#F5C82E`, aksan `#8E4FAA`, metin `#4A2C2A`)
- [x] Karakter: baby fawn (5 slide aynı kalacak)
- [x] `logs/ikindi-15.md` güncellendi
- [x] `icerik.md` — 5 slide metinleri
- [x] `caption.txt` — IG caption + hashtag
- [x] `layout.json` — overlay_text.py için hazır config
- [x] `raw/prompts.json` — Higgsfield için 5 prompt hazır
- [ ] **ADIM 4** — Higgsfield ham görseller (network'e bağlı)
- [ ] **ADIM 5** — PIL ile metin bindirme (ADIM 4 sonrası)

## Network açıldığında çalıştırılacak komutlar

```bash
SLOT="2026-06-02-ikindi-15"
BRANCH="claude/zen-wozniak-xd0tq"

# ADIM 4 — Higgsfield submit + commit
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel-secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/$SLOT/raw/prompts.json

git pull --ff-only origin "$BRANCH"

# ADIM 5 — PIL metin bindirme
python3 scripts/overlay_text.py outputs/$SLOT/layout.json
```
