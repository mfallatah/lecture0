import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة 
# red | green | ble | opacity  
Window.clearcolor = (200/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة
        pass
        
if __name__ == '__main__': 
    Myapp().run()