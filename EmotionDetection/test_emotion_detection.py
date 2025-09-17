from unittest import TestCase
from . import emotion_detector

class Test(TestCase):
    def test_joy(self):
        res = emotion_detector("I am glad this happened", True)
        self.assertEqual(res["dominant_emotion"], "joy")

    def test_anger(self):
        res = emotion_detector("I am really mad about this	", True)
        self.assertEqual(res["dominant_emotion"], "anger")

    def test_disgust(self):
        res = emotion_detector("I feel disgusted just hearing about this", True)
        self.assertEqual(res["dominant_emotion"], "disgust")

    def test_sadness(self):
        res = emotion_detector("I am so sad about this	", True)
        self.assertEqual(res["dominant_emotion"], "sadness")

    def test_fear(self):
        res = emotion_detector("I am really afraid that this will happen	", True)
        self.assertEqual(res["dominant_emotion"], "fear")