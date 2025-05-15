import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse: str) -> dict:
  error_response = {
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion': None
  }

  # Check for blank entries
  if not text_to_analyse.strip():
    return error_response
    
  input = { "raw_document": { "text": f'{text_to_analyse}' } }
  response = requests.post(URL, json=input, headers=HEADERS)
  
  # Check for status code 400 or any other error
  if response.status_code != 200:
    return error_response
    
  res = json.loads(response.text)

  # Extract emotion scores
  emotions = {
    'anger': res[0]['emotion']['anger'],
    'disgust': res[0]['emotion']['disgust'],
    'fear': res[0]['emotion']['fear'],
    'joy': res[0]['emotion']['joy'],
    'sadness': res[0]['emotion']['sadness']
  }
  
  # Find the dominant emotion (emotion with highest score)
  dominant_emotion = max(emotions, key=emotions.get)
  
  # Create the formatted response with dominant emotion
  result = {
    **emotions,
    'dominant_emotion': dominant_emotion
  }
  
  return result


if __name__ == '__main__':
  print(emotion_detector('I love this new technology.'))