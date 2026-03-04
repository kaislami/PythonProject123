palkka = float(input("Kertoisitko minulle tuntipalkkasi: "))
tunnit = float(input("Paljonko teit tunteja eilen: " ))
paiva = input("Mikä viikonpäivä oli eilen: ")
muupalkka = palkka*tunnit
supalkka = 2*palkka*tunnit
if paiva == "sunnuntai" or paiva == "Sunnuntai":
    print("Tienasit eilen ", supalkka, "euroa")
else:
    print("Tienasit eilen ", muupalkka, "euroa")
