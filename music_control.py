import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_music(track_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_client_id",
                                                   client_secret="your_client_secret",
                                                   redirect_uri="http://localhost:8888/callback",
                                                   scope="user-library-read"))
    results = sp.search(q=track_name, limit=1)
    track = results['tracks']['items'][0]
    sp.start_playback(uris=[track['uri']])
