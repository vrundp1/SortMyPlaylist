import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from auth.py import get_tokens, generate_user_token
from get_user_id import get_spotify, get_playlists

if __name__ == "__main__":
    # Get Spotify API credentials from user input
    tokens = get_tokens()
    print("Tokens obtained successfully")

    # Generate user token using provided credentials
    user_token=generate_user_token(tokens)
    spotify=get_spotify(user_token)

    # Get and print user's playlists
    playlists1 = get_playlists(spotify)
    print(playlists1)