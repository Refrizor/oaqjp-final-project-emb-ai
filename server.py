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
    emotion_data = emotion_detector(text, True)
    dominant_emotion = emotion_data['dominant_emotion']
    output = f"For the given statement, the system response is {emotion_data}. The dominant emotion is: <b>{dominant_emotion}</b>"
    return output

if __name__ == "__main__":
    app.run(debug=True)