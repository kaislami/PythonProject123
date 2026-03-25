import math
def yksikkohinta(halksent, hinta):
    sademet=(halksent/2)/100
    ala=math.pi*sademet**2
    return hinta/ala
pizhalk1 = float(input("Kuinka iso ekan pitsasi halkaisia on? "))
pizhalk2 = float(input("Kuinka iso tokan pitsasi halkaisia on? "))
pizhint1 = float(input("Kuinka kallis eka pitsasi on? "))
pizhint2 = float(input("Kuinka kallis toka pitsasi on? "))
ykshin1 = yksikkohinta(pizhalk1, pizhint1)
ykshin2 = yksikkohinta(pizhalk2, pizhint2)
print("Pizza 1 yksikköhinta:", ykshin1, "€/m²")
print("Pizza 2 yksikköhinta:", ykshin2, "€/m²")
if ykshin1 < ykshin2:
    print("Pizza 1 on parempi vastine rahalle")
elif ykshin1 > ykshin2:
    print("Pizza 2 on parempi vastine rahalle")
else:
    print("Molemmat ovat yhtä hyviä")