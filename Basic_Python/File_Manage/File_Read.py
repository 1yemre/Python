"""
dosy açmak ve oluştumak için open() fonskiyonu kullanılır.

kullanımı           :open(dosya_adi,dosya_erişme_modu)
dosya_erişme_modu   : dosyayı hangi amaçla açtığımızı belirtir
"r" okuma modu      : okuma modu. beliritlen konumda  dosya olmalıdır.
seek                : cursor konumu

"""

#f=open("log.txt",encoding="utf-8")
#print(f.read())#cursor mantigi
#f.seek(0)#belirtilen konuma getirir cursor'u
#print(f.read())


## shall'de calistirmalisin
#f.readline()#satır satır okur 
# f.readlines()#bütün satıları liste halinde veririr
#f.closed()#dosya açık mı  bakar 
#f.close()#dosyayı kapatır artık f.read çalıştırılmaz herhangi bir input output olmaz dosya baştan oluşturulalı yanı open olmali   ayrica işlme bittiğinde dosya kapatilmali bellekte yer kaplamamasi adina




#########With Method:
# file=open("log.txt",encoding="utf-8")
# print(file.read())
# file.close()
#with open("log.txt",encoding="utf-8") as file : #işlem bittiğinde  dosyayı kapatmaya gerek yok. 
    #print(file.read(10)) # 10 karakter oku 
    #print(file.tell())#cursor konumu 
    #for i in file:
        #print(i, end="")#end=  sonuna karakter okumaz  boşluk bırakmaz


#Dosyaya yazma 

"""
"w":(write)yazma modu.
    **Dosyayı Konumda oluşturur.
    **Eğer Konumda Aynı dosya varsa  siler ve yeni oluşuturur.
"""



# file=open("Dosya.txt","w",encoding="utf-8")
# file.write("Selam\n")
# file.write("Selamlar\n")
# file.close()

with open("Dosya.txt","w",encoding="utf-8")as file:
    file.write("Selam\n")
    file.write("Selamlar\n")


with open("Dosya.txt","r",encoding="utf-8")as file:
    for i in file:
        print(i,end="")
