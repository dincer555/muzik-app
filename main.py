from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text="Ana Sayfa", halign="center"))

class SearchScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text="Arama", halign="center"))

class PlaylistScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text="Playlist", halign="center"))

class MusicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        
        nav = MDBottomNavigation()
        
        home_item = MDBottomNavigationItem(name='home', text='Ana Sayfa', icon='home')
        home_item.add_widget(HomeScreen())
        nav.add_widget(home_item)
        
        search_item = MDBottomNavigationItem(name='search', text='Ara', icon='magnify')
        search_item.add_widget(SearchScreen())
        nav.add_widget(search_item)
        
        playlist_item = MDBottomNavigationItem(name='playlist', text='Playlist', icon='playlist-music')
        playlist_item.add_widget(PlaylistScreen())
        nav.add_widget(playlist_item)
        
        return nav

if __name__ == '__main__':
    MusicApp().run()
