"""
Flask server for emotion detection using the IBM Watson Emotion API.
This server accepts text input from users, processes it through the emotion
detection model, and returns the dominant emotion along with the associated scores.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the main HTML page for the emotion detection application.

    This route handles the home page request and serves the 'index.html' page
    that contains the text input form for emotion detection.

    Returns:
        str: The rendered HTML page for the user interface.
    """
    return render_template('index.html')  # Serve the main HTML page

@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    """
    Analyzes the provided text for emotions by calling the emotion_detector function.
    This function processes the user input, calls the emotion detection model, and
    returns a formatted HTML response displaying emotion scores and the dominant emotion.

    If the input text is empty or the dominant emotion is None, the function will
    return an error message.

    Returns:
        str: Formatted HTML string with emotion scores and dominant emotion.
             If invalid input, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()  # Get and strip input

    if not text_to_analyze:  # If input is empty
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:  # If API response is invalid
        return "Invalid text! Please try again."

    # Format the emotion scores into an HTML response
    response_html = f"""
        <p>Anger: {result['anger']}</p>
        <p>Disgust: {result['disgust']}</p>
        <p>Fear: {result['fear']}</p>
        <p>Joy: {result['joy']}</p>
        <p>Sadness: {result['sadness']}</p>
        <h3>Dominant Emotion: <strong>{result['dominant_emotion']}</strong></h3>
    """

    return response_html  # Return formatted results

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
