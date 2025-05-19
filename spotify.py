import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')
))

MOOD_PLAYLISTS = {
    'happy': '37i9dQZF1DXdPec7aLTmlC',
    'sad': '37i9dQZF1DX7qK8ma5wgG1',
    'angry': '37i9dQZF1DWWJOmJ7nRx0C',
    'chill': '37i9dQZF1DX889U0CL85jj',
    'neutral': '37i9dQZF1DWXRqgorJj26U'
}

def get_playlist_for_mood(mood):
    playlist_id = MOOD_PLAYLISTS.get(mood, MOOD_PLAYLISTS['neutral'])
    return f"https://open.spotify.com/playlist/{playlist_id}"
