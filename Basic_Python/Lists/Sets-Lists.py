# Setes
    # indexlenmez
    # sırlanmaz
    # güncellenemez 
    # elemanlar tekrarlanmaz
    # elmanlar siler yada ekleriz.
fruit = {"elma","armut","kiraz"}
fruit2 = {"elma","armut","kiraz","kavun"}

result="elma" in fruit

print(result)
fruit.add("karpuz")

fruit.update(fruit2)

fruit2.remove("elma")


fruit.pop()


   