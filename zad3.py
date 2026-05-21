import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

img_path = 'znak.png'

model = tf.keras.models.load_model('best_model.h5')

img = image.load_img(img_path, target_size=(48, 48))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions[0])
confidence = predictions[0][predicted_class_index]

print(predicted_class_index)
print(confidence)