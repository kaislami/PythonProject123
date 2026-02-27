luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1


while True:
    tuumat = float(input("kerro tuumasi tähän: "))
    if tuumat < 0:
        print("Ohjelma sulkeutuu")
        break
    else:
        senttimetrit = tuumat * 2.54
        print("senttimetreinä se on ", senttimetrit)


