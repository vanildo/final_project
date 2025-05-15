from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    if not text_to_analyze:
        return "Please provide text to analyze."
    
    result = emotion_detector(text_to_analyze)
    
    if result and result['dominant_emotion'] is not None:
        # Format the response for display
        response = "For the given text, the system response is "
        for emotion, score in result.items():
            response += f"{emotion}: {score} "
        response += f". The dominant emotion is {result['dominant_emotion']}"
        return response
    else:
        return "Invalid text! Please try again!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)