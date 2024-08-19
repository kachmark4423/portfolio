from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from tensorflow.keras.utils import to_categorical
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()


X_train = X_train.reshape((60000,28,28,1))
X_test = X_test.reshape((10000,28,28,1))


X_train = X_train.astype("float32")/255
X_test = X_test.astype("float32")/255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

cnn = Sequential()

cnn.add(Conv2D(filters=64,kernel_size=(3,3),activation="relu",input_shape=(28,28,1)))
cnn.add(MaxPool2D((2,2)))
cnn.add(Conv2D(filters=128, kernel_size=(3,3),activation="relu"))
cnn.add(MaxPool2D((2,2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation="relu"))
cnn.add(Dense(units=10, activation="softmax"))

print(cnn.summary())

cnn.compile(optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"])

cnn.fit(X_train,y_train,epochs=5,batch_size=64,validation_split=0.1)

loss, accuracy = cnn.evaluate(X_test, y_test)
predictions = cnn.predict(X_test)

images = X_test.reshape((10000,28,28))
incorrect_predictions = []

for i, (e, p) in enumerate(zip(y_test, predictions)):
    expected, predicted = np.argmax(e), np.argmax(p)

    if expected != predicted:
        incorrect_predictions.append((i, images[i], predicted, expected))

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(16,12))

for axes, item in zip(axes.ravel(), incorrect_predictions):
    index, image, predicted, expected = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(f"Index: {index}\np: {predicted}\ne: {expected}")

plt.tight_layout()

plt.show()

