from concurrent.futures import thread
import threading
from tracemalloc import start
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.core.window import Window

import os
import output
import fileSelect
import getPdfData
import loading


resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W2.ttc')
Window.size=(970,600)

class MainApp(App):
    title = 'credit checker'
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        self.sm = ScreenManager()
        self.resultScreen = output.ResultScreen(name='result',screen_manager=self.sm)
        self.sm.add_widget(fileSelect.FileSelectScreen(name='fileSelect', screen_manager=self.sm,resultScreen=self.resultScreen))
        self.sm.add_widget(self.resultScreen)
        self.sm.add_widget(loading.LoadingScreen(name='loading', screen_manager=self.sm))
        self.sm.current = 'fileSelect'
        return self.sm

    def _on_file_drop(self, window, file_path):
        if not self.sm.current == 'fileSelect':
            return
        print(file_path)
        self.sm.transition.direction = 'left'
        datas = getPdfData.getCreditData(file_path)
        self.resultScreen.setListData(datas)
        self.sm.current = 'result'
        return

if __name__ == "__main__":
    MainApp().run()
