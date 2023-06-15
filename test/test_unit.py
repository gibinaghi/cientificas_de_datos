import unittest
from deteccion_spam import spamdetection

class TestSpamDetection(unittest.TestCase):

    def test_spam_detection(self):
        sample = "Free money! Claim now!"
        expected_prediction = "spam"
        prediction = spamdetection(sample)
        assert prediction == expected_prediction, f"Error: Expected {expected_prediction}, but got {prediction}"

if __name__ == '__main__':
    unittest.main()