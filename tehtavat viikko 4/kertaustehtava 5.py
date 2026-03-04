while True:
    muoto = input("Valitse yksi: jakolasku, kertolasku, summa, vähennyslasku tai lopetus: ")
    if muoto == "lopeta" or muoto == "Lopeta" or muoto== "Lopetus" or muoto == "lopetus":
        break
    numero1 = float(input("Anna ensimmäinen numero: "))
    numero2 = float(input("Toinen numero:"))
    if muoto == "jakolasku":
        if numero2 ==0:
            print("Een voi jakaa nollalla.")
        else:
            print(numero1/numero2)
    elif muoto == "kertolasku":
        print(numero1*numero2)
    elif muoto == "summa":
        print(numero1+numero2)
    elif muoto == "vähennyslasku":
        print(numero1-numero2)
    else:
        print("Antamasi laskumuoto oli väärin yritä uudestaan.")