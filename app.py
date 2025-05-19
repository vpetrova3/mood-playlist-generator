from flask import Flask, render_template, request, jsonify
from mood import detect_mood, detect_mood_from_face
from spotify import get_playlist_for_mood

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_playlist', methods=['POST'])
def get_playlist():
    user_text = request.json['text']
    mood = detect_mood(user_text)
    playlist_url = get_playlist_for_mood(mood)
    return jsonify({'mood': mood, 'playlist': playlist_url})

@app.route('/face_mood', methods=['GET'])
def face_mood():
    print("🧠 Face detection started")
    mood = detect_mood_from_face()
    print(f"🎯 Detected mood: {mood}")
    playlist_url = get_playlist_for_mood(mood)
    return jsonify({'mood': mood, 'playlist': playlist_url})

if __name__ == '__main__':
    app.run(debug=True)
