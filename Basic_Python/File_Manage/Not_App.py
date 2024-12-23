# Not uygulaması 

#1- Menu 
#   1-Not Gir
#   2-Ortalamaları göster
#   3-Notları Kayıt et 
#   4-Çıkış

def not_hesapla(satir):
    satir = satir.strip()
    if not satir:
        return ""
    if ":" not in satir:
        return ""

    liste = satir.split(":")
    if len(liste) < 2:
        return ""

    ogrenciAdi = liste[0].strip()
    notlar = liste[1].split("-")
    if len(notlar) < 3:
        return ""

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 90 <= ortalama <= 100:
        harf = "AA"
    elif 80 <= ortalama <= 89:
        harf = "BA"
    elif 75 <= ortalama <= 79:
        harf = "BB"
    elif 70 <= ortalama <= 74:
        harf = "CB"
    elif 65 <= ortalama <= 69:
        harf = "CC"
    elif 60 <= ortalama <= 64:
        harf = "DC"
    elif 50 <= ortalama <= 59:
        harf = "DD"
    elif 40 <= ortalama <= 49:
        harf = "FD"
    else:
        harf = "FF"

    return f"{ogrenciAdi} : {harf} ortalama : {ortalama}\n"


def not_gir():
    Ad = input("Ogrenci Ad :")
    Soyad = input("Ogrenci Soyad: ")
    Not1 = input("Not 1 :  ")
    Not2 = input("Not 2:  ")
    Not3 = input("Not 3 :  ")

    # Dosyayı doğrudan file_manage klasörüne aç
    with open("file_manage/sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(Ad + ' ' + Soyad + ' : ' + Not1 + '-' + Not2 + '-' + Not3 + '\n')


def notlari_oku():
    with open("file_manage/sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            sonuc = not_hesapla(satir)
            if sonuc:
                print(sonuc)


def notlari_kaydet():
    liste = []
    with open("file_manage/sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            sonuc = not_hesapla(satir)
            if sonuc:
                liste.append(sonuc)
                
    with open("file_manage/sonuclar.txt","w",encoding="utf-8") as file2:
        file2.writelines(liste)


while True:
    islem = input("1-Not Gir \n2-Notları Oku \n3-Notları Kayıt\n4-Çıkış\nSeçiminiz (1/2/3/4): ")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notlari_oku()
    elif islem == "3":
        notlari_kaydet()
    else:
        break
