import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import cluster

# 1. Učitavanje slike
try:
    imageNew = mpimg.imread('example_grayscale.png')
except FileNotFoundError:
    print("Slika nije pronađena! Provjeri je li u istom folderu kao i skripta.")
    
    from scipy import misc
    imageNew = misc.face(gray=True)

# Provjera formata (neki formati su 0-255, neki 0-1)
if imageNew.max() <= 1.0:
    imageNew = (imageNew * 255).astype(np.uint8)

# 2. Priprema podataka (X mora biti (n_samples, n_features))
X = imageNew.reshape((-1, 1))

# 3. K-means kvantizacija
n_clusters = 10
k_means = cluster.KMeans(n_clusters=n_clusters, n_init='auto')
k_means.fit(X)

values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

# Kreiranje komprimirane slike
image_compressed = np.choose(labels, values.astype(np.uint8))
image_compressed.shape = imageNew.shape

# 4. Prikaz
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imageNew, cmap='gray')
plt.title('Originalna slika')

plt.subplot(1, 2, 2)
plt.imshow(image_compressed, cmap='gray')
plt.title(f'Kvantizirana slika (K={n_clusters})')
plt.show()