import pygame
from mutagen.mp3 import MP3
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None
        self.is_playing = False
        self.playlist = []
        self.current_index = 0
        
    def load_song(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            self.current_song = file_path
            return True
        except Exception as e:
            print(f"Error loading song: {e}")
            return False
    
    def play(self):
        if self.current_song:
            pygame.mixer.music.play()
            self.is_playing = True
    
    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False
    
    def unpause(self):
        pygame.mixer.music.unpause()
        self.is_playing = True
    
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
    
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
    
    def get_song_info(self, file_path):
        try:
            audio = MP3(file_path)
            return {
                'title': audio.get('TIT2', os.path.basename(file_path)),
                'artist': audio.get('TPE1', 'Unknown'),
                'duration': audio.info.length
            }
        except:
            return {'title': os.path.basename(file_path), 'artist': 'Unknown', 'duration': 0}
    
    def load_local_music(self, directory):
        songs = []
        for file in os.listdir(directory):
            if file.endswith(('.mp3', '.wav', '.ogg')):
                songs.append(os.path.join(directory, file))
        return songs
