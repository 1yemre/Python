# for item in liste:
#     if(kosul):
#          expression



#[expression for item in liste if kosul]

sayilar=[3,5,7,4,5,56,34]
sonuc=[]


for sayi in sayilar:
    if(sayi%2==0):
        sonuc.append(sayi)


sonuc=[sayi  for sayi in sayilar if sayi%2==0 ]
sonuc=[sayi if sayi%20==0  else "tek sayi " for sayi in sayilar]


urun_fiyatlari=[3000,1000,4000,0,5000]
vergiler=[]

for fiyat in urun_fiyatlari:
    if(fiyat > 0):
        vergiler.append(fiyat*1.20)






vergiler=[fiyat*1.20 for fiyat in urun_fiyatlari if fiyat>0 ]
vergiler=[fiyat *1.20  if fiyat>0  else "bu sayi hesaplanamaz!" for fiyat in urun_fiyatlari]
print(vergiler) 