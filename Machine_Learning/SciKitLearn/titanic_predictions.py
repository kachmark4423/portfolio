import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.svm import LinearSVC
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

label_encoder = LabelEncoder()

titanic_df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv")

titanic_df = titanic_df.dropna()
titanic_df['survived'] = label_encoder.fit_transform(titanic_df['survived'].astype(str))
titanic_df['sex'] = label_encoder.fit_transform(titanic_df['sex'].astype(str))
titanic_df = pd.get_dummies(titanic_df, columns=["passengerClass"], dtype=int)

titanic_df = titanic_df.sample(frac=1).reset_index(drop=True)
X = titanic_df.drop(columns=["survived", "rownames"], axis=1)
y = titanic_df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11, shuffle=True)


expected = y_test

 

        
models = {
    "LogisticRegression":LogisticRegression(penalty='l2', C=1.0, solver='liblinear'),
    "SGDCClassifier":SGDClassifier(),
    "LinearDiscriminationAnalysis":LinearDiscriminantAnalysis(),
    "QuadraticDiscriminantAnalysis":QuadraticDiscriminantAnalysis(),
    "LinearSVC":LinearSVC(),
    "RadiusNeighborClassifier":RadiusNeighborsClassifier(radius=2),
    "GaussianNB":GaussianNB(),
    "DecisionTreeClassifier":DecisionTreeClassifier()
    }

for modelName, modelObject in models.items():
    modelObject.fit(X_train, y_train)
    predicted = modelObject.predict(X_test)
    
    acc = accuracy_score(expected, predicted)
    prec = precision_score(expected,predicted)
    rec = recall_score(expected,predicted)
    
    print(modelName, ":")
    
    print("Accuracy: ", acc)
    print("Precision: ", prec)
    print("Recall: ", rec)  
    print("_________________________________________________________")
    print('')
    




