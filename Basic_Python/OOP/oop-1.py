#class

class Product:
    #Attribute,property
    def __init__(self,name,price,isActive):
        self.name=name
        self.price=price
        self.isActive=isActive


   #instance_Method
    def get_product(self):
        return f"urun adı :{self.name} fiyat : {self.price}"

    def kdv_price(self):
         return self.price*1.20
#ınstance,nesne,objeect
p1=Product("ıphone 15",50000,True)
p2=Product("ıphone 15 pro ",60000,False)


urunler=[p1,p2]

for urun in urunler:
     if urun.isActive:
           print(urun.get_product())
           print(urun.kdv_price())

