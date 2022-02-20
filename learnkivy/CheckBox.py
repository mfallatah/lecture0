from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
Window.clearcolor =(0,0,0,1)
Window.size =(400, 620)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH [checkbox]'
        cb = CheckBox()
        return cb
        


Myapp().run()
