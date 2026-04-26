# Sincap Kitap IG — 2026-04-26 İkindi 15:00

**Konu:** Duygu Adlandırma
**Palette:** Turuncu / Toz Beyazı / Sıcak Kahve
- bg: `#E97E28`
- accent: `#FFFFFF`
- text: `#2A1810`

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** Çocuğunuz Hisseder Ama
- **Aksan:** Adını Bilmez
- **Alt:** Duygulara isim vermek küçük kalpleri rahatlatır.

### Slide 2 — ÇERÇEVE
> Çocuk öfkelendiğinde, üzüldüğünde ya da korktuğunda içinde yoğun bir kasırga eser. O kasırgaya bir isim vermek, ona görünür bir kıyı sunar. İsim verilen duygu, küçülmeye başlar.

### Slide 3 — ANAHTAR KAVRAM
- **Başlık:** Adlandır
- **Açıklama:** Duyguyu yüksek sesle söylemek, çocuğun karmaşasını anlam haritasına dönüştürür. *"Hayal kırıklığı yaşıyorsun."*

### Slide 4 — UNUTMAYIN!
> Çocuğunuza duygusunu söylerken yargılamayın, sadece tanımlayın. *"Kızgınsın, çünkü oyuncağın kırıldı."*
> **Bu akşam deneyin:** Yatmadan önce gününün en büyük üç duygusunu birlikte adlandırın.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Hashtag'ler
#sincapkitap #duyguadlandırma #çocukgelişimi #ebeveynlik #pedagoji #çocukpsikolojisi #duygudüzenleme #okulöncesi #anneblog #babablog #çocukkitabı #pozitifebeveynlik #bilinçliebeveynlik #anneçocuk #babaçocuk #küçükadımlar #duygulareğitimi #anneninnotu #sincapkitapailesi #çocuklailetişim

## Üretim Notları (Routine ortamında oluşmadı)

Higgsfield görselleri Routine sandbox egress allowlist'i tarafından bloklandı:
relay endpoint'i (`https://vercel-hf-probe.vercel.app/*`) tüm isteklere
`HTTP 403 "Host not in allowlist"` döndü. Sandbox sadece `github.com`,
`raw.githubusercontent.com` ve `pypi.org` gibi dar bir host kümesine izin
veriyor. Yani bu otomasyonun ADIM 4 (relay submit) kısmı bu çalışmada koşmadı.

### Manuel devam komutları (allowlist'i açık bir ortamdan)

```bash
SLOT="2026-04-26-ikindi-15"
BRANCH="claude/zen-wozniak-N4yR8"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek_secret>" \
python3 scripts/relay_api.py submit-batch \
    --slot "$SLOT" --branch "$BRANCH" \
    --prompts-file outputs/2026-04-26-ikindi-15/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-04-26-ikindi-15/layout.json
```

Hazır görseller `assets/gorseller/2026-04-26-ikindi-15/slide-{1..5}.png` olarak
commit'lendiğinde overlay adımı bu repo'daki `layout.json`'ı tüketip
`outputs/2026-04-26-ikindi-15/slide-{1..5}.png` üretir.
