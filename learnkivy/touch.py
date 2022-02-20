import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.core.window import Window
from kivy.base import runTouchApp # خاصية الممس
from kivy.lang import Builder
Window.clearcolor = (0,0,0,0)
Window.size =(400, 600)

class Myapp(App): 
    def build(self):
        pass
runTouchApp(Builder.load_string('''
ActionBar:# القائمة العلوية
    pos_hint:{'top':1} # يطهر في الاعلى ملاصق للشريط العلوي
    ActionView:
        ActionPrevious:
            title:'FALLATAH' # تظهر في شريط العنوان
        ActionButton: # اضافة زر على البار مثل فايل اديت 
            text:'HOME'
        ActionButton:  
            text:'Back'
        ActionGroup: # القائمة المنسدلة 
            text:'More'
            color:.3, .6, 2,1
            ActionButton:
                text:'test'
            ActionButton:
                text:'test1'
            ActionButton:
                text:'test2'
            ActionButton:
                text:'tes3'                       
'''))
Myapp().run()



# المسافات حساسة جدا في قائمة Action لابد من عمل تاب مرتين او اربع مسافات