import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
Window.clearcolor = (0,0,0,0)
Window.size =(400, 600)

class Myapp(App):
    def build(self):
        self.title = 'FALLATAH'
        cb = CheckBox()
        cb.bind(active=clicko)
        return cb
def clicko(cb, bb): # نريد منه عندما نضع صخ في الشك بوكس يطبع ميل او يس
    if bb: # هذا المتغير نختار اي اسم نبغاه
        print('MAle')# اذا قمنا بتحديد مربع الاختيار اطبع ميل
    else:
        print('Fmale')
    
Myapp().run()
