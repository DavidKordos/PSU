import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np

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

# 1. Generiranje podataka (npr. flagc=1)
n_samples = 500
flagc = 1 
X = generate_data(n_samples, flagc)

# 2. Inicijalizacija i učenje K-means modela
# Pretpostavljamo 3 klastera
kmeans = KMeans(n_clusters=4, n_init='auto')
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# 3. Prikaz rezultata
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, alpha=0.7)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centri')
plt.title(f'K-means grupiranje (flagc={flagc})')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()