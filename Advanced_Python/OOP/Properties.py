class product:
    def __init__(self,name,price):
        self.name=name
        if price>=0:
          self._price=price
        else:
           raise ValueError("ürün fiyati negatif olamaz! ")

    @property
    def price(self):
       return self._price 

    @price.setter
    def price(self,value):
        if value>=0:
         self._price=value
        else:
           raise ValueError("ürün fiyati negatif olamaz! ")
        
    # def set_price(self,value):
    #     if value>=0:
    #       self._price=value
    #     else:
    #        raise ValueError("ürün fiyati negatif olamaz! ")

    # def get_prise(self):
    #      return self._price







p=product("iphone 16",80000)

print(p.price)
p.price=90000
print(p.price)


#p.set_price(70000)
#print(p.get_prise())    => p.price, p.price=7000
# print(p.name,p.price)