from EmotionDetection import emotion_detector
from flask import Flask, render_template, request

# Basic Flask instantiation
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=['GET'])
def get_emotion_detector():
    text = request.args.get('textToAnalyze')
    return emotion_detector(text, True)

if __name__ == "__main__":
    app.run(debug=True)