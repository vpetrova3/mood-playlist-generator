def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ['sad', 'depressed', 'blue']):
        return 'sad'
    elif any(word in text for word in ['happy', 'great', 'amazing']):
        return 'happy'
    elif any(word in text for word in ['angry', 'mad', 'furious']):
        return 'angry'
    elif any(word in text for word in ['chill', 'calm', 'relaxed']):
        return 'chill'
    else:
        return 'neutral'
