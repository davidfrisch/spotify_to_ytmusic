from ytmusicapi import YTMusic


class YouTubeMusicClient:
    def __init__(self, oauth_file_path):
        self.ytmusic = YTMusic(oauth_file_path)

    def create_playlist(self, name, description, privacy_status="PRIVATE"):
        return self.ytmusic.create_playlist(title=name, description=description, privacy_status=privacy_status)

    def get_song_id(self, song_name, artist_name):
        search_results = self.ytmusic.search(song_name + " " + artist_name)
        results_song = [x for x in search_results if x['resultType'] == 'song']
        return results_song[0]['videoId']

    def add_song_to_playlist(self, playlist_id, song_id):
        return self.ytmusic.add_playlist_items(playlist_id, [song_id])
    
    def get_playlists(self):
        return self.ytmusic.get_library_playlists()
