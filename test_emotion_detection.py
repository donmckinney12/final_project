"""Unit tests for the Emotion Detector module."""

import unittest
import json
from unittest.mock import patch, Mock

from EmotionDetection.EmotionDetector import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests the core emotion detector logic by mocking the external API call."""

    # Define mock JSON responses for testing the detector function
    MOCK_JOY_RESPONSE = json.dumps(
        {
            "emotion": {
                "document": {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.01,
                        "fear": 0.05,
                        "joy": 0.85,
                        "sadness": 0.07,
                    }
                }
            }
        }
    )

    MOCK_SAD_RESPONSE = json.dumps(
        {
            "emotion": {
                "document": {
                    "emotion": {
                        "anger": 0.1,
                        "disgust": 0.05,
                        "fear": 0.15,
                        "joy": 0.0,
                        "sadness": 0.7,
                    }
                }
            }
        }
    )

    @patch('EmotionDetector.requests.post')
    def test_emotion_detector_joy(self, mock_post):
        """Tests for correct detection of Joy emotion."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = self.MOCK_JOY_RESPONSE
        mock_post.return_value = mock_response

        # Call the function under test
        result = emotion_detector("I am so happy that I passed the course!")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertAlmostEqual(result['joy'], 0.85, places=2)

    @patch('EmotionDetector.requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        """Tests for correct detection of Sadness emotion."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = self.MOCK_SAD_RESPONSE
        mock_post.return_value = mock_response

        # Call the function under test
        result = emotion_detector("I feel down because I missed my flight.")

        # Assertions
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertAlmostEqual(result['sadness'], 0.7, places=2)

    @patch('EmotionDetector.requests.post')
    def test_api_error_handling(self, mock_post):
        """Tests that API error responses (like 404) are handled gracefully (Task 7)."""
        mock_response = Mock()
        mock_response.status_code = 404  # Simulate an API endpoint error
        mock_response.text = "Not Found"
        mock_post.return_value = mock_response

        # Call the function under test
        result = emotion_detector("Any text")

        # Assertions
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'API Error: 404')


if __name__ == '__main__':
    unittest.main()