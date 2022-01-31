from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('./loading.kv')

class LoadScreen(Screen):
    def __init__(self,name,screen_manager, **kwargs):
        self.screen_manager = screen_manager
        self.name = name
        super(LoadScreen, self).__init__()
