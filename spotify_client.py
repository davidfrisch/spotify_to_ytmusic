import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def get_playlist_tracks(self, username, playlist_id):
        results = self.sp.user_playlist_tracks(username, playlist_id)
        tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        return tracks

    def get_playlist_ids(self, username):
        playlists = self.sp.user_playlists(username)
        playlist_ids = []
        for playlist in playlists['items']:
            playlist_ids.append(playlist['id'])
        return playlist_ids

    def get_playlist_names(self, username):
        playlists = self.sp.user_playlists(username)
        playlist_names = []
        for playlist in playlists['items']:
            playlist_names.append(playlist['name'])
        return playlist_names



 