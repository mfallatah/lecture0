from kivy.app import App 
from kivy.core.window import Window # لتغيير خلفية النافذة  
from kivy.uix.image import Image, AsynceImage  #   من اجل التعامل مع الصور ايميج لادراج صورة من الكمبيوتر واساينس ايميج لادراج صورة من النت
Window.clearcolor = (255/255.0,0,0,0)
Window.size =(400,600)
class Myapp(App):
    def build(self):
        self.title = 'FALLATAH' # لتغيير عنوان البرنامج في اعلى الصحفة
        img = Image(
            source = 'C:\\Users\DAR-S19021\Desktop\m.jpeg', # مسار الصورة
            size_hint = (0.5,0.5), # عرض الصورة وارتفاعها  
            pos_hint = {'x':0.27, 'y':0.3}, # تمركز الصورة في البرنامج

        )
        # لادراج صورة من الانترنت
        # img = AsyncImage(source = 'url')
        return img
     
if __name__ == '__main__': 
    Myapp().run()
