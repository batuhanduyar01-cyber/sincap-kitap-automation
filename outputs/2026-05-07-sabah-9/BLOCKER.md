# 2026-05-07 Sabah 09:00 — BLOKE

## Sorun
Vercel relay (`https://vercel-hf-probe.vercel.app`) bu Routine runner'ından gelen istekleri reddetti.

```
HTTP 403
x-deny-reason: host_not_allowed
body: "Host not in allowlist"
```

Hem `/api/hf/submit` hem `/api/hf/status` aynı yanıtı verdi. Yetki başlığı (`Authorization: Bearer …`) doğru gönderildi; sorun auth değil, **caller IP/host allowlist**.

## Yapılan Hazırlık (Bu commit'te kaydedildi)

- `logs/sabah-9.md` → `2026-05-07: uyku direnci` eklendi
- `outputs/2026-05-07-sabah-9/icerik.md` → konu, palette, karakter, 5 slide metinleri, Higgsfield prompt'ları
- `outputs/2026-05-07-sabah-9/caption.txt` → Instagram caption + 20 hashtag
- `outputs/2026-05-07-sabah-9/layout.json` → overlay config (görseller hazır olduğunda kullanılacak)
- `outputs/2026-05-07-sabah-9/prompts.json` → relay'e yeniden submit etmek için aynı 5 prompt

## Çözüm (insan müdahalesi gerekli)

Vercel `vercel-hf-probe` projesinin allowlist'i (kod tarafında bir `ALLOWED_HOSTS` veya `ALLOWED_IPS` env/config) Anthropic Routine runner outbound IP'sini içermiyor. Ya:

1. Routine runner'ın bugünkü çıkış IP'sini relay'in allowlist'ine ekle, **veya**
2. Allowlist'i tamamen kaldır (sadece shared-secret ile koru), **veya**
3. Allowlist mantığı bir başlığa (örn. `X-Routine-Token`) bağla, secret zaten Bearer'da var.

## Re-run

Allowlist düzeltildikten sonra:

```bash
cd /home/user/sincap-kitap-automation
export SLOT="2026-05-07-sabah-9"
export BRANCH="claude/quirky-mendel-jHGJP"
export RELAY_URL="https://vercel-hf-probe.vercel.app"
export RELAY_SHARED_SECRET="<gerçek secret>"
python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-05-07-sabah-9/prompts.json
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-07-sabah-9/layout.json
```
