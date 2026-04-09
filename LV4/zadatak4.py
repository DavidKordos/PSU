import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ucitavanje podataka
df = pd.read_csv('cars_processed.csv')


# ========================
# ODGOVORI NA PITANJA
# ========================

# 1. broj automobila
print("1. Broj automobila:")
print(len(df))


# 2. tipovi stupaca
print("\n2. Tipovi stupaca:")
print(df.dtypes)


# 3. max i min cijena
print("\n3. Najveca cijena:")
print(df[df['selling_price'] == df['selling_price'].max()][['name','selling_price']])

print("\nNajmanja cijena:")
print(df[df['selling_price'] == df['selling_price'].min()][['name','selling_price']])


# 4. broj auta iz 2012
print("\n4. Broj auta iz 2012:")
print(len(df[df['year'] == 2012]))


# 5. najvise i najmanje km
print("\n5. Najvise km:")
print(df[df['km_driven'] == df['km_driven'].max()][['name','km_driven']])

print("\nNajmanje km:")
print(df[df['km_driven'] == df['km_driven'].min()][['name','km_driven']])


# 6. najcesci broj sjedala
print("\n6. Najcesci broj sjedala:")
print(df['seats'].mode())


# 7. prosjecni km diesel vs petrol
print("\n7. Prosjecni km (diesel):")
print(df[df['fuel'] == 'Diesel']['km_driven'].mean())

print("\nProsjecni km (petrol):")
print(df[df['fuel'] == 'Petrol']['km_driven'].mean())


# ========================
# GRAFOVI
# ========================

# 1. broj auta po gorivu
plt.figure()
sns.countplot(x='fuel', data=df)
plt.title("Broj auta po tipu goriva")
plt.show()


# 2. distribucija cijene
plt.figure()
sns.histplot(df['selling_price'], bins=30)
plt.title("Distribucija cijene")
plt.show()


# 3. cijena po gorivu
plt.figure()
sns.boxplot(x='fuel', y='selling_price', data=df)
plt.title("Cijena po tipu goriva")
plt.show()


# 4. km vs cijena
plt.figure()
plt.scatter(df['km_driven'], df['selling_price'])
plt.xlabel("km")
plt.ylabel("cijena")
plt.title("Kilometraza vs cijena")
plt.show()


# 5. cijena po mjenjacu
plt.figure()
sns.boxplot(x='transmission', y='selling_price', data=df)
plt.title("Cijena po mjenjacu")
plt.show()


# 6. broj sjedala
plt.figure()
sns.countplot(x='seats', data=df)
plt.title("Broj sjedala")
plt.show()
