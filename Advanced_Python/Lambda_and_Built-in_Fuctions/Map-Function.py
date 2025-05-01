Sayilar=[1,2,3,4,5]
Sayilar_str=["1","2","3","4","5"]
isimler=["emre","enes","ali","veli"]
kullanicilar=[
        {
              "ad":"Ali",
              "soyad":"Yılmaz"
        },
        {
              "ad":"Ahmet",
              "soyad":"Yılmaz"
        }
]


# kareleri=[]

# for sayi in Sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)




def Kareal(sayi):
    return sayi **2 

sonuc =list(map(Kareal,Sayilar))





sonuc =list(map(lambda sayi: sayi** 2 ,Sayilar))
sonuc=list(map(int,Sayilar_str))
sonuc=list(map(str.upper,isimler))
sonuc=list(map(lambda kisi: kisi["ad"],kullanicilar))

print(sonuc)


