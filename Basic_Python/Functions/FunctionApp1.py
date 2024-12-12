#1 - Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def yazdir(text,adet):
    return text*adet

#print(yazdir("emre ",5))
    
# 2 - Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def hesapla(kisa,uzun):
    alan=kisa*uzun
    cevre=2*(kisa+uzun)

    return f"alan: {alan}  cevre: {kisa}"


#print(hesapla(20,50))

# 3 - Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

def yaziTura():
    import random
    sayi=random.random()
    
    if(sayi >0.5):
        return "tura"
    else:
        return "yazi"

#print(yaziTura())

# 4 - Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.


def asalsayibul(s1,s2):
    for sayi in range(s1,s2+1):
        if(sayi>1):
             for  i in range(2,sayi):
                 if(sayi%i==0):
                     break
             else:
                 print(sayi)
#asalsayibul(10,20)

# 5 - Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def bolenler(Sayi):
    tambolenler=[]
    for i in range(2,Sayi):
        if(Sayi%i==0):
            tambolenler.append(i)

    return tambolenler


print(bolenler(50))
