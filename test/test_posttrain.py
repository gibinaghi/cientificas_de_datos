import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def post_train(cv, clf):
    sample = "Free money! Claim now!"
    expected_prediction = "spam"
    data = cv.transform([sample]).toarray()
    prediction = clf.predict(data)
    assert prediction == expected_prediction, f"Error: Expected {expected_prediction}, but got {prediction}"
    print("Prediction:", prediction)

