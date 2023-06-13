#prueba unitaria
import unittest
from unittest.mock import patch
from io import StringIO
import sys

from deteccion_spam import spamdetection

class TestSpamDetection(unittest.TestCase):

    @patch('builtins.input', return_value='Win a million dollars in a day!')
    def test_spam_detection_spam_input(self, mock_input):
        expected_output = "Spam"

        # Capturar la salida estándar
        captured_output = StringIO()
        sys.stdout = captured_output

        # Ejecutar la función de detección de spam
        spamdetection()

        # Restaurar la salida estándar
        sys.stdout = sys._stdout_

        # Obtener la salida capturada
        actual_output = captured_output.getvalue().strip()

        # Verificar si la salida es la esperada
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', return_value='Hello, how are you?')
    def test_spam_detection_non_spam_input(self, mock_input):
        expected_output = "No spam"

        # Capturar la salida estándar
        captured_output = StringIO()
        sys.stdout = captured_output

        # Ejecutar la función de detección de spam
        spamdetection()

        # Restaurar la salida estándar
        sys.stdout = sys._stdout_

        # Obtener la salida capturada
        actual_output = captured_output.getvalue().strip()

        # Verificar si la salida es la esperada
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', return_value='')
    def test_spam_detection_empty_input(self, mock_input):
        expected_output = ""

        # Capturar la salida estándar
        captured_output = StringIO()
        sys.stdout = captured_output

        # Ejecutar la función de detección de spam
        spamdetection()

        # Restaurar la salida estándar
        sys.stdout = sys._stdout_

        # Obtener la salida capturada
        actual_output = captured_output.getvalue().strip()

        # Verificar si la salida es la esperada
        self.assertEqual(actual_output, expected_output)

if __name__ == '_main_':
    unittest.main()