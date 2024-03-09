import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set the redirect URL for authentication
REDIRECT="http://localhost:1337"

# Define the required scopes for accessing playlists
SCOPE="playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative"

# Function to get Spotify API credentials from user input
def get_tokens():
    tokens={}
    tokens["client_id"] = input("Insert the Client ID: ")          # Prompt for client ID
    tokens["client_secret"] = input("Insert the Client Secret: ")  # Prompt for client secret
    tokens["name"] = input("Insert your Spotify Username: ")       # Prompt for Spotify username
    return tokens

# Function to get client manager
def get_client_manager(client_tokens):
    return SpotifyClientCredentials(client_id=client_tokens["client_id"], client_secret=client_tokens["client_secret"])

# Function to generate user token
def generate_user_token(client_tokens):
    # Prompt the user to log in to Spotify and grant access
    return spotipy.util.prompt_for_user_token(
        username=client_tokens["name"],
        scope=SCOPE,
        client_id=client_tokens["client_id"],
        client_secret=client_tokens["client_secret"],
        redirect_uri=REDIRECT
    )