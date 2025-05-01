#lambda arguments :expression

def KareAL(a):
    return a**2

sonuc=KareAL(5)
##########


sonuc=(lambda a :a**2)(3)

KareAL= lambda a : a**2 
sonuc=KareAL(4)




toplam=lambda a,b,c : a+b+c
sonuc=toplam(1,2,3)




def myFunc(n):
    return lambda a : a*n

carpma2=myFunc(2)
carmpa3=myFunc(3)
carmpa5=myFunc(5)


sonuc=carpma2(3)
sonuc=carmpa3(5)
sonuc=carmpa5(2)
print(sonuc)