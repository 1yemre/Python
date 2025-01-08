sayilar=[1,3,5,-4,-3]

# def NegatifSayilar(x):
#     if x < 0 :
#          return True
#     else:
#          return False
    
#sonuc=list(filter(NegatifSayilar,sayilar))

sonuc=list(filter(lambda x: x<0 ,sayilar))
sonuc=list(filter(lambda x: x %2==1,sayilar))





isimler=["cinar","Ali","Ada","Yiğit","Sena"]
sonuc=list(filter(lambda x: x[0]=='A',isimler))

filterResult=list(filter(lambda x: x[0]=='A',isimler))
sonuc=list(map(lambda x: x.upper(),filterResult))
print(sonuc)