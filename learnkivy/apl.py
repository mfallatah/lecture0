import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.core.window import Window
Window.size=(400,600)

class Regs(App):
    def build(self):
        self.title='LOGIN SIGNUP'
        pass
if __name__=='__main__':
    Regs().run()
    
'''
# نسوي ملف اسمه regs.kv  وننسخ هذا الكود فيه عشان 
BoxLayout:
    orientation:'vertical'
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'LOGIN'
            font_size:28
        Label:
            text:'USER NAME'
        TextInput:
            text:'ENTER YOUR EMAIL'
            multiline: False
            size_hint:(1,0.9)
        Label:
            text:'PASSWORD'
        TextInput:
            text:'ENTER YOUR PASSWORD'
            multiline: False
            size_hint:(1,0.9)
        BoxLayout:
            orientation:'horizontal'
            Button:
                text:'LOG IN'
            Button:
                text:'SIGN UP'
    BoxLayout:
        orientation:'horizontal'
        Label:
            text:'Developed py Mohammed Fallatah @ 2022'
        



'''