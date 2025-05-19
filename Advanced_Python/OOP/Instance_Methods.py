class CarItem:
    # constructor => yapıcı method 
    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity

    # instance Methods 
    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self, rate):
        self.price = self.price * rate


# instance = nesne
item1 = CarItem("telefon", 50000, 2)
item2 = CarItem("Bilgisayar", 70000, 1)
item3 = CarItem("Kitap", 200, 2)




# print("ürün indirimsiz fiyatı : " + str(item1.calculate_total()))
# item1.apply_discount()
# print("ürün İndirimli fiyatı : " + str(item1.calculate_total()))

# print("ürün indirimsiz fiyatı : " + str(item2.calculate_total()))
# item2.apply_discount()
# print("ürün İndirimli fiyatı : " + str(item2.calculate_total()))

# print("ürün indirimsiz fiyatı : " + str(item3.calculate_total()))
# item3.apply_discount()
# print("ürün İndirimli fiyatı : " + str(item3.calculate_total()))




item1.apply_discount(0.8)# %20 
print(item1.calculate_total())



item2.apply_discount(0.7)# %30 
print(item2.calculate_total())



item3.apply_discount(0.9) # %10 
print(item3.calculate_total())







