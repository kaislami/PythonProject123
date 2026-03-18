luku = int(input("Anna kokonaisluku: "))
if luku < 2:
    print("Ei ole alkuluku")
else:
    jakaja = 0
    for i in range(1, luku +1):
        if luku % i == 0:
            jakaja +=1
    if jakaja == 2:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")
