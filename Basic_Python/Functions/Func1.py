def selamlama():
    for i in range(10):
        print("hello world")

#selamlama()
def toplam():
    a=10
    b=20   
    print(a+b)
#toplam()

def toplam():
    return 10+20
sonuc=toplam()
#print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil()-2001
#print(yasHesapla())

def saat():
    import datetime
    return datetime.datetime.now().hour

def  selamla():
     if(saat()<12):
         return "Gunaydin :) "
     else:
         return "Selamlar :) "
#print(selamla())     


def selamver(isim):
    return "merhaba "+isim
#print(selamver("Emre"))

def toplam(s1,s2):
    return s1+s2

#print(toplam(50,10))

def yasHesapla(dogumTarihi):
    return yil()-dogumTarihi
#print(yasHesapla(2001))


def emeklilik(dogumYili,isim):
    yas=yasHesapla(dogumYili)
    kalansure=65-yas
    if(kalansure>0):
        return f"{isim} emeklilige kalan sure {kalansure} yil kaldi"
    else:
        return f"zaten {abs(kalansure)} yil once emekli oldunuz"
    
#Print(emeklilik(2001,"Emre"))


def selamver(isim,mesaj="Naber"):
    return f" {mesaj}  {isim}"

sonuc=selamver("emre","Selam")
#print(sonuc)

def usAl(t,u=5):
    return t**u
sonuc=usAl(2)

#   print(sonuc)

def topla (a,b):
    return a+b
def cikart(a,b):
    return a-b

def islem (a,b,fn=topla):
    return fn(a,b)

# print(islem(10,20,cikart))
# print(islem(10,20,topla))
# print(islem(10,20))


def full_name(firstname:str,lastname:str )-> str:
    return f"your name is {firstname} {lastname}"


sonuc= full_name(lastname="Yenen",firstname="Emre")
sonuc= full_name(firstname="Emre", lastname="Yenen")

#print(sonuc)

sayilar=(10,20,30,40)

def islem(sayilar):
     sonuc=0
     for i in  sayilar:
         sonuc +=i

     return sonuc

sonuc=islem(sayilar)
#print(sonuc)


def toplam2(*args):
    print(type(args))
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc

#print(toplam2(10,50,60,80,6))


# def display_user(*args):
#     print(type(args))
#     print(args)

# display_user()

# def display_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

   
# display_user()




def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        print("\n")

display_user(Username="EmreYenen")
display_user(Username="EmreYenen",email="info@emreyenen.com")
display_user(Username="EmreYenen",email="info@emreyenen.com",Country="Turkey")



def myfunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50,60,key1="value 1",key2="value 2") 