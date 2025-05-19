# Mood-Based Playlist Generator

A fun web app that detects your mood from a short message and recommends a Spotify playlist to match.


## Features
- Detects mood from text input (e.g. "I'm feeling relaxed")
- Matches your mood to curated Spotify playlists
- Built with Flask, Python, JavaScript, and the Spotify Web API

## How It Works
1. You type how you're feeling.
2. The app classifies your mood using simple NLP.
3. A Spotify playlist opens based on your mood.

## Technologies Used
- Python (Flask)
- Spotify API (`spotipy`)
- JavaScript (fetch API)
- HTML/CSS
- dotenv for API key security

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Setup Instructions
```bash
git clone https://github.com/YOUR_USERNAME/mood-playlist-generator.git
cd mood-playlist-generator
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
