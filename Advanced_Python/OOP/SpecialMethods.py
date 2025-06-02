liste=[1,2,3]

print(len(liste))

# sayi=10


s="Hello world!"
print(len(s))



class  movie :
       def __init__(self,title,director,year,duraction):
            self.title=title
            self.director=director
            self.year=year
            self.duraction=duraction
       

       def __repr__(self):
              return f"{self.title},{self.director} tarafından  {self.year} yılında yayınlandı"
       
       def __len__(self): 
             return self.duraction
       
       def  __del__(self):
             print("film silindi")

m=movie("film adı","yönetmen","yayın tarihi",120)

print(m.__repr__())
print(len(m))


del m 


