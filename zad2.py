import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import datetime

img_size = (48, 48)
batch_size = 32

train_ds = image_dataset_from_directory(
    'dataset/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=batch_size,
    image_size=img_size,
    validation_split=0.2,
    subset='training',
    seed=123
)

validation_ds = image_dataset_from_directory(
    'dataset/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=batch_size,
    image_size=img_size,
    validation_split=0.2,
    subset='validation',
    seed=123
)

test_ds = image_dataset_from_directory(
    'dataset/Test',
    labels='inferred',
    label_mode='categorical',
    batch_size=batch_size,
    image_size=img_size
)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
validation_ds = validation_ds.prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

model = models.Sequential()
model.add(layers.Rescaling(1.0 / 255, input_shape=(48, 48, 3)))

for filters in [32, 64, 128]:
    model.add(layers.Conv2D(filters, (3, 3), padding='same', activation='relu'))
    model.add(layers.Conv2D(filters, (3, 3), padding='valid', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(layers.Dropout(0.2))

model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(43, activation='softmax'))

model.summary()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath='best_model.h5',
    monitor='val_accuracy',
    mode='max',
    save_best_only=True,
    verbose=1
)

history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=20,
    callbacks=[checkpoint_callback, tensorboard_callback]
)

best_model = models.load_model('best_model.h5')

test_loss, test_acc = best_model.evaluate(test_ds)
print(f"Tocnost: {test_acc * 100:.2f}%")

y_true = []
y_pred = []

for images, labels in test_ds:
    preds = best_model.predict(images, verbose=0)
    y_true.extend(np.argmax(labels.numpy(), axis=1))
    y_pred.extend(np.argmax(preds, axis=1))

cm = confusion_matrix(y_true, y_pred)
print(cm)
print(classification_report(y_true, y_pred))