kayttajatunnus = "python"
salasana = "rules"
for yritys in range (5):
    tunnus = input("Käyttäjätunnus: ")
    sana= input("Salasana: ")
    if tunnus == kayttajatunnus and salasana == sana :
        print("Tervettuloa")
        break
else:
    print("Pääsy evätty")

