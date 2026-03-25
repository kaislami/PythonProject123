def lasku(lista):
    summa =0
    for luku in lista:
        summa = summa + luku
    return summa
numerot=[60,7]
print("Summa on ", lasku(numerot))