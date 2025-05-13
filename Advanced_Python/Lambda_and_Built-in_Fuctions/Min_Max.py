sayilar=[1,4,6,23,32,12]

harfler=['a','b','c','d']

isimler=["ahmet","ali","ada","yiğit"]


sonuc=min(sayilar)
sonuc=max(sayilar)
sonuc=max(harfler)
sonuc=max(harfler)


sonuc=min(isimler)
sonuc=max(isimler)



sonuc=min([len(isim) for isim in isimler])
sonuc=max([len(isim) for isim in isimler])

sonuc=max(isimler,key=lambda x:len(x))
sonuc=min(isimler,key=lambda x:len(x))

urunler=[
      {"title":"samsung s24","price":70000},
      {"title":"samsung s23","price":60000},
      {"title":"samsung s22","price":50000},
]

sonuc=min(urunler,key=lambda urun: urun["price"])
sonuc=max(urunler,key=lambda urun: urun["price"])["title"]



print(sonuc)