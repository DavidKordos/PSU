ime_datoteke = input("Ime datoteke: ")

try:
    datoteka = open(ime_datoteke)

    suma = 0
    brojac = 0

    for linija in datoteka:
        if linija.startswith("X-DSPAM-Confidence:"):
            vrijednost = float(linija.split(":")[1])
            suma += vrijednost
            brojac += 1

    if brojac > 0:
        prosjek = suma / brojac
        print("Average X-DSPAM-Confidence:", prosjek)
    else:
        print("Nema pronađenih vrijednosti.")

except:
    print("Greška: datoteka nije pronađena.")
