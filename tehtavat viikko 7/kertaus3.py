sanat = ["Olipa", "kerran", "pieni", "insinööri", "opiskelija", "jolla", "oli","vaikeuksia", "koodauksessa"]
laskuri =0
for sana in sanat:
    if len(sana) >5:
        laskuri +=1
print("Yli 5 kirjainta sisältävät sanat listassani: ", laskuri)