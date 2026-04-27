import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np

# Ponovljena funkcija za generiranje
def generate_data(n_samples, flagc):
    if flagc == 1:
        random_state = 365
        X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
    elif flagc == 2:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples, centers=4, cluster_std=[1.0, 2.5, 0.5, 3.0], random_state=random_state)
    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    else:
        X = []
    return X

# 1. Generiranje podataka
X = generate_data(500, 1)

# 2. Izračun kriterijske funkcije za k od 1 do 20
vrijednosti_kriterija = []
broj_klastera = range(1, 21)

for k in broj_klastera:
    km = KMeans(n_clusters=k, n_init='auto', random_state=42)
    km.fit(X)
    vrijednosti_kriterija.append(km.inertia_) # inertia_ je kriterijska funkcija, što je manja točke su bliže centru

# 3. Prikaz grafa
plt.figure(figsize=(10, 6))
plt.plot(broj_klastera, vrijednosti_kriterija, 'o-')
plt.title('Metoda lakta (Elbow Method)')
plt.xlabel('Broj klastera (k)')
plt.ylabel('Vrijednost kriterijske funkcije (Inertia)')
plt.xticks(broj_klastera)
plt.grid(True)
plt.show()