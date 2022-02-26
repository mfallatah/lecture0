# لاضافة سكرول بار للصفحة 

import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder # للكتابة داخل المف الحالي دون الحجة لملف خارجي
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.core.window import Window
Window.clearcolor=(100/255.0,0,0,0)
Window.size =(400, 600)
# من اجل كتابة الاكواد داخل البرنامج نفسه
Builder .load_string('''
<Scroll>:
    text:'Welcome To Python Course 2022 Interduced Py Mohammed Fallatah' * 100
    Label:
        text: root.text  # الروت يدل على لبرنامج نفسه
        font_size: 22
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
    
                     
''')
class Scroll(ScrollView): # هذا لازم يكون نفس الاسم اللي في سكرول تحت بيلدر
    text = StringProperty('')
runTouchApp(Scroll())
    