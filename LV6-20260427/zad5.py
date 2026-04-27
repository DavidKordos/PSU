import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

# 1. Učitavanje slike u boji
try:
    img = mpimg.imread('example.png')
except FileNotFoundError:
    print("Greška: Datoteka 'example.png' nije pronađena!")
    
    exit()

# Neki formati učitavaju sliku kao float (0-1), a neki kao int (0-255)

if img.max() > 1.0:
    img = img / 255.0

# 2. Transformacija slike u niz piksela
# Slika je (visina, širina, 3), pretvaramo u (broj_piksela, 3)
w, h, d = img.shape
X = img.reshape((w * h, d))

# 3. Primjena K-means algoritma
# n_clusters definira koliko će unikatnih boja slika imati na kraju
n_colors = 8 
kmeans = KMeans(n_clusters=n_colors, n_init='auto', random_state=42)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# 4. Rekonstrukcija kvantizirane slike
quantized_img = centers[labels].reshape((w, h, d))

# 5. Prikaz rezultata
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Originalna slika')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(quantized_img)
plt.title(f'Kvantizirana slika ({n_colors} boja)')
plt.axis('off')

plt.tight_layout()
plt.show()