import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LinearRegression, Lasso, ElasticNet, Ridge
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.datasets import fetch_california_housing, load_wine
from sklearn.metrics import r2_score



data = load_wine()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, shuffle=True)

models = {
    "KNN":KNeighborsClassifier(),
    "GaussianNB":GaussianNB(),
    "SVC":SVC(),
    "SGDClassifier":SGDClassifier(),
    "RNN":RadiusNeighborsClassifier(radius=70),
    "DecisionTree":DecisionTreeClassifier()
}

for model_name, model_object in models.items():
    try:
        model_object.fit(X_train, y_train)
        predicted = model_object.predict(X_test)

        acc = accuracy_score(y_test, predicted)

        print(model_name)
        print("Accuracy: ", acc)
        print("________________________________________________\n")
    except Exception as e:
        print(f"Model {model_name} failed due to {e}")







