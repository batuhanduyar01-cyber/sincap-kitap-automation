# Sincap Kitap IG — 2026-04-21 Sabah 09:00

## Konu
**Uyku direnci** (0-6 yaş)

## Palette
**MOR**
- Arka plan: `#7E5BA0`
- Aksan: `#C5E86C` (yeşil)
- Metin: `#FFFFFF` (beyaz)

## Karakter
Bear cub (ayı yavrusu) — 5 slide boyunca sabit.

## Slide Metinleri

### Slide 1 — KAPAK
- **Başlık:** "Anne, Bir Kitap"
- **Aksan:** "Daha?"
- **Alt başlık:** "Uyku direnci, bağ kurma çağrısıdır."

### Slide 2 — TANIDIK SAHNE
> Işığı söndürür söndürmez başlar: 'Anne, susadım. Anne, pipim var.' Bu sahne tanıdık geliyor mu?

### Slide 3 — ÇOCUĞUN SESİ
> "Yorgun değilim, sadece seninle biraz daha kalmak istiyorum."

### Slide 4 — UNUTMAYIN!
> Uyku direnci çoğu zaman yorgunluk değil, ayrılmakta zorlanmak demektir. Kısa ve sakin bir rutin güveni kurar. Bugün: yatmadan önce 10 dakika sadece ikiniz bir kitap okuyun.

### Slide 5 — KAPANIŞ
> Uykusuz geçen bu anlar, yıllar sonra en değerli anılar olacak. Sincap Kitap'ı takip et 🐿️

## Higgsfield Prompt'ları (her slide için üretilmiş)

**Ortak iskelet:**
```
Children's book illustration, watercolor gouache painting, textured brush strokes,
cute bear cub character, large expressive eyes, rosy blush cheeks, warm painterly
palette, solid #7E5BA0 background, Oliver Jeffers and Marc Boutavant style,
storybook art, no text, no frames, no borders, soft painterly shading,
portrait orientation, {SAHNE}
```

**Sahneler:**
- Slide 1: `big character standing on a small hill, decorative leaves and stars around, looking hopeful`
- Slide 2: `character with mother/parent character, warm hugging interaction, cozy indoor scene`
- Slide 3: `small isolated character, emotional vulnerable pose, vast empty space around (scale contrast), looking up`
- Slide 4: `family scene, parent and child reading book together, warm cozy bedroom setting`
- Slide 5: `character waving goodbye, smiling, sitting on a book stack`

**Ortak parametreler:** `--aspect-ratio 4:5 --resolution 1080p --quality high` + `character-reference.png` referansı.

## ⚠️ Higgsfield Üretimi — BLOKE

Bu ortamdan `platform.higgsfield.ai` API'sine yapılan istekler `HTTP 403 —
x-deny-reason: host_not_allowed` ile reddedildi. API, runner'ın IP'sini
allowlist'te tutmuyor. 

`outputs/2026-04-21-sabah-9/raw/slide-{1..5}-raw.png` dosyaları **geçici
placeholder** (solid `#7E5BA0` arka plan). Görsellerin asıl üretimi için:

1. Yukarıdaki promptları allowlist'te bir ortamdan (veya Higgsfield
   MCP/UI üzerinden) çalıştır.
2. Üretilen dosyaları aynı isimle `outputs/2026-04-21-sabah-9/raw/` altına koy.
3. Tekrar çalıştır: `python3 scripts/overlay_text.py outputs/2026-04-21-sabah-9/layout.json`

Final `slide-1.png … slide-5.png` dosyaları yeni raw'lar üzerinden otomatik
yeniden üretilir.

## Caption (özet)
400-500 kelimelik samimi anne dili caption, `caption.txt` dosyasında.
Kapanış: "Sincap Kitap'ı takip et 🐿️💜"

## Hashtag'ler (20 adet)
`#sincapkitap #çocukkitabı #annelik #06yaş #ebeveynlik #uykudirenci #uykurutini
#yatmasaati #tatlırüyalar #bebekuykusu #çocukuykusu #annelikyolculuğu
#erkenyıllar #ebeveyncocukbağı #annelikhali #anneolmak #anneninyükü
#çocukgelişimi #okulöncesi #annelikdestek`
