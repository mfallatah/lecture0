import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة  
from kivy.uix.label import Label # اول خطوة استدعاء مكتبة النصوص
Window.clearcolor = (255/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة
        return Label(text='Python kivy',
                     color =(1,1,1,1), # لون النص
                     font_size=19
            
        ) 
if __name__ == '__main__': 
    Myapp().run()