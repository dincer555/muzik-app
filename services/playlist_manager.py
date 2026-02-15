import json
import os

class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.playlist_file = 'playlists.json'
        self.load_playlists()
    
    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = []
            self.save_playlists()
            return True
        return False
    
    def add_to_playlist(self, playlist_name, song_path):
        if playlist_name in self.playlists:
            if song_path not in self.playlists[playlist_name]:
                self.playlists[playlist_name].append(song_path)
                self.save_playlists()
                return True
        return False
    
    def remove_from_playlist(self, playlist_name, song_path):
        if playlist_name in self.playlists and song_path in self.playlists[playlist_name]:
            self.playlists[playlist_name].remove(song_path)
            self.save_playlists()
            return True
        return False
    
    def get_playlist(self, name):
        return self.playlists.get(name, [])
    
    def save_playlists(self):
        with open(self.playlist_file, 'w') as f:
            json.dump(self.playlists, f)
    
    def load_playlists(self):
        if os.path.exists(self.playlist_file):
            with open(self.playlist_file, 'r') as f:
                self.playlists = json.load(f)
