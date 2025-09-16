from emotion_detection import emotion_detector
from flask import Flask

# Basic Flask instantiation
app = Flask(__name__)

emotion_detector("I love this new technology.", True)