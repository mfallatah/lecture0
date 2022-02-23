# box layout  = item fixed
# flut layout  = items can be conrle and moved

import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
Window.size=(400,600)

class Fapp(App):
    def build(self):
        self.title='Drag App'
        f= FloatLayout()
        s= Scatter() # s is locate inside f
        l= Label(text='MOHAMMED FALLATAH', font_size=20)
        f.add_widget(s) # المتعير اللي حاي
        s.add_widget(l)
        return f
        
if __name__=='__main__':
    Fapp().run()

# للتدوير والتكبير والتصغير نقوم بالضغط على زرالماوس الايمن تظهر علامة حمراء ثم بالزر الايسر يتم التدوير والتكبير والتصغير ويمكننا اضافة صور وازارير بنفس الخاصية