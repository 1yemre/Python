# BankaHesabı isminde bir sınıf tanımlayınız.

# Üretilen her bir nesne "hesapSahibi" isminde bir özelliğe sahip olmalıdır.
# BankaHesabı("Ad Soyad")
# Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
# Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiyeye ekleyin ve bakiye miktarını geriye döndürün.
# Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiyeden çıkarıp geriye döndürün.


# hesap = BankaHesabı("adsoyad")
# hesap.hesapSahibi => adsoyad
# hesap.bakiye => 0.0
# hesap.paraYatir(1000) => 1000.0
# hesap.paraCek(500) => 500.0


class BankaHesabi:
    def __init__(self,hesapSahibi):
        self.hesapSahibi=0.0
        self.bakiye=0.0

    def paraYatir(self,miktar):
        self.bakiye+=miktar
        return self.bakiye
    
    def paracek(self,miktar):
        self.bakiye-=miktar
        return self.bakiye
    
    def get_bakiye(self):
        return self.bakiye
          
hesap=BankaHesabi("Emre Yenen")
print(hesap.paraYatir(1000))
print(hesap.get_bakiye())
print(hesap.paracek(500))
print(hesap.get_bakiye())