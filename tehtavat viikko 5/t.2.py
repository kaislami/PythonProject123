luvut=[]
while True:
    syote = input("Anna joku luku: ")
    if syote == "" :
        break
    luku = float(syote)
    luvut.append(luku)
luvut.sort(reverse=True)
isoimmat = luvut[:5]
print("Viisi isointa lukua oli: ", isoimmat)

