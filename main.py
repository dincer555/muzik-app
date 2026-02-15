from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from screens.home_screen import HomeScreen
from screens.playlist_screen import PlaylistScreen
from screens.search_screen import SearchScreen
from services.music_player import MusicPlayer

class MusicApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music_player = MusicPlayer()
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        
        # Bottom navigation
        nav = MDBottomNavigation()
        
        # Home tab
        home_item = MDBottomNavigationItem(
            name='home',
            text='Ana Sayfa',
            icon='home'
        )
        home_item.add_widget(HomeScreen())
        nav.add_widget(home_item)
        
        # Search tab
        search_item = MDBottomNavigationItem(
            name='search',
            text='Ara',
            icon='magnify'
        )
        search_item.add_widget(SearchScreen())
        nav.add_widget(search_item)
        
        # Playlist tab
        playlist_item = MDBottomNavigationItem(
            name='playlist',
            text='Playlist',
            icon='playlist-music'
        )
        playlist_item.add_widget(PlaylistScreen())
        nav.add_widget(playlist_item)
        
        return nav

if __name__ == '__main__':
    MusicApp().run()
