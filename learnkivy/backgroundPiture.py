import os # if the kivy not running we have to add those tow line
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.core.window import Window
Window.size =(370, 600)
class Picture(App):
    def build(self):
        pass
if __name__=='__main__':
    Picture().run()

'''
# creat new file named picture same anme of class and puting this text n it
# هسم الملف لازم يكون بنفس اسم الكلاس وبحروف صغيرة

FloatLayout:  # من اجل الخلفية ولون الخلفية
    canvas:
        Color:    # لازم الحرف الاول يكون كبير 
            rgb: 1,1,1
        Rectangle:   # من اجل الصورة في الخلفية
            source:'44.jpg'
            size: self.size  # يعني ياخذ كامل حجم الصفحة
    BoxLayout:  # لتقسيم الصفحة حصصنا الجزء الاعلى من الصفحة
        padding:10   # من الاعلى يبتعد 10
        spacing:10   # ياخذ مسافة 10 من اليسار
        size_hint:1,None # معناها العرض كامل الصفحة والطول يتعرف عليه تلقائيا
        pos_hint: {'top':1} # تمركز البوكس يكون في الاعلى 
        height: 44  # ارتفاع البوكس 44
        Image:
            size_hint: None, None
            size: 24, 24  # حجم الصورة في البوكس 
            source: 'bl.png'
        Label:
            height: 22  # نص البوكس لان ارتفاعه 44
            text_size: self.width, None
            color: (1,1,1,1)
            text: 'MOHAMMED FALLATAH'
#https://www.youtube.com/watch?v=fhED37dHyLM&list=PLSiLeKadTQ7l7DJIUbCj749eAiwIHE4hH&index=25
'''