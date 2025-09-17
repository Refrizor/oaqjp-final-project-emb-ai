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

    if emotion_data["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    dominant_emotion = emotion_data.pop('dominant_emotion')

    parts = [f"'{k}': {v}" for k, v in emotion_data.items()]

    if len(parts) > 1:
        pretty = ", ".join(parts[:-1]) + " and " + parts[-1]
    else:
        pretty = parts[0]

    output = (
        f"For the given statement, the system response is {pretty}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )
    return output

if __name__ == "__main__":
    app.run(debug=True)