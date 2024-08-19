import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LinearRegression, Lasso, ElasticNet, Ridge
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score



data = fetch_california_housing()


X = pd.DataFrame(data=data.data, columns=data.feature_names)
y = pd.Series(data.target)

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=11)

param_grid = {"alpha":[0.001, 0.01, 0.5, 0.1, 1, 5, 10, 100]}

alpha = 0.001
estimators = {"LinearRegression":LinearRegression(),
          "Lasso":Lasso(alpha=alpha),
          "Elasticnet":ElasticNet(alpha=alpha),
          "Ridge":Ridge(alpha=alpha)}

for estimator_name, estimator in estimators.items():
    model = estimator
    model.fit(X=X_train, y=y_train)
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    print(f"{estimator_name}")
    print("R2 Score: ",r2)
    print("___________________________")






