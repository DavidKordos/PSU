import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('tiger.jpg')
h, w = img.shape

# a
img_a = np.clip(img.astype(float) + 50, 0, 255).astype(np.uint8)

# b
img_b = np.rot90(img, k=-1)

# c
img_c = np.fliplr(img)

# d
img_d = img[::10, ::10]

# e
img_e = np.zeros_like(img)
img_e[:, w//4 : w//2] = img[:, w//4 : w//2]

# Prikaz rezultata
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0,0].imshow(img, cmap='gray'); axes[0,0].set_title('Original')
axes[0,1].imshow(img_a, cmap='gray'); axes[0,1].set_title('a) Brightness')
axes[0,2].imshow(img_b, cmap='gray'); axes[0,2].set_title('b) Rotacija')
axes[1,0].imshow(img_c, cmap='gray'); axes[1,0].set_title('c) Zrcaljenje')
axes[1,1].imshow(img_d, cmap='gray'); axes[1,1].set_title('d) Rezolucija')
axes[1,2].imshow(img_e, cmap='gray'); axes[1,2].set_title('e) 2. četvrtina')
plt.show()
