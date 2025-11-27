"""
Emotion Detection Web Application
A Flask-based web service for detecting emotions in text.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.EmotionDetector import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    API endpoint for emotion detection.

    Expected JSON payload:
        {"textToAnalyze": "text string"}

    Returns:
        JSON response with emotion analysis
    """
    try:
        # Get JSON data from request
        data = request.get_json(force=True, silent=True)

        # Validate request data
        if data is None or not data:
            return jsonify({
                'error': 'No data provided',
                'status': 'error'
            }), 400

        if 'textToAnalyze' not in data:
            return jsonify({
                'error': 'Missing textToAnalyze field',
                'status': 'error'
            }), 400

        text_to_analyze = data['textToAnalyze']

        # Handle empty or None text
        if not text_to_analyze or not text_to_analyze.strip():
            return jsonify({
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None,
                'status': 'error',
                'message': 'Invalid text! Please provide valid text to analyze.'
            }), 400

        # Detect emotions
        result = emotion_detector(text_to_analyze)

        # Format response
        if result['dominant_emotion'] is None:
            response = {
                'anger': result['anger'],
                'disgust': result['disgust'],
                'fear': result['fear'],
                'joy': result['joy'],
                'sadness': result['sadness'],
                'dominant_emotion': result['dominant_emotion'],
                'status': 'error',
                'message': 'Invalid text! Please provide valid text to analyze.'
            }
            return jsonify(response), 400

        response = {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion'],
            'status': 'success'
        }

        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({
            'error': str(ve),
            'status': 'error'
        }), 400

    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'details': str(e),
            'status': 'error'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'Emotion Detection API'
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)