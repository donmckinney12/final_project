from EmotionDetection import emotion_detector

text = "I am so happy and excited today!"
result = emotion_detector(text)

print("="*50)
print("Emotion Detection Output Format Test")
print("="*50)
print(f"Input text: {text}")
print("\nFormatted Output:")
print(result)
print("\nOutput Structure:")
for key, value in result.items():
    print(f"  {key}: {value}")
print("="*50)