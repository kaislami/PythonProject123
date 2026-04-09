vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausinumero = int(input("Anna kuukauden numero: "))
if kuukausinumero <= 2 or kuukausinumero ==12:
    print("Vuodenaika on ", vuodenajat[0])
elif kuukausinumero <= 5:
    print("Vuodenaika on ", vuodenajat[1])
elif kuukausinumero <= 8:
    print("Vuodenaika on ", vuodenajat[2])
elif kuukausinumero <= 11:
    print("Vuodenaika on ", vuodenajat[3])
else:
    print("Vuodenaika on virheellinen")
