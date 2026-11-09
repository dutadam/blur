# Halay Ekonomisi

TikTok LIVE interaktif oyunlarının Türkiye fırsatını anlatan tek sayfalık interaktif site.

## Dosyalar
- `index.html` — tarayıcıda doğrudan açılan tam sürüm (yerelde geliştirme için).
- `halay-ekonomisi.html` — claude.ai artifact'ına yayınlanan kaynak. Başında `<!doctype>`, `<html>`, `<body>` yok; artifact bunları kendisi ekliyor.

- `sunum.src.html` — mobil oyun şirketine yönelik interaktif sitenin kaynağı. Video kartları `{{video:ID}}` yer tutucusu olarak duruyor.
- `halay-sunum.html` — `python3 tools/build_sunum.py` ile üretilen, görselleri data URI olarak gömülü sayfa. Artifact'a bu yayınlanır.
- `assets/yt/` — YouTube küçük resimleri (`ID.jpg`) ve videodan kareler (`ID-1/2/3.jpg`, videonun ~%25/%50/%75 noktası).

## Mobil oyun şirketi sürümü
https://claude.ai/artifact/9Jvv4famfe3LiaB79QgWnx

- Tek sayfa, üstte yapışkan menü (Nasıl çalışır, Pazar, Neden siz, Demo, Formatlar, Rakipler, Gelir, Ortaklık, Pilot). Her bölümün adresi var (`#demo`, `#gelir`…).
- Video karelerine tıklayınca büyür; ← → ile gezilir, Esc kapatır.
- Video eklemek: görselleri `https://i.ytimg.com/vi/ID/{maxresdefault,hq1,hq2,hq3}.jpg` adresinden indirip `assets/yt/` altına koy, `tools/build_sunum.py` içindeki `VIDEOS` sözlüğüne ekle, kaynağa `{{video:ID}}` yaz ve build'i çalıştır.
- Aynı linki korumak için: "halay-sunum.html dosyasını https://claude.ai/artifact/9Jvv4famfe3LiaB79QgWnx artifact'ına yayınla"

## Yayındaki artifact (site)
https://claude.ai/artifact/95frjoa4HKVX6KbUiUmAuk

Aynı linki korumak için Claude Code'a şunu söyle:
"halay-ekonomisi.html dosyasını https://claude.ai/artifact/95frjoa4HKVX6KbUiUmAuk artifact'ına yayınla"

## Yapı
- Tek dosya: HTML + CSS + JavaScript, kütüphane yok.
- Fontlar Google Fonts'tan (Bricolage Grotesque, Figtree, JetBrains Mono).
- Simülasyonlar `<canvas>` ile çiziliyor: `halay`, `halay2` (aynı yayının küçük kopyası), `map`, `race`, `mahalle`.
- Gelir hesaplayıcı `calc()` fonksiyonunda; kur `FX` sabitinde (varsayılan 42 TL).

## Artifact kuralları (değişiklik yaparken)
- Dış resim, iframe (YouTube dahil) ve fetch engelli; görselleri data URI olarak göm.
- Scriptler sadece cdnjs, jsDelivr, unpkg gibi izinli CDN'lerden yüklenebilir.
- Sayfa 400px genişlikte de çalışmalı; yatay kaydırma olmamalı.

## Yapılacaklar
- Site sürümündeki video kartlarına da sunumdaki gerçek görselleri taşımak.
