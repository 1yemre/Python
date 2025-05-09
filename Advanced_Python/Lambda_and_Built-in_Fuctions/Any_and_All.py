#Any all

sonuc=all([True,True,False])
sonuc=all([True,True,True])
sonuc=any([True,True,True])
sonuc=any([True,False,True])
sonuc=any([True,False,False])
sonuc=any([False,False,False])


# And=> True and True => all()
# or => True or False => any()

# print(sonuc)


sayilar=[1,3,5,7,6,5,52,0]
sonuc=all([bool(sayi)for sayi in sayilar])
sonuc=any([bool(sayi)for sayi in sayilar])

print(sonuc)