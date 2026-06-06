# Sincap Kitap IG Post — 2026-06-06 Sabah 09:00

## Konu
**Öfke nöbetleri** (0-6 yaş)

## Palette
**MERCAN**
- Arka plan: `#F08A7B`
- Aksan: krem `#FFF1D4`
- Metin: koyu kahve `#4A2C1A`

Neden bu palette? Öfke yoğun bir duygu — ama bu konudaki sosyal medya yaklaşımımız "tutma, kucaklama" üzerine. Mercan, yoğunluk ve şefkatin buluştuğu yer; ne çiğ ne soğuk.

## Karakter
**Kirpi (hedgehog)** — dışı dikenli, içi yumuşak. Öfke nöbetlerini yaşayan çocuğun metaforu.

## Slide Metinleri

### Slide 1 — Kapak
- **Ana başlık:** Küçük Bedende
- **Aksan:** Büyük Fırtına
- **Alt başlık:** Öfke nöbetleri, ifade edilemeyen duyguların sesidir.

### Slide 2 — Tanıdık sahne
> Markette bir anda yere yatıyor, bağırıyor, tekmeliyor. Etraftakilerin bakışları üzerinizde. Bu sahne tanıdık geliyor mu?

### Slide 3 — Çocuğun sesi (alıntı)
> "İçimde bir şey patlıyor ama nasıl söyleyeceğimi bilmiyorum."

### Slide 4 — UNUTMAYIN!
> Öfke nöbetleri, çocuğunuzun yaramaz olduğunun değil, henüz duygularıyla baş edemediğinin işaretidir.
> **Bugün:** Sakin bir nefes alın, yanına oturun ve sadece "Yanındayım" deyin.

### Slide 5 — Kapanış
> Fırtınalar geçer, sevgi kalır. Bu yolculukta yalnız değilsin. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları

Her slide için ortak iskelet:
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute hedgehog character, large expressive eyes, rosy blush cheeks, warm painterly palette,
solid #F08A7B background, Oliver Jeffers and Marc Boutavant style, storybook art,
no text, no frames, no borders, soft painterly shading, portrait orientation, {SAHNE}
```

Sahne değişkenleri:
1. big hedgehog character standing on a small hill, decorative leaves and stars around, looking hopeful and gentle
2. hedgehog child with mother hedgehog character, warm hugging interaction, cozy indoor scene, comforting embrace
3. small isolated hedgehog character, emotional vulnerable pose with tears in eyes, vast empty space around for scale contrast, looking up with overwhelmed expression
4. family scene, mother hedgehog and child hedgehog reading a picture book together, warm cozy bedroom setting, soft lamplight
5. hedgehog character waving goodbye, smiling kindly, sitting on a stack of colorful books

## Üretim Durumu

| Adım | Durum |
|---|---|
| Konu seçimi | ✅ |
| Metin üretimi | ✅ |
| Palette seçimi | ✅ |
| Higgsfield prompt hazırlama | ✅ |
| Higgsfield görsel üretimi | ❌ **BLOKE** — Vercel relay 403 "Host not in allowlist" |
| Text overlay | ⏳ Görseller gelince çalıştırılacak |
| Caption + hashtag | ✅ |

## Hata Notu — Vercel Relay

`RELAY_SHARED_SECRET` olarak gönderilen `78e1e7737a34f6c5596763be8e78e5025257f12f130c5843c9f46f80e34645a4` değeri relay tarafından kabul edilmedi — 403 `Host not in allowlist` döndü.

Routine'in prompt tanımında belirtildiği gibi, bu değer "Routine UI'ye paste ederken" gerçek Vercel `RELAY_SHARED_SECRET` ile değiştirilmeliydi; muhtemelen placeholder olarak kaldı.

**Aksiyon:** Vercel dashboard → `vercel-hf-probe` projesi → Settings → Environment Variables → `RELAY_SHARED_SECRET` değerini al, Routine prompt'undaki ilgili yere yapıştır ve routine'i tekrar çalıştır. Yeni çalıştırma:
1. Bu `layout.json` ile aynı isimle slot'a düşer (`2026-06-06-sabah-9`).
2. Görseller gelince `python3 scripts/overlay_text.py outputs/2026-06-06-sabah-9/layout.json` ile final slide'lar üretilir.

Tüm metin/palette/karakter kararları bu dosyada hazır — sadece görseller eksik.
