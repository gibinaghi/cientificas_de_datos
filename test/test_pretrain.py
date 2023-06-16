import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def test_pre_train():
    df = pd.read_csv("../data/spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df['label'] = df['class'].map({'ham': 0, 'spam': 1})
    X = df['message']
    y = df['label']
    cv = CountVectorizer()
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    assert X_train is not None, "Error: X_train is None"
    assert X_test is not None, "Error: X_test is None"
    assert y_train is not None, "Error: y_train is None"
    assert y_test is not None, "Error: y_test is None"
    print ("listo")

test_pre_train()