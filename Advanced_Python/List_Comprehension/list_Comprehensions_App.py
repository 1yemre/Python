# 1 - (1-100) arasındaki sayılardan 12'ye tam bölünebilen sayı listesini oluşturunuz.

sayilar=[i for i in range(1,101) if i%3==0 if i%4==0 ] 
print(sayilar)



# 2 - Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
# text = "Hello 12345 World" => [1, 2, 3, 4, 5]

text="Hello 12345 World"
rakamlar=[i for i in text if i.isdigit()]
print(rakamlar)

# 3 - Sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehliskesi yazınız
# sicakliklar=[20,15,0,-5,-2]


sicakliklar=[20,15,0,-5,-2]
sonuc=[i if i>=4  else "buzlanma tehlikesi" for i in sicakliklar]
print(sonuc)



# 4 - Öğrenciler ve notlar listelerindeki notu 50'den fazla olan kişileri
# ekrana dict verisinde yazdırınız.
# öğrenciler = ["ali", "ahmet", "canan"]
# notlar = [50, 60, 80]
# => {"ahmet": 60, "canan": 80}

öğrenciler = ["ali", "ahmet", "canan"]
notlar = [50, 60, 80]

# Sadece 50'den büyük notlara sahip öğrenciler
başarılı_öğrenciler = {(öğrenciler[i], notlar[i]) for i in range(len(öğrenciler)) if notlar[i] > 50}

print(başarılı_öğrenciler)





# 5 - For döngüsüyle yazılan uygulamayı list comprehension ile yazınız.

#sonuc=[]
# for x in range(3):
#     for y in range(3):
#          for z in range(3):
#             sonuc.append((x,y,z))



sonuc=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(sonuc)