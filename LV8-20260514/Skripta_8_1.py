from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay # Dodano ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)



# TODO: strukturiraj konvolucijsku neuronsku mrezu
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax"),
])



# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])



# TODO: definiraj callbacks
my_callbacks = [
    # Tensorboard callback
    callbacks.TensorBoard(log_dir='./logs', histogram_freq=1),
    # ModelCheckpoint za pohranjivanje najboljeg modela
    callbacks.ModelCheckpoint(filepath='best_model.keras', 
                             monitor='val_accuracy', 
                             save_best_only=True, 
                             mode='max')
]


# TODO: provedi treniranje mreze pomocu .fit()
model.fit(x_train_s, y_train_s, 
          batch_size=128, 
          epochs=10, 
          validation_split=0.1, 
          callbacks=my_callbacks)


#TODO: Ucitaj najbolji model
best_model = models.load_model('best_model.keras')


# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
y_train_pred = np.argmax(best_model.predict(x_train_s), axis=1)
y_test_pred = np.argmax(best_model.predict(x_test_s), axis=1)

train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

print(f"\nTocnost na skupu za ucenje: {train_acc*100:.2f}%")
print(f"Tocnost na skupu za testiranje: {test_acc*100:.2f}%")


# TODO: Prikazite matricu zabune na skupu podataka za testiranje
cm = confusion_matrix(y_test, y_test_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.arange(10))

fig, ax = plt.subplots(figsize=(10, 10))
disp.plot(cmap=plt.cm.Blues, ax=ax)
plt.title("Matrica zabune - Testni skup")
plt.show()
