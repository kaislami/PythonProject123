lista =[]
while True:
    luku = int(input("Uusi luku: "))
    if luku == 0:
        break
    lista.append(luku)
    print("Lista nyt ", lista)
    print("Lista järjestyksessä ", sorted(lista))
