class CarItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    @classmethod
    def creat_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return CarItem(name, float(price), int(quantity))

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        CarItem.item_count += 1

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * CarItem.discount_rate


class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount


C1 = Coupon("code1", 0.8)
C2 = Coupon("code2", 0.7)
C3 = Coupon("code3", 0.9)

item1 = CarItem("telefon", 50000, 2)
item2 = CarItem("Bilgisayar", 70000, 1)
item3 = CarItem("Kitap", 200, 2)


class ShoppingCart:
    coupon_list = [C1, C2, C3]

    def __init__(self, liste):
        self.liste = liste

    def add_item(self, item):
        self.liste.append(item)

    def display_item(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")

    def calculate_totals(self):
        return sum(item.calculate_total() for item in self.liste)

    def remove_item(self, Cart_item):
        self.liste = [item for item in self.liste if item != Cart_item]

    def clear(self):
        self.liste = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]

    @classmethod
    def get_coupon(cls, code):
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))

    def apply_coupon(self, code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"geçersiz kupon kodu ! : {code}")
        coupon = ShoppingCart.get_coupon(code)

        for index in range(0, len(self.liste)):
            self.liste[index].price = self.liste[index].price * coupon.discount


# Kullanım
sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_item()


# print(sc.calculate_totals())
# sc.remove_item(item1)
# sc.display_item()
# sc.clear()
# sc.display_item()

sc.apply_coupon("code2")
print(sc.calculate_totals())
