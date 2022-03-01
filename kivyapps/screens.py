import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
# لاستدعاء ملف خارجي او كتابة كود مباشر داخل التطبيق
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
# يمكننا من خلاله انشاء اكثر من شاشة شاشة ولخد شاشة 2 ....
Window.clearcolor=(100/255.0,0,1,1)
Window.size=(400,630)

# ScreenManager = استدعاء الوجهات من خلال 
# اسم الكلاس اختياري لكن مابين القوسين ثابت
# أنشأنا كلاس لكل نافذة
class MainWindow(Screen): # شاشة صعيرة 
    pass
class SeconedWindow(Screen): # شاشة صعيرة 
    pass
class Error(Screen): 
    pass
class Python(Screen): 
    pass
class Php(Screen): 
    pass
class Swift(Screen): 
    pass
class Djanco(Screen): 
    pass
class Sql(Screen): 
    pass
class Java(Screen): 
    pass
class WindowManager(ScreenManager):  # هذي تعتبر الشاشة الرئيسية
    pass # حانكتب الاكواد في الملف الخارجي


# kv = ملف خارجي تم انشائه
# load_file = من اجل الاستعانة بملف خارجي
# load_string = من اجل الكتابة داخل التطبيق 
# استدعاء الملف الخارجي
kv = Builder.load_file('my.kv')
class MyMainApp(App):
    def build(self):  # سلف يعني الكلاس نفسه
        self.title ='MDF APP'
        return kv
        # السطر اللي فوق تشغيل الملف الخارجي
        
MyMainApp().run()
