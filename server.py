"""
Flask server for emotion detection application.
This module provides a web interface for detecting emotions in text using Watson NLP API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page of the application.
    
    Returns:
        The rendered index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Process text input and detect emotions using the emotion_detector function.
    
    Returns:
        str: A formatted string containing the detected emotions and their scores,
             or an error message if the text is invalid.
    """
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

    return "Invalid text! Please try again!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
