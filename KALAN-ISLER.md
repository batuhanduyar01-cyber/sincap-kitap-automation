# Repo Hazır — Kalan İşler

Cowork oturumunun ağ kısıtları nedeniyle fontlar sandbox'tan indirilemedi.
Kendi makinende yapman gereken son adımlar:

## 1. Logo ✅ (TAMAMLANDI)

`assets/logo.png` hazır — senin gönderdiğin dosya, beyaz arka plan kaldırıldı,
transparan PNG olarak kaydedildi.

## 2. Karakter Referansı ✅ (TAMAMLANDI — Opsiyon A)

`assets/character-reference.png` hazır — logodaki sincap karakteri kırpılıp
1024×1024 krem arka plan üzerine yerleştirildi. Higgsfield görseli üretmeye
gerek kalmadı.

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
- ✅ `assets/logo.png` (commit `c8afc77`)
- ✅ `assets/character-reference.png` (logo kırpımı — Opsiyon A)
- ⬜ `assets/fonts/BagelFatOne-Regular.ttf`
- ⬜ `assets/fonts/Baloo2-Regular.ttf`
- ⬜ 3 Routine'i claude.ai/code/routines'te oluştur
