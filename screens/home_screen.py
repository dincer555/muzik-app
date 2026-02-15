from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDFabButton
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.slider import Slider

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Song list
        scroll = ScrollView()
        self.song_list = MDList()
        scroll.add_widget(self.song_list)
        layout.add_widget(scroll)
        
        # Player controls
        controls = MDBoxLayout(size_hint_y=0.2, spacing=10)
        
        self.play_btn = MDIconButton(icon='play', on_release=self.toggle_play)
        self.prev_btn = MDIconButton(icon='skip-previous')
        self.next_btn = MDIconButton(icon='skip-next')
        
        controls.add_widget(self.prev_btn)
        controls.add_widget(self.play_btn)
        controls.add_widget(self.next_btn)
        
        layout.add_widget(controls)
        
        # Volume slider
        self.volume_slider = Slider(min=0, max=1, value=0.7, size_hint_y=0.1)
        self.volume_slider.bind(value=self.on_volume_change)
        layout.add_widget(self.volume_slider)
        
        self.add_widget(layout)
    
    def toggle_play(self, instance):
        player = self.manager.get_screen('home').parent.parent.music_player
        if player.is_playing:
            player.pause()
            self.play_btn.icon = 'play'
        else:
            player.unpause() if player.current_song else player.play()
            self.play_btn.icon = 'pause'
    
    def on_volume_change(self, instance, value):
        player = self.manager.get_screen('home').parent.parent.music_player
        player.set_volume(value)
    
    def load_songs(self, songs):
        self.song_list.clear_widgets()
        for song in songs:
            item = TwoLineListItem(text=song['title'], secondary_text=song['artist'])
            self.song_list.add_widget(item)
