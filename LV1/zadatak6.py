
ham_rijeci = 0
ham_broj = 0
spam_rijeci = 0
spam_broj = 0
spam_usklicnik = 0

datoteka = open("SMSSpamCollection.txt", "r", encoding="utf-8")

for linija in datoteka:
    dijelovi = linija.split()
    tip = dijelovi[0]          
    poruka = dijelovi[1:]   
    broj_rijeci = len(poruka)
    if tip == "ham":
        ham_broj += 1
        ham_rijeci += broj_rijeci
    if tip == "spam":
        spam_broj += 1
        spam_rijeci += broj_rijeci
        if poruka[-1].endswith("!"):
            spam_usklicnik += 1
datoteka.close()
prosjek_ham=ham_rijeci/ham_broj
prosjek_spam=spam_rijeci/spam_broj
print("Prosječan broj riječi u HAM porukama:", prosjek_ham)
print("Prosječan broj riječi u SPAM porukama:", prosjek_spam)
print("Broj SPAM poruka koje završavaju uskličnikom:", spam_usklicnik)


