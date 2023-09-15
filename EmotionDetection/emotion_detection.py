import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    final_response = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant_emotion, n = None, 0    
    for key in final_response:
        if float(final_response[key]) > n:
            n = final_response[key]
            dominant_emotion = key
    final_response['dominant_emotion'] = dominant_emotion
    
    return final_response