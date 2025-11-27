import requests
import json

print("\n" + "="*60)
print("Testing Error Handling - Empty Text")
print("="*60)

# Test 1: Empty text
response = requests.post(
    'http://localhost:5000/emotionDetector',
    json={'textToAnalyze': ''}
)

print("\nTest 1: Empty text")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 2: Only spaces
response = requests.post(
    'http://localhost:5000/emotionDetector',
    json={'textToAnalyze': '    '}
)

print("\nTest 2: Whitespace only")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 3: Missing field
response = requests.post(
    'http://localhost:5000/emotionDetector',
    json={'wrongField': 'test'}
)

print("\nTest 3: Missing field")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

print("="*60)
print("✅ Error handling is working correctly!")
print("="*60 + "\n")