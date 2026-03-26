def suurin_arvo(a, b, c):
    return max(a, b, c)
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
suurin = suurin_arvo(luku1, luku2, luku3)
print("Suurin luku on:", suurin)