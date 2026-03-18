import random
lukumaara = int(input("Kuinka monta noppaa haluat heittää: "))
summa=0
for i in range(lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto
print("Silmälukujesi summa on: ", summa)