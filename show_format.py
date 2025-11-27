from EmotionDetection import emotion_detector

print("\n" + "="*60)
print("TASK 3B: FORMATTED OUTPUT VALIDATION")
print("="*60)

# Test with positive emotion
text = "I love this new technology."
result = emotion_detector(text)

print(f"\nInput: {text}")
print("\nOutput Format:")
print(result)

print("\nFormatted Display:")
print(f"  anger: {result['anger']}")
print(f"  disgust: {result['disgust']}")
print(f"  fear: {result['fear']}")
print(f"  joy: {result['joy']}")
print(f"  sadness: {result['sadness']}")
print(f"  dominant_emotion: {result['dominant_emotion']}")

print("\n" + "="*60)
print("✅ Output format is correct!")
print("="*60 + "\n")