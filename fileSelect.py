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
            print(path)
            #ここにPDFを読み込んだ後の処理を書く

        self.dismiss_popup()
        self.screen_manager.transition.direction = 'left'

        #単位数計算処理+出力リスト作成
        #-----テスト用-----
        finDic = {'健康運動':2,'英語':3,'工学融合':1,'英語プレゼンテーション中級':10}
        neDic = {'情報技術':1,'知能情報コア':10,'知能情報アドバンスト':9.5,'人文+社会+総合領域':10.5,'人+社+総+自然':10.5}
        self.resultScreen.setListData(finDic,neDic)
        #-----テスト用-----

        self.screen_manager.current = 'result'


    

class Editor(App):
    def build(self):#ドラッグ&ドロップの処理
        Window.bind(on_dropfile=self.on_dropped_file)
        return FileSelectScreen()

    def on_dropped_file(self, window, file_path): #ドラッグ&ドロップの処理
        self.root.text = file_path.decode('utf-8')
        path = file_path.decode('utf-8') #読み込まれたファイルのパス
        print(path)


Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    Editor().run()