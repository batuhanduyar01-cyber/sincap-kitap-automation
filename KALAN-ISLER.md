# Repo Hazır — Kalan 3 Manuel İş

Cowork oturumunun ağ kısıtları nedeniyle 3 varlık sandbox'tan indirilemedi.
Kendi makinende yapman gereken son adımlar:

## 1. Logo (senin dosyan)

`assets/logo.png` → Sincap Kitap baykuş logosu (gözlüklü kahverengi baykuş +
altında "SİNCAP KİTAP" yazısı). Transparan arka plan, ~400×400 veya daha
büyük PNG. Mevcut dijital dosyandan kopyala.

## 2. Karakter Referansı (Higgsfield ile üret)

Cowork sandbox'undan Higgsfield'a erişemedim. Kendi makinende Claude Code
veya Cowork'te bir kez çalıştır:

```
higgsfield_soul_text_to_image:
  prompt: "Cute brown baby squirrel character mascot with large round black
    glasses, children's book style, watercolor gouache painting, soft textured
    brush strokes, large expressive eyes, rosy blush cheeks, friendly warm
    smile, standing front-facing full body portrait pose, solid cream
    background, Oliver Jeffers and Marc Boutavant illustration style, storybook
    art, no text, no frames, no borders, painterly shading, high detail, clean
    edges, centered composition"
  aspect_ratio: "1:1"
  resolution: "1080p"
  quality: "high"
```

Çıkan görseli `assets/character-reference.png` olarak kaydet.

## 3. Fontlar

Cowork sandbox'unun proxy allowlist'i GitHub raw içeriği ve font CDN'lerini
blokluyor. Kendi makinende:

```bash
cd assets/fonts
curl -L -o BagelFatOne-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/bagelfatone/BagelFatOne-Regular.ttf"
curl -L -o Baloo2-Regular.ttf \
  "https://github.com/google/fonts/raw/main/ofl/baloo2/Baloo2%5Bwght%5D.ttf"
```

## 4. GitHub'a Push

Bu klasör zaten bir git repo — ilk commit atıldı (`076e7bc`). GitHub'da
boş bir repo aç (`sincap-kitap-automation`), sonra:

```bash
cd sincap-routines
# 3 dosyayı ekledikten sonra:
git add assets/logo.png assets/character-reference.png assets/fonts/*.ttf
git commit -m "Add logo, character reference, fonts"

git remote add origin git@github.com:<KULLANICI-ADIN>/sincap-kitap-automation.git
git push -u origin main
```

## 5. Routine Oluşturma

`BURADAN-BASLA.md` dosyasının 4. adımı. claude.ai/code/routines üzerinde
3 Routine oluştur, her birine `prompts/routine-*.md` içeriğini yapıştır.

---

**Hazır olan her şey**:
- ✅ Klasör yapısı
- ✅ 3 Routine prompt'u (sabah/öğle/ikindi)
- ✅ Python PIL overlay scripti (180+ satır, 6 slide tipi)
- ✅ Boş log dosyaları (14-gün tekrar kontrolü için)
- ✅ requirements.txt, README, .gitignore
- ✅ Git repo initialized + initial commit
- ✅ CHECKLIST ve başlangıç rehberi

**Senin eklemen gerekenler**:
- ⬜ `assets/logo.png` (mevcut dijital dosyandan)
- ⬜ `assets/character-reference.png` (Higgsfield ile)
- ⬜ `assets/fonts/BagelFatOne-Regular.ttf`
- ⬜ `assets/fonts/Baloo2-Regular.ttf`
- ⬜ GitHub remote + push
- ⬜ 3 Routine'i claude.ai'de oluştur
