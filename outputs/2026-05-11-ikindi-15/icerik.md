# Sincap Kitap IG — İkindi 15:00 | 2026-05-11

## Konu
**Hayal Gücü** (0-6 yaş gelişiminde hayal kurmanın yeri ve onu beslemenin yolları.)

## Palette
**MERCAN**
- Arka plan: `#F08A7B`
- Aksan: `#FFF1D6` (krem)
- Metin: `#3A2418` (koyu kahve)

## Slide Metinleri

### Slide 1 — KAPAK
- Başlık ana: **Çocuğun Hayal Dünyası**
- Başlık aksan: **Sonsuzdur**
- Alt başlık: _Her küçük zihinde yepyeni bir evren büyür._

### Slide 2 — ÇERÇEVE
> Çocuklar hayal kurarken sadece oyun oynamaz; dünyayı anlamlandırır, duygularını işler ve yaratıcılığını besler. Bu hayaller, gelişimin en güçlü zeminidir.

### Slide 3 — ANAHTAR KAVRAM
- Başlık: **Hayal**
- Açıklama: _Hayal etmek, çocuğun zihninin en özgür alanıdır. Bu alanda kelimeleri, duyguları ve cesaretini birlikte büyütür._

### Slide 4 — UNUTMAYIN!
> Hayal gücünü beslemek için pahalı oyuncak gerekmez. Bir karton kutu uzay gemisi, bir battaniye sıcak bir mağara olabilir.
>
> **Bu akşam:** 'Bu kutu ne olsun?' diye sorun ve çocuğunuzun kurduğu oyuna onun fikriyle eşlik edin.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Prompt'lar

Ortak karakter: **baby fox** (yavru tilki)
Ortak arka plan: `#F08A7B` mercan
Boyut: 1152x1536, kalite 1080p

1. **Slide 1 (Kapak):** central baby fox character standing on a small soft hill, looking up dreamily, 2-3 small side objects floating around (paintbrush, open book, glowing star), decorative leaves and tiny clouds
2. **Slide 2 (Sahne):** rich cozy art table scene with baby fox, baby rabbit, and squirrel drawing together, papers and crayons scattered, paper airplanes flying, warm afternoon light, multiple small animal characters interacting
3. **Slide 3 (Kavram):** small baby fox wearing a paper crown looking up at a giant whimsical imaginary creature made of soft clouds and stars rising from an open book, dreamlike scale contrast, magical floating shapes around
4. **Slide 4 (Aktivite):** warm parent fox and child fox playing inside a cardboard box pretending it is a spaceship, household objects nearby (blanket cape, paper telescope), cozy living room corner, soft glowing lamp
5. **Slide 5 (Kapanış):** baby fox smiling and waving, sitting on a stack of small storybooks, surrounded by floating stars and tiny warm objects (acorns, leaves), friendly look

## Durum Notu

**Higgsfield görselleri bu çalışmada üretilemedi.** Vercel relay (`https://vercel-hf-probe.vercel.app/api/hf/submit`) bu oturumun IP'sini reddetti:

```
HTTP 403  {"_raw": "Host not in allowlist"}
```

Relay yalnızca Routine runner IP'lerini kabul edecek şekilde yapılandırılmış. Bu görev Claude Code üzerinden çalıştırıldığı için relay'in allowlist'inde yok.

**Çözüm seçenekleri:**
1. Aynı routine'u **Anthropic Routine UI** üzerinden çalıştır (whitelisted IP).
2. Vercel `vercel-hf-probe` projesinin allowlist'ine bu runner'ın IP/CIDR'sini ekle.
3. Görselleri manuel üret ve `assets/gorseller/2026-05-11-ikindi-15/slide-{1..5}.png` yoluna koy, ardından `python3 scripts/overlay_text.py outputs/2026-05-11-ikindi-15/layout.json` ile metin bindir.

Hazır olan tüm metin/prompt/layout dosyaları bu commit'te. Görseller geldiğinde overlay tek komutla çalışır.
