import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ucitavanje podataka
podaci = pd.read_csv('cars_processed.csv')


# ========================
# ODGOVORI NA PITANJA
# ========================

# 1. broj automobila
print("1. Broj automobila u datasetu:")
print(len(podaci))


# 2. tipovi stupaca
print("\n2. Tipovi stupaca:")
print(podaci.dtypes)


# 3. najveca i najmanja cijena
print("\n3. Automobil s najvecom cijenom:")
najveca_cijena = podaci[podaci['selling_price'] == podaci['selling_price'].max()]
print(najveca_cijena[['name', 'selling_price']])

print("\nAutomobil s najmanjom cijenom:")
najmanja_cijena = podaci[podaci['selling_price'] == podaci['selling_price'].min()]
print(najmanja_cijena[['name', 'selling_price']])


# 4. broj automobila iz 2012
print("\n4. Broj automobila iz 2012:")
auta_2012 = podaci[podaci['year'] == 2012]
print(len(auta_2012))


# 5. najvise i najmanje kilometara
print("\n5. Automobil s najvise kilometara:")
najvise_km = podaci[podaci['km_driven'] == podaci['km_driven'].max()]
print(najvise_km[['name', 'km_driven']])

print("\nAutomobil s najmanje kilometara:")
najmanje_km = podaci[podaci['km_driven'] == podaci['km_driven'].min()]
print(najmanje_km[['name', 'km_driven']])


# 6. najcesci broj sjedala
print("\n6. Najcesci broj sjedala:")
najcesce_sjedala = podaci['seats'].mode()
print(najcesce_sjedala)


# 7. prosjecna kilometraza (diesel vs petrol)
print("\n7. Prosjecna kilometraza za diesel:")
diesel = podaci[podaci['fuel'] == 'Diesel']
print(diesel['km_driven'].mean())

print("\nProsjecna kilometraza za petrol:")
petrol = podaci[podaci['fuel'] == 'Petrol']
print(petrol['km_driven'].mean())


# ========================
# GRAFOVI
# ========================

# 1. broj automobila po gorivu
plt.figure()
sns.countplot(x='fuel', data=podaci)
plt.title("Broj automobila po tipu goriva")
plt.xlabel("Tip goriva")
plt.ylabel("Broj automobila")
plt.show()


# 2. distribucija cijene
plt.figure()
sns.histplot(podaci['selling_price'], bins=30)
plt.title("Distribucija cijene automobila")
plt.xlabel("Cijena")
plt.ylabel("Frekvencija")
plt.show()


# 3. cijena ovisno o gorivu
plt.figure()
sns.boxplot(x='fuel', y='selling_price', data=podaci)
plt.title("Cijena ovisno o tipu goriva")
plt.xlabel("Tip goriva")
plt.ylabel("Cijena")
plt.show()


# 4. kilometraza vs cijena
plt.figure()
plt.scatter(podaci['km_driven'], podaci['selling_price'])
plt.xlabel("Kilometraza")
plt.ylabel("Cijena")
plt.title("Odnos kilometraze i cijene")
plt.show()


# 5. cijena ovisno o mjenjacu
plt.figure()
sns.boxplot(x='transmission', y='selling_price', data=podaci)
plt.title("Cijena ovisno o mjenjacu")
plt.xlabel("Mjenjac")
plt.ylabel("Cijena")
plt.show()


# 6. broj sjedala
plt.figure()
sns.countplot(x='seats', data=podaci)
plt.title("Broj sjedala u automobilima")
plt.xlabel("Broj sjedala")
plt.ylabel("Broj automobila")
plt.show()
