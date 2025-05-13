import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse: str) -> str:
  input = { "raw_document": { "text": f'{text_to_analyse}' } }
  response = requests.post(URL, json=input, headers=HEADERS)
  
  if response.status_code == 200:
    res = json.loads(response.text)

    emotions = {
      'anger': res[0]['emotion']['anger'],
      'disgust': res[0]['emotion']['disgust'],
      'fear': res[0]['emotion']['fear'],
      'joy': res[0]['emotion']['joy'],
      'sadness': res[0]['emotion']['sadness'],
    }

    formatted_res = {
      **emotions,
      'dominant_emotion': sorted(emotions.items(), key=lambda x: x[1], reverse=True)[0][0]
    }

  return formatted_res
  # else:
  #   return ''


if __name__ == '__main__':
  print(emotion_detector('I love this new technology.'))