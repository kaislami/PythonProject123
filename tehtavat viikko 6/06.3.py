def gal_lit(gal):
    return gal*3.785
while True:
    maara= float(input("Bensa galloonina: "))
    if maara < 0:
        break
    litrat= gal_lit(maara)
    print("Se on litroina", litrat)