customers = ["sadıkturan", "ahmetyılmaz", "cinarturan", "yigitbilgi"]
order_totals = [12000, 13000, 5000, 15000]

# 1- 'sadıkturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
customers.append("sadıkturan")
order_totals.append(5000)
sonuc= customers 
sonuc=order_totals

# 2- Son eklenen sipariş siliniz.

sonuc=customers.pop()
sonuc=order_totals.pop()

# 3- Tüm müşteriler için aşağıdaki gibi özet cümleyi yazdırınız.
# "<kullanıcıadı>" isimli müşterinin siparişi toplam <sipariştoplamı> liradır.


sonuc=f"{customers[0]} isimli müşterinin siparişi toplam {order_totals[0]} liradır."


# 4- Müşterileri alfabetik olarak sıralayınız.

customers.sort()
print(customers)


# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()


# 6- En düşük sipariş hangisidir?

sonuc=min(order_totals)
# 7- 'sadıkturan' isimli kullanıcıdan kaç tane sipariş vardır?

sonuc=customers.count("sadıkturan")

# 8- Customers listesinden 'ahmetyılmaz' isimli kullanıcıyı siliniz.

customers.remove("ahmetyılmaz")
sonuc=customers



# 9- Listelerde tüm içerikler siliniz.
customers.clear()
order_totals.clear()

print(customers, order_totals)


# 10- Kullanıcının aldığı sipariş toplamlarını listeleyiniz.

username=input("müşerti adı:")
toplam=input("toplam:")
customers.append(username)
order_totals.append(toplam)


print(username)
print(toplam)