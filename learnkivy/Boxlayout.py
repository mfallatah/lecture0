from kivy.app import App
from kivy.uix.label import Label
class Group(App):
    pass
if __name__ == '__main__': # امر تشغيل الكلاس
    Group().run()

# Boxlayout
# هذه الخاصية من اجل تكرار العناصر لاانا لو اظفنا اكثر من ليبل مايقبل في الوضع العادي بالنسبة للملف الخارجي
# يضيفها في النافذة بشكل افقي سواء نص او زر ...

# الملف الخارجي لازم يكون بنفس اسم الكلاس لكن باحرف صغيرة 
'''
BoxLayout:    # يمننا انشاء العديد من الادوات داخله
    Label:
        text:"MOHAMMED"
    Label:
        text: "IBRAHIM"
    Button:
        text: "FALLATAH"

'''