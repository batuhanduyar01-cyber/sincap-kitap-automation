# Rapor — 2026-06-18 Sabah 09:00

## Durum: ⚠️ KISMI BAŞARI — Görseller üretilemedi

### Seçilen Konu
**uyku direnci**

### Seçilen Palette
**TOZ MAVİSİ** (`bg=#C9DDEC`, `accent=#E97E28`, `text=#3A2A1A`)

### Karakter
Baby squirrel (5 slide boyunca sabit)

### Hazırlanan Dosyalar
- `icerik.md` — konu, palette, 5 slide metni, Higgsfield prompt'lar
- `caption.txt` — Instagram caption + 20 hashtag
- `layout.json` — overlay_text.py için config
- `higgsfield-prompts.json` — relay'e gönderilecek prompt batch'i

### Caption İlk 3 Satır
```
Anne, uykum gelmiyor… 🌙

Gece on bir. Sen yorgunsun, üstündeki güne bir gün daha eklemişsin. Ama o, battaniyenin altında bir balıklava gibi kıvranıyor. Bir su istiyor, bir hikaye istiyor, bir "anne, biraz daha"…
```

## Görsel Üretim — Engel

ADIM 4 (Higgsfield via Vercel relay) **çalıştırılamadı**. Çıktı:

```
[relay_api] Submitting 5 prompt to relay (slot=2026-06-18-sabah-9, branch=claude/quirky-mendel-xli932)
[relay_api] submit HTTP 403: {"_raw": "Host not in allowlist: vercel-hf-probe.vercel.app.
Add this host to your network egress settings to allow access."}
```

Anthropic Routine ortamının network egress allowlist'inde `vercel-hf-probe.vercel.app` yok.

### Çözüm — Kullanıcı tarafı

1. Routine ayarlarına gir (Claude Code on the web → environment / network policy).
2. Outbound allowlist'e ekle: `vercel-hf-probe.vercel.app`
3. Aynı düzeltme `ogle-12` ve `ikindi-15` routine'leri için de gerekli.
4. Bir sonraki tetiklemede (veya manuel run'da) görsel üretimi normale döner.

### Manuel Devam — Lokal Makinede

Egress düzeltilene kadar bu post'u lokal makinede tamamlamak için:

```bash
git fetch origin claude/quirky-mendel-xli932
git checkout claude/quirky-mendel-xli932

SLOT="2026-06-18-sabah-9"
BRANCH="claude/quirky-mendel-xli932"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" \
    --branch "$BRANCH" \
    --prompts-file outputs/$SLOT/higgsfield-prompts.json

git pull --ff-only origin "$BRANCH"

python3 scripts/overlay_text.py outputs/$SLOT/layout.json
```

### 14 Gün Tekrar Log'u
`logs/sabah-9.md` dosyasına `- 2026-06-18: uyku direnci` satırı eklendi.
