kuha = float(input("Kuinka pitkä kalastamasi kuha on? "))
if kuha > 37:
    print("Onnea! Saat pitää kuhasi!")
if kuha < 37:
    print("Kuhasi on liian pieni, päästä se takaisin järveen")
    puuttuu = 37 - kuha
    print("Kuhasi pitää kasvaa vielä ", puuttuu, "senttiä")



hytti = input("Onko hyttisi LUX, A, B vai C? ")
if hytti == "LUX":
    print("Hyttisi on yläkannella ja siinä on parveke")
elif hytti == "A":
    print("Hytissäsi on ikkuna ja se on autokannen yläpuolen")
elif hytti == "B":
    print("Hyttisi on ikkunaton ja se on autokannen yläpuolella")
elif hytti == "C":
    print("Hyttisi on ikkunaton ja se on autokannen alapuolen")
else :
    print("Virheellinen hyttiluokka, tarkista isot kirjaimet.")


print("Nyt kerron sinulle hemoglobiiniarvosi laadun, ")
sukupuoli = input("oletko nainen vai mies, vastaa N/M? ")
if sukupuoli == "N":
    nHemo = float(input("Mikä on sinun hemoglobiiniarvo? "))
    if nHemo <=117 :
        print("Hemoglobiinisi on alhainen")
    elif nHemo >=175 :
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on viitearvoissa")
elif sukupuoli == "M":
    mHemo = float(input("Mikä on sinun hemoglobiiniarvo? "))
    if mHemo <=134 :
        print("Hemoglobiinisi on alhainen")
    elif mHemo >=195 :
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on viitearvoissa")

vuosi = int(input("Kerro minulle joku vuosiluku "))
if (vuosi % 4 == 0 and vuosi % 100 !=0) or vuosi % 400 == 0:
    print("Vuosi ", vuosi, " on karkausvuosi")
else:
    print("Vuosi ", vuosi, " ei ole karkausvuosi")