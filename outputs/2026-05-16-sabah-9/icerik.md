# Sincap Kitap IG — 2026-05-16 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

Tekrar kontrolü: `logs/sabah-9.md` okundu — son 14 günde kayıtlı konu yoktu, tekrar riski yok. Konu loga eklendi.

## Palette
**AHUDUDU**

| Rol | Renk |
|---|---|
| Arka plan | `#E63B5C` |
| Aksan | `#C5E86C` (yeşil) |
| Metin | `#FFFFFF` (beyaz) |

Gerekçe: Öfke nöbetleri yoğun, sıcak bir duygu konusu → "sıcak duygu" eşleşmesi AHUDUDU.

## Karakter
**Bear cub (ayı yavrusu)** — 5 slide boyunca sabit.

---

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık (ana):** Öfke Geldi,
- **Başlık (aksan):** Geçecek
- **Alt başlık:** Öfke nöbetleri, büyümenin gürültülü bir parçasıdır.

### Slide 2 — TANIDIK SAHNE
> Markette, herkesin gözü önünde çocuğunuz yere yatıyor. Yüzünüz kızarıyor, ne yapacağınızı bilemiyorsunuz. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "İçimde kocaman bir fırtına var, onu nasıl durduracağımı bilmiyorum."

### Slide 4 — UNUTMAYIN!
> Öfke nöbeti bir terbiyesizlik değil, gelişen bir beynin taşkınlığıdır. Siz sakin kaldıkça çocuğunuz güvende hisseder. Bugün: önce kucağınızı açın, konuşmayı fırtına dindikten sonraya bırakın.

### Slide 5 — KAPANIŞ
> Her fırtınadan sonra mutlaka sakin bir liman gelir; o liman sizsiniz. Duyguları birlikte tanımanıza eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

---

## Higgsfield Prompt'lar

Ortak iskelet: watercolor gouache, bear cub karakter, solid `#E63B5C` arka plan, Oliver Jeffers + Marc Boutavant stili, 1152x1536, 1080p. Tam prompt'lar `prompts.json` dosyasında.

| Slide | Sahne |
|---|---|
| 1 | big bear cub standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | bear cub with caring mother bear character, warm hugging interaction, cozy indoor scene |
| 3 | small isolated bear cub, emotional vulnerable pose, vast empty space around for scale contrast, looking up |
| 4 | family scene, mother bear and bear cub reading a book together, warm cozy bedroom setting |
| 5 | bear cub waving goodbye, smiling, sitting on a stack of books |

---

## Caption
Tam metin + hashtag'ler: `caption.txt` (20 hashtag dahil).

---

## ÜRETİM DURUMU — GÖRSELLER EKSİK

ADIM 4 (Higgsfield görselleri) bu ortamda **tamamlanamadı**.

- Relay submit `HTTP 403 "Host not in allowlist"` döndü.
- Bu çalışma ortamının ağ politikası `vercel-hf-probe.vercel.app` host'una çıkışı blokluyor (GitHub'a erişim açık).
- `relay_api.py` exit kodu 3 (submit başarısız) ile durdu — bu kalıcı bir politika bloğu, geçici ağ hatası değil; retry çözmez.

Sonuç olarak üretilemeyenler:
- `assets/gorseller/2026-05-16-sabah-9/slide-1..5.png` (ham Higgsfield çıktıları)
- `outputs/2026-05-16-sabah-9/slide-1..5.png` (metin bindirilmiş final)
- `outputs/2026-05-16-sabah-9/raw/slide-*-raw.png`

### Görselleri tamamlamak için (ağ politikası düzeltildikten sonra)
```bash
SLOT="2026-05-16-sabah-9"
BRANCH="claude/quirky-mendel-gfYCM"

RELAY_URL="https://vercel-hf-probe.vercel.app" \
RELAY_SHARED_SECRET="<gerçek değer>" \
python3 scripts/relay_api.py submit-batch \
  --slot "$SLOT" --branch "$BRANCH" \
  --prompts-file outputs/2026-05-16-sabah-9/prompts.json

git pull --ff-only origin "$BRANCH"
python3 scripts/overlay_text.py outputs/2026-05-16-sabah-9/layout.json
```

Metin, palette, karakter, prompt'lar ve `layout.json` hazır; sadece görsel adımı tekrar çalıştırılmalı.
