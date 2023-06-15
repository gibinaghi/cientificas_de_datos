import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def pre_train():
    data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
    data = data[["class", "message"]]
    x = np.array(data["message"])
    y = np.array(data["class"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    return cv, clf

# Ejemplo de uso
cv, clf = pre_train()
