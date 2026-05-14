import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'mojbroj1.png'

# Ucitaj sliku
img_original = mpimg.imread('mojbroj1.png')  # Zamijeni 'test.png' s putanjom do svoje slike
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))



# Prikazi sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()

# Pripremi sliku - ulaz u mrezu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# TODO: ucitaj izgradenu mrezu
model = models.load_model('best_model.keras')



# TODO: napravi predikciju za ucitanu sliku pomocu mreze
predictions = model.predict(img)
predicted_class = np.argmax(predictions)



# TODO: ispis rezultat u terminal
print(f"\nPredvidjena znamenka je: {predicted_class}")
print(f"Pouzdanost: {np.max(predictions)*100:.2f}%")


