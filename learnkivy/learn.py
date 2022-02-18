
'''
import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App # مهمة  App  انشاء نافذة

# class name class  |=> fFirst letter capital ():
class Name(App):
    pass # if I don't have code yet
if __name__ == '__main__': # امر تشغيل التطبيق داخل الكلاس
    Name().run()
'''

# عشان استدعي ملف خارجي داخل الملف الحالي لازم يكون بنفس الاسم والحروف صغيرةويكونو في نفس المجلد
#  انشاء داله داخل الكلاس 


import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App 
from kivy.core.window import Window
# red | green | ble | opacity
Window.clearcolor = (100/255.0,0,0,0)
class Myapp(App):
    def  build(self):
         pass
        
if __name__ == '__main__': 
    Myapp().run()