# Sincap Kitap — İkindi 15:00 Carousel

- **Tarih:** 2026-05-13
- **Slot:** ikindi-15
- **Konu:** Cesaret
- **Ton:** Sıcak anne + bilge arkadaş — pedagojik ipucu ağırlıklı
- **Palette (ikindi turuncu):** bg `#E97E28`, accent `#FFFFFF`, text `#2A1810`

## Slide Metinleri

### Slide 1 — KAPAK
- title_main: "Küçük Yüreklerin"
- title_accent: "Büyük Cesareti"
- subtitle: "Çocuğunuzun cesareti nasıl filizlenir, nasıl beslenir?"

### Slide 2 — ÇERÇEVE
> Cesaret, korkunun yokluğu değildir. Korkuya rağmen küçük bir adım atmaktır. Çocuğunuz her yeni denemede bu kası biraz daha güçlendirir.

### Slide 3 — ANAHTAR KAVRAM
- başlık: **Cesaret**
- body: "Yeni bir oyuncak grubuna 'merhaba' demek, karanlık koridorda yalnız yürümek, hatasını söylemek… Çocuk için bunlar gerçek kahramanlıklardır."

### Slide 4 — UNUTMAYIN!
> Cesaret, "korkma" demekle değil, "yanındayım" demekle büyür. Sonucu değil, denemenin kendisini övün.
>
> **Bu akşam:** Çocuğunuza "Bugün hangi küçük cesaret adımını attın?" diye sorun.

### Slide 5 — KAPANIŞ
> Bu konuyu çocuğunuzla birlikte keşfetmek için Sincap Kitap'ı takip edin 🐿️

## Higgsfield Görsel Prompt Özetleri

1. Cesur poz veren sincap, etrafında hayran bakan tilki ve tavşan, küçük yıldız/yaprak detayları
2. Oyun parkı sahnesi — tilki ilk kez ip merdivene tırmanıyor, tavşan/baykuş cesaretlendiriyor
3. Küçük sincap tahta köprünün ucunda ilk adımını atıyor, anne sincap yanında izliyor (cesaret = ilk adım)
4. Akşam sahnesi — anne ve yavru sincap koltukta birlikte, sıcak fener ışığı, dizinde kitap
5. Sincap el sallıyor, etrafında küçük kitaplar, kakao, fener, palamut

## Durum Notu

Vercel HF relay (`vercel-hf-probe.vercel.app`) bu çalıştırmada **403 "Host not in allowlist"** döndü; bu oturumun çıkış IP'si relay allowlist'inde değil. Görsel üretim adımı (Higgsfield), bu yüzden tamamlanamadı. Tüm metin sanat eserleri (prompts.json, layout.json, caption.txt, icerik.md) hazır; Routine pipeline'ı üzerinden tekrar çalıştırıldığında `submit-batch` görselleri commit'leyebilir, ardından `overlay_text.py layout.json` çıktıları üretebilir.
