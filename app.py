from EmotionDetection import emotion_detector
from flask import Flask

# Basic Flask instantiation
app = Flask(__name__)

emotion = emotion_detector("I love this new technology.", True)

print(emotion)