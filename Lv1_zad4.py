naziv = input("Unesi ime datoteke: ")
file = open(naziv)

ukupno = 0.0
count = 0

for red in file:
    if "X-DSPAM-Confidence:" in red:
        dijelovi = red.strip().split(":")
        broj = float(dijelovi[1])
        ukupno += broj
        count += 1

if count > 0:
    prosjek = ukupno / count
    print("Prosječna vrijednost:", prosjek)
else:
    print("Nema podataka za izračun.")
