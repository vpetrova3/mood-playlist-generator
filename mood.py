from deepface import DeepFace
import cv2

# 1) Text‐based keyword mapping for seven moods(deepface allows 7)
TEXT_KEYWORDS = {
    'happy':   ['happy', 'joyful', 'great', 'amazing', 'glad', 'delighted'],
    'sad':     ['sad', 'depressed', 'blue', 'down', 'unhappy'],
    'angry':   ['angry', 'mad', 'furious', 'irate', 'annoyed'],
    'calm':    ['chill', 'calm', 'relaxed', 'peaceful', 'serene'],
    'surprise':['surprised', 'astonished', 'amazed', 'shocked'],
    'fear':    ['afraid', 'scared', 'fearful', 'terrified', 'anxious'],
    'disgust': ['disgusted', 'grossed', 'revolted', 'nauseated']
}

def detect_mood(text: str) -> str:
    """
    Simple keyword lookup in the user’s input text.
    Returns one of the seven moods, or 'neutral' if nothing matches.
    """
    text = text.lower()
    for mood, keywords in TEXT_KEYWORDS.items():
        if any(word in text for word in keywords):
            return mood
    return 'neutral'


def detect_mood_from_face() -> str:
    """
    Captures one frame from the default webcam, analyzes it with DeepFace,
    and returns the dominant emotion (lowercased).
    Falls back to 'neutral' on any error or if DeepFace returns something unexpected.
    """
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        print("❌ Failed to capture frame")
        return "neutral"

    try:
        # DeepFace.analyze now returns a dict with 'dominant_emotion'
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant = result.get('dominant_emotion', '').lower()
        print(f"🎯 Detected mood from face: {dominant}")

        # Only accept one of our known moods
        if dominant in TEXT_KEYWORDS or dominant == 'neutral':
            return dominant
        else:
            # Unexpected label
            return 'neutral'

    except Exception as e:
        print("DeepFace error:", e)
        return "neutral"
