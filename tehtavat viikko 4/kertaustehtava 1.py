nimi =  input("Hei! Kerro nimesi: ")
if nimi == "Matti":
    print("Keittokauppamme syrjii Matteja, mene muualle!")
else:
    keittomaara = float(input("Kuinka monta keittoa haluaisit: "))
    hinta = keittomaara*5.90
    print("Okei se maksaisi ", hinta, "euroa, kiitos!")

