#!/usr/bin/env python3
"""sunum.src.html -> halay-sunum.html

Kaynak dosyadaki {{video:ID}} yer tutucularını, assets/yt/ altındaki
görselleri data URI olarak gömen video kartlarına çevirir. Artifact dış
resim yükleyemediği için görseller sayfanın içine gömülmek zorunda.

Çalıştırma:  python3 tools/build_sunum.py
"""
import base64, html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sunum.src.html"
OUT = ROOT / "halay-sunum.html"
YT = ROOT / "assets" / "yt"

# YouTube oEmbed ile doğrulandı (9 Kasım 2026). Kareler YouTube'un otomatik
# ürettiği hq1/hq2/hq3 görselleri: videonun yaklaşık %25, %50 ve %75'i.
VIDEOS = {
    "yqFDriQvloo": ("Horon Halkası: kurulum ve oyun", "Kaan Tan · TikMax",
                    "Her yorum halaya giren bir karaktere dönüşüyor, hediye gönderen horon başı oluyor."),
    "1gfako9AXVo": ("TikTok'ta halay ve horon yayınları gündem oldu", "Ahmet Balat",
                    "Akım haber gündemine girdi: yayıncılar izleyiciye halay çektirerek hediye topluyor."),
    "DB1KIqoU-Ls": ("Telefondan canlı yayın oyunu, bilgisayarsız", "Kaan Tan · TikMax",
                    "Oyun telefon tarayıcısında açılıyor, TikTok'un mobil oyun yayınıyla yayına alınıyor."),
    "Nc89U0eQeq4": ("QubeLive: hediyeyle harita fethi, 6 modül", "YT Automation",
                    "İl fethi, takım savaşı, kelime ve bayrak tahmini modülleri tek masaüstü yazılımında."),
    "yC-n6_BQtSI": ("Memleket: plakanı yaz, şehrinin kulesini yükselt", "TikQo",
                    "İzleyici plaka kodunu yazıyor, hediyeyle kendi şehrinin kulesini zirveye taşıyor."),
    "4ZDbtNAMCKg": ("Country Game: bayraklar sahada yarışıyor", "TikTok Interactive Game Store",
                    "Yorum ve hediyeyle ülkesine destek veren izleyiciler, sahaya bayrak küpleri yağdırıyor."),
    "n_uIgYamciQ": ("Düğün Konvoyu: izleyici arabasıyla katılıyor", "TikQo",
                    "Hediye gönderen izleyicinin arabası konvoya giriyor; büyük hediye öne geçiriyor."),
}


def uri(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


def card(vid):
    title, channel, desc = (html.escape(x) for x in VIDEOS[vid])
    url = f"https://www.youtube.com/watch?v={vid}"
    frames = "".join(
        f'<button class="frame" type="button" data-pos="%{p}" aria-label="{title}, videonun %{p} noktasındaki kareyi büyüt">'
        f'<img src="{uri(YT / f"{vid}-{k}.jpg")}" alt="" loading="lazy"><span>%{p}</span></button>'
        for k, p in ((1, 25), (2, 50), (3, 75))
    )
    return (
        f'<figure class="vcard" data-title="{title}" data-url="{url}">'
        f'<a class="vthumb" href="{url}" target="_blank" rel="noopener" aria-label="{title}, YouTube\'da izle">'
        f'<img src="{uri(YT / f"{vid}.jpg")}" alt="{title} videosunun küçük resmi">'
        f'<span class="vsrc">YouTube</span><span class="play" aria-hidden="true"></span></a>'
        f'<div class="frames" aria-label="Videodan kareler">{frames}</div>'
        f'<figcaption><b>{title}</b><small>{channel}</small><p>{desc}</p>'
        f'<a class="go" href="{url}" target="_blank" rel="noopener">YouTube\'da izle →</a></figcaption></figure>'
    )


text = SRC.read_text(encoding="utf-8")
text = re.sub(r"\{\{video:([A-Za-z0-9_-]{11})\}\}", lambda m: card(m.group(1)), text)
assert "{{" not in text, "çözülmemiş yer tutucu kaldı"
OUT.write_text(text, encoding="utf-8")
print(f"{OUT.name}: {OUT.stat().st_size/1024:.0f} KB")
