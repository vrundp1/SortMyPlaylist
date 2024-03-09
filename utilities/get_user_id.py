import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Function to get Spotify object
def get_spotify(user_token):
    return spotipy.Spotify(auth=user_token)

# Function to get user's playlists
def get_playlists(spotify):
    playlists={}
    user_playlists=spotify.current_user_playlists()
    for playlist in user_playlists["items"]:
        playlists[playlist['name']]=playlist['id']
    return playlists.keys()
