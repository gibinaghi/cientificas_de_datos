import joblib
from sklearn.feature_extraction.text import CountVectorizer

def test_evaluation():
    NB_spam_model = open('/home/florencia/Documentos/cientificas_de_datos/model/spam_clf_v1.pkl', 'rb')
    clf = joblib.load(NB_spam_model)
    sample = "Free money! Claim now!"
    expected_prediction = 1  # Assuming 'spam' is represented as 1 in the label
    cv = CountVectorizer()
    data = cv.fit_transform([sample]).toarray()
    prediction = clf.predict(data)
    assert prediction == expected_prediction, f"Error: Expected {expected_prediction}, but got {prediction}"

test_evaluation()
