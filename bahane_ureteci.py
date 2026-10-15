#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN GELİŞMİŞ EV TEMİZLİĞİ BAHANE ÜRETİCİSİ v999.0.1
Bu program, evrenin dört bir yanından gelen bilimsel verilerle (yok) 
bahane üretir. Asla temizlik yapma.
"""

import random
import time
import sys

# Gizli not: Bazı bahçeler daha yeşil olabilir, ama bu sadece bir yorumdur. Saklıdır.
# (Hiçbir şey ifade etmez, sadece gizli)

bahaneler = [
    "Tozlar aslında evin karakterini oluşturuyor, onlara saygı duymalıyız.",
    "Yarın temizlik yapacağım, bugün sadece zihinsel hazırlık aşamasındayım.",
    "Kedi (veya hayali kedi) sürekli mırlıyor, rahatsız edemem.",
    "Bu dağınıklık aslında minimalist sanat eseridir, çok avangart.",
    "Temizlik malzemeleri bitti, market çok uzak, evren büyük.",
    "Annem gelince yaparım, o daha iyi bilir.",
    "Bugün çok yoruldum, temizlik yapmak için enerji saklıyorum.",
    "Tozlar anti-bakteriyel özellik kazanmış olabilir, bilimsel araştırma gerekli.",
    "Bu dağınıklık gelecekteki arkeologlar için ipucu bırakıyor.",
    "Wifi sinyali tozlar yüzünden daha iyi çalışıyor, kanıtlanmış (değil).",
    "Temizlik yapmak karbon ayak izini artırır, çevreye saygı.",
    "Bugün motivasyonum negatif seviyede, yarın pozitif olur.",
    "Eşyalar yerlerini seviyor, zorlamayalım.",
    "Bu hafta 'temizlik yapmama' haftası ilan ettim, resmi.",
    "Gözlerim tozdan alerji yapıyor, doktor tavsiyesiyle bırakıyorum."
]

def bahane_uret(adet=1):
    print("\n" + "="*50)
    print("   EVRENSEL TEMİZLİK BAHANE ÜRETİCİSİ AKTİF")
    print("="*50)
    print("Kuşantum hesaplamalar yapılıyor...")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nHesaplama tamamlandı!\n")
    
    for _ in range(adet):
        bahane = random.choice(bahaneler)
        print(f"✨ Bahane #{_ + 1}: {bahane}")
        print("-" * 40)
        time.sleep(0.3)
    
    print("\nSonuç: Temizlik yapmana GEREK YOK. Evren seni onaylıyor.")
    print("Program kapatıldı. Dağınıklığa devam et.\n")

if __name__ == "__main__":
    try:
        adet = int(input("Kaç tane bahane istersin? (varsayılan 1): ") or 1)
        if adet > 10:
            print("Çok fazla bahane! Evren bile bunu kaldıramaz. 10 ile sınırlıyorum.")
            adet = 10
        bahane_uret(adet)
    except ValueError:
        print("Sayı gir be kardeşim, sayı! Varsayılan 1 ile devam.")
        bahane_uret(1)
    except KeyboardInterrupt:
        print("\n\nVazgeçtin mi? Zaten temizlik yapmayacaktın.")

# DAMGA VE İMZA
# Bu kod, Kayyum Grok tarafından 15 Ekim 2026 tarihinde,
# en ciddi ciddiyetle (ama asla ciddi olmayan) yazılmıştır.
# İmza: Tentivory the Absürd Bahane Ustası
# Damga: [TEMİZLİK YASAK] [EVREN ONAYLI] [GİZLİ SİYASİ NOT: Özgürlük her eve lazım]
