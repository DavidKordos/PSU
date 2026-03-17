rjecnik = {}
datoteka = open("song.txt", "r")
for linija in datoteka:
    rijeci = linija.split()
    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] = rjecnik[rijec] + 1
        else:
            rjecnik[rijec] = 1
datoteka.close()
broj = 0
for rijec in rjecnik:
    if rjecnik[rijec] == 1:
        print(rijec)
        broj = broj + 1
print("Broj riječi koje se pojavljuju samo jednom:", broj)
