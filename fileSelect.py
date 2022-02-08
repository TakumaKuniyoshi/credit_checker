from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.core.window import Window
from kivy.lang import Builder

import os

from kivy.uix.screenmanager import Screen

import getPdfData


Builder.load_file('./editor.kv')

# 日本語フォント設定
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W2.ttc')



class LoadDialog(FloatLayout): #ファイル読み込み時のダイアログボタン
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class FileSelectScreen(Screen): 
    def __init__(self,name,screen_manager,resultScreen, **kw):
        super(FileSelectScreen,self).__init__()
        self.screen_manager = screen_manager
        self.name = name
        self.resultScreen = resultScreen

    loadfile = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self): #ファイル選択画面
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="成績表(PDFファイル形式)を選択してください", content=content, size_hint=(0.9, 0.9))
        self._popup.open()



    def load(self, path, filename): #ファイルの読み込み
        with open(os.path.join(path, filename[0])) as stream:
            path = os.path.join(path, filename[0]) #読み込まれたファイルのパス
            #print(path)
            #ここにPDFを読み込んだ後の処理を書く

        self.dismiss_popup()
        self.screen_manager.transition.direction = 'left'

        #単位数計算処理+出力リスト作成
        datas = getPdfData.getCreditData(path)
        self.resultScreen.setListData(datas)

        self.screen_manager.current = 'result'


Factory.register('LoadDialog', cls=LoadDialog)
