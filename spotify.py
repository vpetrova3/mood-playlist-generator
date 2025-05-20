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
    'happy':   ['37i9dQZF1DXdPec7aLTmlC','37i9dQZF1DWYMfG0Px3qxF'],
    'sad':     ['37i9dQZF1DX7qK8ma5wgG1','37i9dQZF1DX3YSRoSdA634'],
    'angry':   ['37i9dQZF1DWWJOmJ7nRx0C','37i9dQZF1DX0XUsuxWHRQd'],
    'disgust': ['37i9dQZF1DX3YSRoSdA634'], 
    'fear':    ['37i9dQZF1DWYmmr74INQlb'],
    'surprise':['37i9dQZF1DWXRqgorJj26U'],
    'neutral': ['37i9dQZF1DWXRqgorJj26U','37i9dQZF1DX4WYpdgoIcn6'],
}

def get_playlists_for_mood(mood):
    ids = MOOD_PLAYLISTS.get(mood, MOOD_PLAYLISTS['neutral'])
    return [f"https://open.spotify.com/embed/playlist/{pid}" for pid in ids]