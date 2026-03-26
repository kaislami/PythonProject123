def summa(a, b):
    return a + b
def erotus(a, b):
    return a - b
def tulo(a, b):
    return a * b
def jako(a, b):
    if b == 0:
        return "Ei voi jakaa nollalla"
    return a / b
luku1 = float(input("Anna ensimmäinen luku: "))
operaatio = input("Valitse (+, -, *, /): ")
luku2 = float(input("Anna toinen luku: "))
if operaatio == "+":
    print("Tulos:", summa(luku1, luku2))
elif operaatio == "-":
    print("Tulos:", erotus(luku1, luku2))
elif operaatio == "*":
    print("Tulos:", tulo(luku1, luku2))
elif operaatio == "/":
    print("Tulos:", jako(luku1, luku2))
else:
    print("Virheellinen valinta")