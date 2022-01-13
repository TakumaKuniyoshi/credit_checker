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


resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W2.ttc')


sm = ScreenManager()
sm.add_widget(fileSelect.FileSelectScreen(name='fileSelect'))
sm.add_widget(output.ResultScreen(name='result'))
sm.current = 'fileSelect'
class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()

