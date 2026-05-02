# Sincap Kitap IG — 2026-05-02 Öğle 12:00

**Konu:** Diş fırçalatmama (çocuk perspektifinden, alıntı ağırlıklı)
**Palette:** TOZ MAVİSİ `#C9DDEC`
**Karakter:** Sevimli minik sincap (Sincap Kitap mascot)

---

## Slide 1 — KAPAK
- **title_main:** "Dişlerimi Fırçalatmak"
- **title_accent:** "İstemiyorum!"
- **subtitle:** "Küçük bir sincabın büyük inadı."

## Slide 2 — ÇOCUĞUN SESİ 1 (sevgi)
> "Anneciğim, seni çok seviyorum ama o fırça benim ağzıma çok büyük geliyor!"

## Slide 3 — ÇOCUĞUN SESİ 2 (ihtiyaç)
> "Dişlerim minicik, dünyam kocaman... acaba fırça da benimle birlikte büyür mü?"

## Slide 4 — EBEVEYN NOTU
- **title_accent:** "Ebeveyn Notu"
- **body:** "Diş fırçalama bir savaş değil, bir bağ kurma anı olabilir. Çocuğunuza fırçayı seçtirin, aynanın önünde birlikte fırçalayın. İpucu: Sevdiği bir şarkıyla iki dakika sayın."

## Slide 5 — KAPANIŞ
- **body:** "İyi geceler! Yarın yeni maceralar bizi bekliyor. Sincap Kitap'ı takip et 🐿️"

---

## ⚠ Görsel Üretimi — Bu Çalıştırmada Tamamlanamadı

Higgsfield çağrısı için kullanılan Vercel relay (`https://vercel-hf-probe.vercel.app`) Anthropic Routine sandbox'ının çıkış proxy'sinde **host allowlist'te değil**:

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

Aynı blok `api.higgsfield.ai` ve `higgsfield.ai` için de geçerli — yani relay'i atlayıp doğrudan HF'ye gitmek de mümkün değil. Sandbox'ın allowlist'ine `vercel-hf-probe.vercel.app` (ve mümkünse `*.vercel.app`) eklendiğinde aşağıdaki komut tekrar çalıştırılarak görseller üretilebilir:

```bash
SLOT="2026-05-02-ogle-12"
BRANCH="claude/confident-dijkstra-K5DaJ"
RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<vercel'deki gerçek secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" --prompts-file outputs/2026-05-02-ogle-12/prompts.json
```

Görseller geldikten sonra:

```bash
git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-02-ogle-12/layout.json
```

`prompts.json` ve `layout.json` bu klasörde hazır beklemektedir.
