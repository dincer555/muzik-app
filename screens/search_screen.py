from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget, IconRightWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from services.streaming_service import StreamingService
from kivy.clock import Clock

class SearchScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.streaming = StreamingService()
        self.search_timer = None
        self.build_ui()
    
    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Search field
        self.search_field = MDTextField(
            hint_text="Müzik ara...",
            mode="rectangle",
            size_hint_y=0.1
        )
        self.search_field.bind(text=self.on_search_text)
        layout.add_widget(self.search_field)
        
        # Results list
        scroll = ScrollView()
        self.results_list = MDList()
        scroll.add_widget(self.results_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def on_search_text(self, instance, value):
        # Debounce: 0.5 saniye bekle
        if self.search_timer:
            self.search_timer.cancel()
        if value.strip():
            self.search_timer = Clock.schedule_once(lambda dt: self.perform_search(value), 0.5)
    
    def perform_search(self, query):
        results = self.streaming.search_music(query)
        self.display_results(results)
    
    def display_results(self, results):
        self.results_list.clear_widgets()
        for track in results:
            item = ThreeLineAvatarIconListItem(
                text=track['title'],
                secondary_text=track['artist'],
                tertiary_text=track['album']
            )
            icon = IconLeftWidget(icon='music')
            play_icon = IconRightWidget(icon='play', on_release=lambda x, t=track: self.play_preview(t))
            item.add_widget(icon)
            item.add_widget(play_icon)
            self.results_list.add_widget(item)
    
    def play_preview(self, track):
        # Preview çal
        preview_url = track.get('preview')
        if preview_url:
            app = self.manager.get_screen('search').parent.parent
            if hasattr(app, 'music_player'):
                app.music_player.load_song(preview_url)
                app.music_player.play()
