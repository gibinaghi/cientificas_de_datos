#ChatGPT para prueba estática
import unittest
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

class TestSpamDetection(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
        self.data = self.data[["class", "message"]]
        self.x = np.array(self.data["message"])
        self.y = np.array(self.data["class"])
        self.cv = CountVectorizer()
        self.X = self.cv.fit_transform(self.x)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.33, random_state=42)
        self.clf = MultinomialNB()
        self.clf.fit(self.X_train, self.y_train)

    def test_data_loaded(self):
        self.assertEqual(len(self.data), 5572)  # Verificar si se han cargado todos los datos

    def test_model_accuracy(self):
        accuracy = self.clf.score(self.X_test, self.y_test)
        self.assertGreater(accuracy, 0.8)  # Verificar si la precisión del modelo es mayor al 80%

if _name_ == '_main_':
    unittest.main()