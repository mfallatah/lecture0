from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
Window.clearcolor =(0,0,0,1)
Window.size =(400, 620)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH [checkbox]'
        cb = CheckBox() # أنشانا متغير نسميه باي اسم ولكن بعد يساوي لاوم نكتب CheckBox
        cb.bind(active = clicko )  # عند النقر عليه
        return cb
        
def clicko(cb, ok): # نعدل على المتغير اللي انشاناه في الدرس السابق
    print('Mohammed Fallatah \nLern kivy \nCheckBox \n2022') #  لما اشغل الدالة راح يطبع في التريمنال 
Myapp().run()