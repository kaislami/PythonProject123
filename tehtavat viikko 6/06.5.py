def karsimusmaximus(lista):
    uusilista = []
    for luku in lista:
        if luku % 2 == 0:
            uusilista.append(luku)
    return uusilista
numerot=[67,67,333,420,20051003,5008]
karsitut= karsimusmaximus(numerot)
print(karsitut, "on parilliset ja ")
print(numerot, "oli sun alkuperäset")