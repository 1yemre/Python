liste = ["1", "3", "5", "200", "abc", "10a", "60"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         sonuc=int(x)
#         print(sonuc)
#     except ValueError:
#          continue






# 2: Kullanıcı 'quit' (q) değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz,
# aksi halde hata mesajı yazın.

# while True:
#     sayi = input("sayı : ")
#     if sayi == "q":
#         break
    
#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayi  {sonuc}")
#         break
#     except ValueError:
#         print("gecersiz sayi")
#         continue


# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonunu hazırlayınız.

urun = {"urunAdi": "samsung s10","fiyat":10000}

# d["fiyat"] => KeyError
# get(urun, "fiyat") => None
# get(urun, "urunAdi") => samsung s10


def get (liste,key):
    try: 
        return liste[key]
    except KeyError:
        return None


sonuc=get(urun,"fiyat")
print(sonuc)