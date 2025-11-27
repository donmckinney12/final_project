"""
Emotion Detection Module
This module provides emotion detection functionality using text analysis.
"""

from typing import Dict, Union


class EmotionDetector:
    """
    A class to detect emotions from text input.
    """

    def __init__(self):
        """Initialize the emotion detector with emotion keywords."""
        self.emotion_keywords = {
            'anger': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'rage', 'hate', 'frustrated'],
            'disgust': ['disgusting', 'gross', 'awful', 'terrible', 'nasty', 'revolting'],
            'fear': ['scared', 'afraid', 'terrified', 'anxious', 'worried', 'nervous', 'frightened'],
            'joy': ['happy', 'joyful', 'excited', 'delighted', 'pleased', 'wonderful', 'great', 'amazing', 'love'],
            'sadness': ['sad', 'depressed', 'unhappy', 'miserable', 'disappointed', 'lonely', 'hurt']
        }

    def _calculate_emotion_scores(self, text: str) -> Dict[str, float]:
        """Calculate emotion scores based on keyword matching."""
        if not text or not isinstance(text, str):
            return {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }

        text_lower = text.lower()
        word_count = len(text_lower.split())

        if word_count == 0:
            return {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }

        scores = {}
        for emotion, keywords in self.emotion_keywords.items():
            count = sum(1 for keyword in keywords if keyword in text_lower)
            scores[emotion] = min(count / max(word_count * 0.5, 1), 1.0)

        return scores

    def detect_emotion(self, text: str) -> Dict[str, Union[str, float, None]]:
        """Detect emotions from the input text."""
        if text is None or not isinstance(text, str) or not text.strip():
            return {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0,
                'dominant_emotion': None
            }

        scores = self._calculate_emotion_scores(text)
        dominant_emotion = max(scores, key=scores.get) if max(scores.values()) > 0 else None

        result = {
            'anger': scores['anger'],
            'disgust': scores['disgust'],
            'fear': scores['fear'],
            'joy': scores['joy'],
            'sadness': scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

        return result


def emotion_detector(text: str) -> Dict[str, Union[str, float, None]]:
    """Convenience function to detect emotions from text."""
    try:
        detector = EmotionDetector()
        return detector.detect_emotion(text)
    except:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': None
        }