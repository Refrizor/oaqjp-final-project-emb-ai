import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
ERROR_DICT = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

def create_request(text_to_analyze: str) -> list | dict[str, None]:
    """Sends a POST request to Watson's LLM library

    :param text_to_analyze: Input text to be analyzed.
    :return: dict if success, None otherwise
    """

    text_to_analyze = text_to_analyze.lower()
    request = requests.post(URL, json={"raw_document": {"text": text_to_analyze}}, headers=HEADERS)
    status = request.status_code

    if status == 400:
        return ERROR_DICT

    try:
        response = request.json().get("emotionPredictions", [])
        return response
    except Exception as e:
        print("Error parsing:", e)
        return ERROR_DICT

def emotion_detector(text: str, verbose: bool = False) -> dict | None:
    """Detects emotions using Watson's LLM library thingy

    :param text: Input text to be used in the request
    :param verbose: Output request for testing
    :return: emotion results from create_request
    """

    response = create_request(text)

    # If Watson shoots a 400, create_request already returned the dict of Nones
    if isinstance(response, dict) and response["dominant_emotion"] is None:
        return response

    # Otherwise, proceed
    emotion_dict = response[0]["emotion"]

    dominant_emotion = get_dominant_emotion(emotion_dict)
    emotion_dict["dominant_emotion"] = dominant_emotion

    if verbose: print("Beautified output:", json.dumps(emotion_dict, indent=2))
    return emotion_dict

def get_dominant_emotion(emotions: dict[str, float]) -> str:
    """Find the emotion with the highest score :D

    :param emotions: Dictionary mapping emotion names to scores
    :return: The name of the emotion (str)
    """

    emotion = max(emotions, key=emotions.get)
    return emotion