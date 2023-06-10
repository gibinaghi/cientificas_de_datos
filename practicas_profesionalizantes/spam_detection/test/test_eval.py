#prueba de funcionalidad de la evaluación
import unittest
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score

class TestModelEvaluation(unittest.TestCase):

    def setUp(self):
        # Cargar los datos de entrenamiento
        self.data_train = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
        self.data_train = self.data_train[["class", "message"]]
        self.x_train = self.data_train["message"]
        self.y_train = self.data_train["class"]

        # Crear el vectorizador
        self.cv = CountVectorizer()
        self.X_train = self.cv.fit_transform(self.x_train)

        # Dividir los datos en entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_train, self.y_train, test_size=0.33, random_state=42)

        # Crear el clasificador y entrenarlo
        self.clf = MultinomialNB()
        self.clf.fit(self.X_train, self.y_train)

    def test_precision(self):
        # Proporcionar un conjunto de datos de prueba específico
        test_samples = [
            "Free money! Claim now!",
            "Hello, how are you?",
            "Get the latest offers!"
        ]
        test_labels = ["spam", "not spam", "spam"]

        # Transformar los datos de prueba
        X_test = self.cv.transform(test_samples)

        # Realizar la predicción en los datos de prueba
        y_pred = self.clf.predict(X_test)

        # Calcular la precisión del modelo
        precision = precision_score(test_labels, y_pred, pos_label='spam')

        # Verificar que la precisión calculada coincida con el valor esperado
        expected_precision = 0.6666666666666666
        self.assertAlmostEqual(precision, expected_precision, places=2)

if _name_ == '_main_':
    unittest.main()