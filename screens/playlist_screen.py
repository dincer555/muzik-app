from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.button import MDFabButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

class PlaylistScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=10)
        
        scroll = ScrollView()
        self.playlist_list = MDList()
        scroll.add_widget(self.playlist_list)
        layout.add_widget(scroll)
        
        # Add playlist button
        self.add_btn = MDFabButton(
            icon='plus',
            pos_hint={'center_x': 0.9, 'center_y': 0.1},
            on_release=self.show_create_dialog
        )
        
        self.add_widget(layout)
        self.add_widget(self.add_btn)
    
    def show_create_dialog(self, instance):
        self.dialog = MDDialog(
            title="Yeni Playlist",
            type="custom",
            content_cls=MDTextField(hint_text="Playlist adı"),
        )
        self.dialog.open()
