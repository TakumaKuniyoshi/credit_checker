from kivy.app import App
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('./result.kv')

class ResultScreen(Screen):
    def __init__(self,name,screen_manager, **kwargs):
        self.screen_manager = screen_manager
        self.name = name
        super(ResultScreen, self).__init__()
        self.finishedList = MyList()
        self.needList = MyList()
        finList = {'健康運動':2,'英語':3,'工学融合':1}
        neList = {'情報技術':1,'知能情報コア':10,'知能情報アドバンスト':9.5,'人文+社会+総合領域':10.5,'人+社+総+自然':10.5}
        self.setListData(finList,neList)
        self.ids.finished.add_widget(self.finishedList)
        self.ids.need.add_widget(self.needList)
    
    def setListData(self,finishedList,needList):
        self.finishedList.addLists(finishedList)
        self.needList.addLists(needList)

class RLabel(Label):
    pass
class LLabel(Label):
    pass

class Border(Widget):
    pass

class MyList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 0
    
    def addItem(self,name,num):
        nameLabel = LLabel()
        nameLabel.text = name
        numLabel = RLabel()
        numLabel.text = f'{num}単位'
        self.rows += 2
        self.add_widget(nameLabel)
        self.add_widget(numLabel)
        self.add_widget(Border())
        self.add_widget(Border())

    def addLists(self,lists:dict):
        for name,num in lists.items():
            self.addItem(name,num)