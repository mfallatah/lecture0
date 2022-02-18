import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة 
from kivy.uix.textinput import TextInput # اول خطوة نستدعي كلاس الادخال من المكتبة 
# red | green | ble | opacity  
Window.clearcolor = (200/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة 
        # ننشئ متغير
        texo = TextInput(
            text='Enter Your Email', # نص افتراضي
            multiline = False, # يمنع النزول لاسفل عند ضغط انتر
            font_size= 16,
            pos_hint={'x':0.3,'y':0.6}, # التمركز من اليسار ومن الاسفل
            size_hint=(0.5,0.05) # التحكم بحجم مساحة الادخال
            
            
        )  
        return texo
        
if __name__ == '__main__': 
    Myapp().run()