from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping


df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv")
df = df.drop(columns = ["rownames"])
df = df.dropna()

X = df.drop(columns=["survived"])
y = df["survived"]
X = pd.get_dummies(X, columns=["sex",  "passengerClass"], drop_first=True)
y = y.map({"yes":1, "no":0})


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, test_size=0.2)

print(X_train.shape, X_test.shape)

model = Sequential()

model.add(Dense(units=4, activation="relu"))
model.add(Dense(units=2, activation="relu"))

model.add(Dense(units=1, activation="sigmoid"))

early_stop = EarlyStopping(monitor="loss", mode="min")

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=58)

print(pd.DataFrame(model.history.history))
print(pd.DataFrame(model.history.history).plot())

predictions = model.predict(X_test)
preds = np.round(predictions)

print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds))