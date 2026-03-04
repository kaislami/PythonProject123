import math
while True:
    luku = float(input("Kerro minulle kokonaisluku: "))
    if luku <0 :
        print("Virheellinen numero")
    elif luku >0 :
        posi = math.sqrt(luku)
        print("Neljöjuuri luvustasi: ", posi)
    else:
        break
