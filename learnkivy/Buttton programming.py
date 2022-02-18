import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة 
from kivy.uix.button import Button # اول خطوة نستدعي كلاس الزر من المكتبة 
# red | green | ble | opacity  
Window.clearcolor = (200/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة
        # ننشئ متغير للزر كثاني خطوة
        b1 = Button(
            text='HOME',
            size_hint=(0.3,0.1), #التحكم في عرض وارتفاع الزر
            pos_hint={'x':0.33, 'y':0.01}, # موقع الزر  الواي تعني من اسفل لاعلى 
            color=(1,1,1,1), # لون الزر
            background_color=(0,0,3,1), # لون خلفية النص 
            
        )
        return b1
        
if __name__ == '__main__': 
    Myapp().run()