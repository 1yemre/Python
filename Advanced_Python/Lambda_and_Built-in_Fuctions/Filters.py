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

users=[
    {"username":"EmreYenen","posts":["post1","post2"]},
    {"username":"EnesYenen","posts":[]},
    {"username":"EmreEnesYenen","posts":["post1","post2","post3"]},
    {"username":"EnesEmreYenen","posts":["post1","post2","post3","post4"]}
]


sonuc=list(filter(lambda u: len(u["posts"])>2 , users))


filterUsers=list(filter(lambda u: len(u["posts"])==0 , users))

##sonuc=list(map(lambda u:u["username"],filter(lambda u: len(u["posts"])>2 , users))) // uzun yolu 

sonuc=list(map(lambda u:u["username"],filterUsers))


sonuc = [user["username"].upper() for user in users if len(user["posts"]) > 0]




print(sonuc)