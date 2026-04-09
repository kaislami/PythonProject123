lentoasemat = {}
while True:
    akti = input("Haluatko lisätä hakea vai lopettaa: ")
    if akti == "lisätä" or akti == "Lisätä":
        ICAO = input("Anna icao koodisi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[ICAO] = nimi
    elif akti == "hakea" or akti == "Hakea":
        icao = input("Anna icao koodisi: ").upper()
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy")
    elif akti == "Lopeta" or "lopeta":
        break
    else:
        print("Virheellinen valinta")