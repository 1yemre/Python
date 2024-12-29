
"""
    module1 (db)        : urunler
    module2 (methods)   : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)       :

    yeni ürün ekleme  => urunEkle("iphone 15", 60000)
    ürün güncelle     => urunGuncelle(1, "iphone 15 pro", 80000)
    ürünleri listele  => urunleriGetir()

"""


from methods import * 


sonuc=urunleriGetir()

# for i in sonuc:
#       print(i["urunAdi"])



urunEkle("iphone 20",90000)

for i in urunleriGetir():
      print(i["urunAdi"])


urunGuncelle(1,"iphone 15 pro max  ",75000)

print(sonuc)


for i in sonuc:
      print(i["urunAdi"])

