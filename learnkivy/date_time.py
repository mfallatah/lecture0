import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import datetime
from kivy.uix.label import Label
from kivy.base import runTouchApp # من اجل اللمس في الجوال 
from kivy.properties import StringProperty
from kivy.core .window import Window
Window.size =(400,600)

class MyLabel(Label):
    text = str(datetime.datetime.now()) # variable
    time = StringProperty('') # variable
    def on_time(self):
        self.text = str(datetime.datetime.now())
runTouchApp(MyLabel())
    
    
    


