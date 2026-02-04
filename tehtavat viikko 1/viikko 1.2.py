import math

name = (input("mikä sinun nimesi on: "))
print(f"Hauska tavata {name}!")


import math

number1 = float(input("mikä on sinun ympyran sade:"))
number2 =  math.pi * (number1 ** 2)
print(f"ympyran pinta-ala on silloin:", number2)


number3 = float(input("kuinka korkea on sinun suorakulmio: "))
number4 = float(input("Okei kiitos tiedosta, kerro vielä sen leveys tähän: "))
print(f"kiitos tiedosta")
number5 = 2 * number3 + 2* number4
print("tiesitkö että suorakulmiosi piiri on", number5)
number6 = number3 * number4
print("Suorakulmiosi pinta-ala puolestaan on", number6)


print("kertoisitko minulle kolme kokonaislukua?")
number7 = int(input("numero:" ))
number8 = int(input("numero:" ))
number9 = int(input("numero:" ))
number10 = number7 * number8 * number9
number11 = number7 + number8 + number9
number12 = (number7 + number8 + number9) / 3
print("antamiesi numeroiden tulo on", number10, "summa on", number11, "ja keskiarvo", number12)


print("huomasin että sinulla oli vanhanaikaisissa mitoissa aarteita, voin muuttaa ne sinulle!")
leviskat = float(input("kuinka monta leiviskaa?" ))
naulat = float(input("kuinka monta naulaa?" ))
luodit = float(input("kuinka monta luotia?" ))
number13 = leviskat *20 *30 + naulat *32 + luodit
grammat = number13 *13.5
kilot = int(grammat // 1000)
loput = grammat % 1000
print("sinun aarteesi ovat yhteensä", kilot, "kiloa ja", loput, "grammaa")



print("jos haluat uusia supersalaisia pinkoodeja tässä kaksi vaihtoehtoa:")
import random
code1 = ""
for i in range(3):
    code1 += str(random.randint(0,9))
print("kolmenumeroinen koodi", code1)
code2 = ""
for i in range(4):
     code2 += str(random.randint(1, 6))
print("nelinumeroinen koodi", code2)

