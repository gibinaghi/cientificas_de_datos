from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


def detect_spam(message):
    # Cargar el modelo entrenado
    NB_spam_model = open('/home/florencia/Documentos/cientificas_de_datos/model/spam_clf_v1.pkl', 'rb')
    clf = joblib.load(NB_spam_model)

    # Cargar el vectorizador
    cv = CountVectorizer(vocabulary=joblib.load("/home/florencia/Documentos/cientificas_de_datos/model/spam_vectorizer_v1.pkl"))

    # Transformar el mensaje en un vector de características
    data = [message]
    vect = cv.transform(data).toarray()

    # Realizar la predicción de spam
    prediction = clf.predict(vect)

    return prediction


def test_spam_detection():
    # Arrange
    message = "Buy now and get a discount!"
    expected_prediction = ['spam']

    # Act
    prediction = detect_spam(message)

    # Assert
    assert prediction == expected_prediction

    # Print result
    if prediction == expected_prediction:
        print("La predicción de spam es correcta.")
    else:
        print("Error: La predicción de spam no es la esperada.")


# Ejecutar la prueba
test_spam_detection()