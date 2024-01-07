from spotify_client import SpotifyClient
from youtube_client import YouTubeMusicClient
from dotenv import load_dotenv
import os
load_dotenv()

scope = "user-library-read"
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
USERNAME = os.getenv("USERNAME")

def transfer_playlist(spotify_client, youtube_client, username):
    # Get all the playlist names and ids from Spotify
    playlist_names = spotify_client.get_playlist_names(username)
    playlist_ids = spotify_client.get_playlist_ids(username)

    # Get Youtube Music playlist 
    yt_playlist = youtube_client.get_playlists()
    yt_playlist_names = [x['title'] for x in yt_playlist]

    # Display available playlists for transfer
    print("Which playlist do you want to transfer?")
    for i, playlist_name in enumerate(playlist_names):
        already_exists = playlist_name in yt_playlist_names
        print(f"{i}: {playlist_name} {'(already exists)' if already_exists else ''}")

    playlist_choice = int(input("Enter your choice: "))

    if playlist_names[playlist_choice] in yt_playlist_names:
        are_you_sure = input("This playlist already exists. Are you sure you want to continue? (y/n): ")
        while are_you_sure.lower() not in ["y", "n"]:
            are_you_sure = input("Please enter y or n: ")
        if are_you_sure == "n":
            return

    # Get all the tracks from the chosen playlist
    tracks = spotify_client.get_playlist_tracks(username, playlist_ids[playlist_choice])
    print(f"Attempting to transfer {len(tracks)} tracks")

    # Create a new playlist on YouTube Music
    playlist_name = playlist_names[playlist_choice]
    playlist_description = ""
    youtube_playlist_id = youtube_client.create_playlist(playlist_name, playlist_description)

    # Search for and add each song to the YouTube Music playlist
    for track in tracks:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        youtube_song_id = youtube_client.get_song_id(song_name, artist_name)

        if youtube_song_id:
            print(f"Adding {song_name}")
            try:
                youtube_client.add_song_to_playlist(youtube_playlist_id, youtube_song_id)
            except Exception as e:
                print(f"Couldn't add {song_name}: {e}")
        else:
            print(f"Couldn't find {song_name}")

def main():
    SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
    SPOTIPY_REDIRECT_URI = 'your_spotify_redirect_uri'
    SCOPE = 'user-library-read'
    USERNAME = 'your_username'

    spotify_client = SpotifyClient(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE)
    youtube_client = YouTubeMusicClient("youtube_auth.json")

    transfer_playlist(spotify_client, youtube_client, USERNAME)

if __name__ == "__main__":
    main()