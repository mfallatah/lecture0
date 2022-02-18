import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة  
from kivy.uix.button import Button # step 1
Window.clearcolor = (255/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة
        b1 = Button( # step2
            text='Home ', # النص الذي يظهر على الزر
            size_hint=(0.3,0.1), # التحكم بعرض الز وارتفاعه
            font_size = '22', #حجم النص
            color =(1,1,1,1), # لون النص
            background_color=(0,0,0.3,0), # لون خلفية الزر
            on_press   = self.clickkyes, # اون بريس واون ريليز ثابته ومعناها عند النقر وعند الافلات
            on_release = self.clickno # النتيجة تظهر في التيرمنال
            
            
        )
        return b1
    #  الخطوة  الثالثة ننشئ دالتين ونستدعيها في داخل الزر لانها مرتبطة به
    def clickkyes(self,yes):
        print('cliked')
    def clickno(self,no):
        print('unkliked')
if __name__ == '__main__': 
    Myapp().run()