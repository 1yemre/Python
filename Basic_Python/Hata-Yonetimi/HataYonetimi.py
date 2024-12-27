#ZeroDivisionError

#ValueError

#SyntaxError

#NameError => tanımlanmamış deger kullanimi
   # print(ad) 

#TypeError =>Hatalı parametre kullanımı
#    len(10)    
# 10 + 'a'

#IndexError => yanlış index kullanımı
# liste=[10]
# liste[1]


#keyError => key hatasi 

# a={}
# a["ad"]

#AttributeError -> olamayan bir özelliğe  ulaşmak istediğmizde gelen hatalardır.

# "merhaba".upper() -> doğru 
# "merhaba".Upper() -> yanlış  

#################################################################


# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Y sıfır olamaz ")
# except ValueError:
#     print("x ve y sayi olmalidir. ")

# except:
#      print("Bilinmeyen bi hata")


# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError):  
#     print("x ve y sayi olmalidir.Sıfır olamaz.")
# except:
#      print("Bilinmeyen bi hata olustu")

# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e: #  hata hakkında log 
#     print("x ve y sayi olmalidir.Sıfır olamaz.")
#     print(e)
# except :
#      print("Bilinmeyen bi hata olustu")



try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e: 
   print("x ve y sayi olmalidir.Sıfır olamaz.")
   print(e)    
except Exception as e: #genel hatalar yakalanır
     print("Bilinmeyen bi hata olustu")
     print(e)
else:
    print("hersey yolunda")           
finally: #herzaman calisir.
    print("finally bloğu  calisti ")