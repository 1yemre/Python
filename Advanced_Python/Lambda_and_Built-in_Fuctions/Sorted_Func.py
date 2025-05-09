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
sonuc =sorted(users,key=lambda user :len(user["posts"]), reverse=True)



sonuc = list(map(lambda user : user["username"],sorted(users,key=lambda user :len(user["posts"]))))


kurslar = [
       {"title":"Pyhton","count":10000},
       {"title":"Php","count":8000},
       {"title":"javascript","count":5000}
]


sonuc= sorted(kurslar , key= lambda kurs :kurs["count"])
sonuc= sorted(kurslar , key= lambda kurs :kurs["count"], reverse=True)
sonuc= list(map(lambda kurs : kurs["title"],sorted(kurslar , key= lambda kurs :kurs["count"], reverse=True)))


print(sonuc)
