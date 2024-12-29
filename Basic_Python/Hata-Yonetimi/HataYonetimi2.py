#print(10/0)

# x=10
# if x>5:
#     raise ValueError("x den büyük olamaz.")


def renklendir(text,renk):
    renkler=("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalı ")
    if type(renk) is not str:
        raise TypeError("renk str tipinde olmalı ")
    
    if renk not in renkler:
        raise ValueError("gecersiz bir renk")

    print(f"{text} {renk} olarak yazıldı ")

try : 
    #renklendir(10,"red")
    renklendir("selam","red")
    renklendir("merhaba","white")
    renklendir("merhaba","purple")
except (TypeError,ValueError) as ex:
    print(ex)