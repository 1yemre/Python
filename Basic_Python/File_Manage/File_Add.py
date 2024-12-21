# open(dosya_adi, dosya_erisim_modu)
# dosya_erisim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu.
#     ** Dosyayı konumda oluşturur.
#     ** Dosya içeriğini siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.




# with open("dosya.txt","a",encoding="utf-8")as file :
#     file.seek(0)# işlevsel değilde  kaldığı yerden devam eder.
#     file.write("birinci satır\n")
  
# with open("dosya.txt","r+",encoding="utf-8")as file :
#     file.write("dortuncu satır\n")
  
# with open("dosya.txt","r+",encoding="utf-8")as file :
#     file.seek(20)# 20. degerden sonra yazar 
#     file.write("bes\n")
  
with open("dosya.txt","r+",encoding="utf-8")as file :
    file.read()#cursor en sona alır
    file.write("alti\n")
  
