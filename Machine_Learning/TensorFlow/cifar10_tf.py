from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D
from tensorflow.keras.utils import to_categorical
import numpy as np

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

X_train = X_train.astype("float32")/255
X_test = X_test.astype("float32")/255

y_test = to_categorical(y_test)
y_train = to_categorical(y_train)

cnn = Sequential()

cnn.add(Conv2D(filters=64, kernel_size=(3,3), activation="relu", input_shape=(32,32,3)))
cnn.add(MaxPool2D(pool_size=(2,2)))
cnn.add(Conv2D(filters=128, kernel_size=(3,3), activation="relu"))
cnn.add(MaxPool2D(pool_size=(2,2)))
cnn.add(Flatten())
cnn.add(Dense(units=4096, activation="relu"))
cnn.add(Dense(units=128, activation="relu"))
cnn.add(Dense(units=10, activation="softmax"))

print(cnn.summary())
cnn.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

cnn.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.1)
loss, accuracy = cnn.evaluate(X_test, y_test)
print("Accuracty: ", accuracy)
predictions = cnn.predict(X_test)


incorrect_predictions = []


for (p,e) in zip(predictions, y_test):
    predicted, expected = np.argmax(p), np.argmax(e)
    if predicted != expected:
        incorrect_predictions.append((p, e))

print(len(incorrect_predictions))