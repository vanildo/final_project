import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse: str) -> str:
  input = { "raw_document": { "text": f'{text_to_analyse}' } }
  response = requests.post(URL, json=input, headers=HEADERS)
  
  if response.status_code == 200:
    res = response.json()
    # emotion = res['emotionPredictions'][0]['emotion']
    # dominant_emotion = max(emotion, key=emotion.get)
    print(res)

if __name__ == '__main__':
  print(emotion_detector('I love this new technology.'))