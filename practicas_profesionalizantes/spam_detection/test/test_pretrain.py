#test de pre-train
import unittest
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

class TestPreTraining(unittest.TestCase):

    def test_pre_training(self):
        # Cargar los datos de entrenamiento
        data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
        data = data[["class", "message"]]
        x = data["message"]
        y = data["class"]

        # Crear el vectorizador
        cv = CountVectorizer()
        X = cv.fit_transform(x)

        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        # Crear el clasificador y entrenarlo
        clf = MultinomialNB()
        clf.fit(X_train, y_train)

        # Verificar la precisión del modelo
        accuracy = clf.score(X_test, y_test)

        # Comprobar si la precisión es mayor al 80%
        self.assertGreaterEqual(accuracy, 0.8)

if _name_ == '_main_':
    unittest.main()