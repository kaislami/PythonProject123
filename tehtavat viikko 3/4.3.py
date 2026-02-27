pieninisoin=[]
while True:
    luvut=(input("Sano joku luku "))
    if luvut == "":
        break
    luku=float(luvut)
    pieninisoin.append(luku)

if len(pieninisoin) >0:
    print("Isoin sanomasi luku oli:", max(pieninisoin))
    print("Pienin sanomasi luku oli:", min(pieninisoin))
else:
    print("Kerroit liian vähän lukuja")
