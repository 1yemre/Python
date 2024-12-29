import Module


sonuc=Module.sayi
sonuc2=Module.sayilar
sonuc3=Module.urunler
sonuc4=Module.urunler["urunadi"]
sonuc5=Module.urunler["renkler"]
sonuc6=Module.toplama(10,5)

print(sonuc6)


import Module as m #alias tanımladık
sonuc=m.sayilar

from Module import sayi,sayilar,urun #sadece seçili 
sonuc=sayi
sonuc=sayilar
sonuc=urun


from Module import * # tüm herşeyi aldık
sonuc=urun




print(sonuc)