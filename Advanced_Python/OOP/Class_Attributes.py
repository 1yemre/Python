class CarItem:
    # constructor => yapıcı method 
    discount_rate=0.8
    item_count=0

    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
        CarItem.item_count+=1

    # instance Methods 
    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * CarItem.discount_rate


# instance = nesne
item1 = CarItem("telefon", 50000, 2)
item2 = CarItem("Bilgisayar", 70000, 1)
item3 = CarItem("Kitap", 200, 2)


#print(CarItem.discount_rate)

print(item1.__dict__)
print(item2.__dict__)
print(item3.__dict__)
print(CarItem.__dict__)


print(CarItem.item_count)


item1.apply_discount()
print(item1.calculate_total())


item2.apply_discount()
print(item2.calculate_total())


item3.apply_discount() 
print(item3.calculate_total())







