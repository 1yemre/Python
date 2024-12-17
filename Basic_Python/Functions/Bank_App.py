#hesap bilgileri
#mennu,paracek,bakiyesorgula,parayetir fonk
#çekılmek istenen tutar hesapta yoksa ek hesabın kullanılmak istediği sorulacak

hesaplar=[
     {
          "Ad":"Emre Yenen",
          "HesapNo":"123456789",
          "Bakiye":20000,
          "EkHesap":5000,
          "Username":"emreyenen",
          "Password":"1234"
     },
     {
          "Ad":"Enes Yenen",
          "HesapNo":"123456789",
          "Bakiye":40000,
          "EkHesap":10000,
          "Username":"enesyenen",
          "Password":"1234"
     }

]


def menu(hesap):
    print("/n")

    print(f"Merhaba, {hesap["Ad"] }")  

    print("1-Bakiye Sorgula")
    print("2-Para Cekme")
    print("3-Para Yatirma")#sonra

    islem=input("islem seciniz :")

    if islem=="1":
         bakiye(hesap)
    elif islem=="2":
        paracek(hesap)
    elif islem==3:
        parayatir(hesap)     
    else:
        print("hatali secim")

    menu(hesap)



def parayatir(hesap):
    pass
def paracek(hesap):
    miktar=float(input(" Tutar :"))

    if(hesap["Bakiye"]) >= miktar:
        hesap["Bakiye"]-=miktar
        print("Paranız Hazır.")
    else:
       toplam=hesap["Bakiye"]+hesap["EkHesap"]

       if toplam >=miktar:
                EkHesapKullanimIzni=input("Yeterli paranız yok parayı tamamlamak için en hesap  limiti kullanılsın mı ? (e/h):")


                if EkHesapKullanimIzni=="e":
                        kullanilcakMiktar=miktar-hesap["Bakiye"]
                        hesap["Bakiye"]=0
                        hesap["EkHesap"] -=kullanilcakMiktar
                        print("Paranızı Alabilirsiniz . ")
                else:
                        print("Maalesef bakiyeniz yetersiz")
       else:
            print("Maalesef ekhesap ve hesap limitiniz tutarı çekmeye uygun degil..")     

def bakiye(hesap):
    print(f"Bakiye:{hesap["Bakiye"]}")
    print(f"Ek Hesap Bakiye:{hesap["EkHesap"]}")

def login():
    username=input("username : ")
    password=input("Password : ")

    isloggedIn=False

    for hesap in hesaplar:
        if hesap["Username"]== username and hesap["Password"]==password:
            isloggedIn=True
            menu(hesap)
            break
    
    if not(isloggedIn):
        print("Username yada Parola Yanlis")


login()