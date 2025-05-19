class CarItem:
    discount_rate=0.8
    item_count=0

    @classmethod
    def display_item_count(cls):
     return f"{cls.item_count} tane ürün oluşturuldu."

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CarItem.item_count+=1


    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * CarItem.discount_rate



print(CarItem.display_item_count())
item1 = CarItem("telefon", 50000, 2)
item2 = CarItem("Bilgisayar", 70000, 1)
item3 = CarItem("Kitap", 200, 2)

print(CarItem.display_item_count())
