import random
def heita_noppaa(TAHKOT):
    return random.randint(1, TAHKOT)
TAHKOT = int(input("Montako tahkoa: "))
while True:
    tulos = heita_noppaa(TAHKOT)
    print(tulos)
    if tulos == TAHKOT:
        break