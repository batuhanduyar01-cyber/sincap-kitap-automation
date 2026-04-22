# Sincap Kitap IG — 2026-04-22 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

Seçim gerekçesi: `logs/sabah-9.md` içinde son 14 gün boyunca kullanılmış konu yok (log boş); "uyku direnci" her yaş grubunu kesen, ebeveynlerin çok sık yaşadığı ama az konuşulan bir tema.

## Palette
**MOR** — gece / sakinlik / güven atmosferi için

| Rol | Hex |
|---|---|
| Arka plan | `#7E5BA0` |
| Aksan | `#C5E86C` (yumuşak yeşil) |
| Metin | `#FFFFFF` |

Not: Rota'da "sakinlik/uyku → TOZ MAVİSİ" öneriliyor, ancak `overlay_text.py` alıntı slide'ını (slide-3) sabit beyaz metinle çiziyor. Açık TOZ MAVİSİ arka plan üzerinde beyaz alıntı okunmazdı; MOR hem gece atmosferini veriyor hem de metin kontrastını koruyor.

## Karakter
**Bear cub (ayı yavrusu)** — 5 slide boyunca sabit, cozy / rahat / uyku-dostu çağrışım.

## 5 Slide Metinleri

### Slide 1 — KAPAK
- Başlık (ana): `Uykum Var Ama`
- Başlık (aksan): `Uyumak İstemiyorum!`
- Alt başlık: `Uyku direnci, güven arayışının sessiz sesidir.`

### Slide 2 — TANIDIK SAHNE
> Saat geç oldu, siz yorgunsunuz. "Bir hikâye daha..." derken küçük gözler hâlâ pırıl pırıl. Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> Gözlerimi kapatınca seni kaybedecekmişim gibi hissediyorum.

### Slide 4 — UNUTMAYIN!
> Uyku direnci inat değil, güven ihtiyacıdır. Öngörülebilir, sakin bir ritim gecenin korkutucu olmadığını hissettirir.
>
> **Bugün:** Uyku öncesi 15 dakikayı sadece ona ayırın; telefon başka odada kalsın.

### Slide 5 — KAPANIŞ
> Uyku savaşlarının yerine sessiz bir kucaklaşma koyabilirsin. Bu süreçte sana eşlik edecek kitaplar için Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'lar

Ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly
palette, solid #7E5BA0 background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading, portrait
orientation, {SAHNE}
```

| Slide | {SAHNE} |
|---|---|
| 1 | big bear cub character standing on a small hill, decorative leaves and stars around, looking hopeful |
| 2 | character with mother/parent character, warm hugging interaction, cozy indoor scene |
| 3 | small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up |
| 4 | family scene, parent and child reading book together, warm cozy bedroom setting |
| 5 | character waving goodbye, smiling, sitting on a book stack |

Ortak parametreler: `--aspect-ratio 4:5 --resolution 1080p --quality high --reference-image-url https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png`

## Çıktılar

| Dosya | Not |
|---|---|
| `slide-1.png` ... `slide-5.png` | Final kompozit slide'lar (overlay_text.py çıktısı) |
| `raw/slide-1-raw.png` ... `raw/slide-5-raw.png` | Ham zemin (bu çalıştırmada solid MOR placeholder) |
| `caption.txt` | Instagram caption + 20 hashtag |
| `layout.json` | overlay_text.py config |
| `icerik.md` | Bu rapor |

## Uyarılar / Tamamlanması Gereken Adımlar

> ⚠ **Higgsfield API bu sandbox'tan erişilemiyor.**
> `scripts/higgsfield_api.py` çağrısı `platform.higgsfield.ai` için `HTTP 403 — Host not in allowlist` döndürdü. Sandbox'ın egress proxy allowlist'i bu hostu bloklamış durumda (daha önce font CDN'leri için de yaşanan aynı kısıt — bkz `KALAN-ISLER.md`).
>
> Bu yüzden `raw/slide-*-raw.png` dosyaları **solid #7E5BA0 placeholder**. Final slide'lar (`slide-*.png`) bu zemin üzerine metin + logo bindirilerek üretildi.
>
> **Yapılması gereken (kendi makinende):**
> ```bash
> export HIGGSFIELD_API_KEY="b0ce4df9-80ac-44a3-8f9d-be0869a428e1"
> export HIGGSFIELD_API_SECRET="be73a38e07e4faebd09666eb51d1fe04eea7feea96d83b81ca4640d33531e35c"
>
> # 5 görseli sırayla üret (sahneler yukarıdaki tabloda)
> python3 scripts/higgsfield_api.py --prompt "<prompt>" \
>   --output outputs/2026-04-22-sabah-9/raw/slide-1-raw.png \
>   --aspect-ratio 4:5 --resolution 1080p --quality high \
>   --reference-image-url "https://raw.githubusercontent.com/batuhanduyar01-cyber/sincap-kitap-automation/main/assets/character-reference.png"
> # ... slide 2..5
>
> # Sonra tekrar overlay:
> python3 scripts/overlay_text.py outputs/2026-04-22-sabah-9/layout.json
> ```

> ⚠ **Fontlar yüklü değil.**
> `assets/fonts/BagelFatOne-Regular.ttf` ve `Baloo2-Regular.ttf` repoda yok (`KALAN-ISLER.md` madde 3). `overlay_text.py` PIL default font'a düştü — final slide'lardaki tipografi geçici. Fontlar eklenince aynı `layout.json` ile yeniden çalıştırılması yeterli.
