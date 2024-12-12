urunler = [
    {"urunAdi": "Hp Victu 1", "fiyat": 32999},
    {"urunAdi": "Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "Huawei Matebook", "fiyat": 26999},
    {"urunAdi": "Hp Victus 2", "fiyat": 20000}
]
# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
# "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."

        # for urun in urunler:
        #        print(f"{urun['urunAdi']} marka ürünün fiyatı{urun['fiyat']} $ dır.")

# 2- Ürünlerin fiyatları toplamı nedir?
# fiyat=0
# for urun in urunler:
#        fiyat += urun['fiyat']

# print(fiyat) 

# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.

# for urun in urunler:
#    if (urun["fiyat"] >= 2500 and urun["fiyat"] <= 4000):
#       print(f"{urun['urunAdi']}")
                  

# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.


# kelime =input("aramak istediğiniz uruun :")


# for urun in urunler:
#    if(urun["urunAdi"].lower().find(kelime.lower()) >-1):
#       print(f"{urun['urunAdi']}")



#5- klavyedem girişi istenen username bilgisi için boşluk girilidiği sürece tekrar girişi isteyiniz.

# username=""

# while not username:
#     username=input("kullanıcı adı: ")

# print("girilen username :"+username)




#6- klaveyden girilen n sayıdaki öğrenci liste içerisinde saklayınız.
# ** dic liste yapısı(ogrno, ogrename,ogresurname)
# ekleme bittiğinde öğrenci  listesini listele

# devammi="e"
# ogrenciler=[]
# while (devammi  !="h"):
#     ogrenciNo=input("ogrenci No:")
#     ogrenciSoyad=input("ogrenci Soyad:")
#     ogrenciAd=input("ogrenci Ad:")

#     ogrenciler.append({
#         "ogrenciNo" :ogrenciNo,
#         "ogrenciSoyad" :ogrenciSoyad,
#         "ogrenciAd" :ogrenciAd,

#     })

#     devammi= input("devam mı ? (e/h)")


# for ogrenci in ogrenciler:
#     print(f"Ogrenci Adı: {ogrenci['ogrenciAd']} Soyadı : {ogrenci['ogrenciSoyad']} Numarasi :{ogrenci['ogrenciNo']}")



 ##Range:

        # for i in range(1,100,2):
        #     print(i)


        # rng=range(10)
        # rng=range(10,20)
        # rng=range(100,200,10)
        # rng=range(0,-20,-1)
        # sonuc=list(rng)
        # print(sonuc)

        # for i in range(50,250):
        #     if(i%2==0):
        #         print(i)


##enumerate and zip

    # markalar=["opel","bmw","audi"]
    # index=1
    # for marka in markalar :
    #     print(f"{index}-{marka}")
    #     index+=1

    # obj1=enumerate(markalar,1)
    # print(type(obj1))
    # print(list(obj1))


    # for index,marka in enumerate(markalar,1):
    #     print(f"{index}-{marka}")


#zip 

numara=[100,200,300]
ogrenci=["ali","ayse","canan","mehmet"]

#print(list(zip(numara,ogrenci)))

for no,isim in zip(numara,ogrenci):
    print(no,isim)

