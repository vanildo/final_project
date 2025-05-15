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

    # For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.
    
    if result:
        # Format the response for display
        response = "For the given text, the system response is "
        for emotion, score in result.items():
            response += f"{emotion}: {score}<br>"
        response += f"The dominant emotion is {result['dominant_emotion']}"
        return response
    else:
        return "Error processing the text. Please try again."

if __name__ == '__main__':
    app.run(debug=True, port=5000)