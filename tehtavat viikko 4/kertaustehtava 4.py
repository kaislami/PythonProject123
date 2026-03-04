sanat=""
edellinen=""
while True:
    sana=input("Lisää sana tarinaan: ")
    if sana == "Loppu" or sana== "loppu" or sana ==edellinen:
        break
    sanat+=sana+" "
    edellinen= sana
print(sanat.strip())