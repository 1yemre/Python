# Sorted : 

sayilar = [1,53,4,5,65,23]
#sayilar.sort()
sonuc= sorted(sayilar)
sonuc= sorted(sayilar,reverse=True) # azalan şekilde

#print(sayilar)

users=[
      {"username":"EmreYenen","posts":["post1","post2"],"email":"info@abc.com","phone":"1234"},
      {"username":"EnesYenen","posts":["post1"],"email":"info@abcd.com"},
      {"username":"YeneneEmre","posts":["post1"],"email":"info@abcd.com"}
]



sonuc =sorted(users,key=len)
sonuc =sorted(users,key=len , reverse= True)
sonuc =sorted(users,key=lambda user :user["username"])
sonuc =sorted(users,key=lambda user :len(user["posts"]))




print(sonuc)
