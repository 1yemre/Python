sayilar=[1,3,5,4,32,56]

sonuc=sum(sayilar)#tüm sayıların toplamını  verir.
sonuc=sum(sayilar,15)


products=[
    {"title":"iphone 13", "price":60000},
    {"title":"iphone 14", "price":70000},
    {"title":"iphone 15", "price":80000},
    {"title":"iphone 18", "price":0}

]

toplamFiyat=sum([urun["price"] for urun in  products])
urunAdeti=len([urun for urun in products if urun["price"]>0])
sonuc=toplamFiyat/urunAdeti

 
sonuc=round(5.3)# en yakın tam sayıya yuvarlar.
sonuc=round(5.6)
sonuc=round(5.5)
sonuc=round(1.32)
sonuc=round(1.321233,2)# iki basamak olarak deger  dondurur.
sonuc=round(1.321233,4)
sonuc=round(1.321253,4)





print(sonuc)