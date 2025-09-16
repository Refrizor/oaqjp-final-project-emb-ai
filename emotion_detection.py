import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def create_request(text_to_analyze):
    """Sends a POST request to Watson's LLM library

    :param text_to_analyze: Input text to be analyzed.
    :return: dict if success, None otherwise
    """

    text_to_analyze = text_to_analyze.lower()
    request = requests.post(URL, json={"raw_document": {"text": text_to_analyze}}, headers=HEADERS)

    try:
        response = request.json().get("emotionPredictions")
        return response
    except Exception as e:
        print("Error parsing the response:", request.raise_for_status(), e)

def emotion_detector(text, verbose=False):
    """Detects emotions using Watson's LLM library

    :param verbose: Printing output
    :param text: Input text to be passed to request and analyzed
    """

    response = create_request(text)
    if verbose: print(json.dumps(response, indent=2))
    return response