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
Window.size=(970,600)

class MainApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        self.sm = ScreenManager()
        self.resultScreen = output.ResultScreen(name='result',screen_manager=self.sm)
        self.sm.add_widget(fileSelect.FileSelectScreen(name='fileSelect', screen_manager=self.sm,resultScreen=self.resultScreen))
        self.sm.add_widget(self.resultScreen)
        self.sm.current = 'fileSelect'
        return self.sm

    def _on_file_drop(self, window, file_path):
        if not self.sm.current == 'fileSelect':
            return
        print(file_path)
        self.sm.transition.direction = 'left'
        self.sm.current = 'result'

        #出力結果テスト用
        finDic = {'健康運動':2,'英語':3,'工学融合':1}
        neDic = {'情報技術':1,'知能情報コア':10,'知能情報アドバンスト':9.5,'人文+社会+総合領域':10.5,'人+社+総+自然':10.5}
        self.resultScreen.setListData(finDic,neDic)
        return

if __name__ == "__main__":
    MainApp().run()

