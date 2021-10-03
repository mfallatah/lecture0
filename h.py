'''
a= ['Apple','Mango','orange']# list
b = (91,2,3) # tuple
fow = {'a', 'b', 'c', 'd'} #set
abl = {'a' : 'Apple', 'b' : 'Mango', 'c' :'Orang'} #dectonary

print(a)
print(b)
print(fow)
print(abl)
'''


'''
x = "moahmmed"
print(x.upper())

يحول الحروف كلها الى حروف كبيرة
'''

'''
s = {1,2,3,4,5,6,6,6} 
print(type(s)) # نوع القوس بريسس ويطبع مجموعات
print(s) # يطبع العناصر اللي داخل s وما يطبع العناصر المتكررة 
'''






''''
x = "moahmmed"
print(x.lower())
يحول الحروف الى صغيرة
'''

"""
for x in range (30):
    print(x)
else:
    print("Your have tow days of")
"""

"""
a = 5
print(type(a)) # لمعرفة نوع المدخل

"""


"""
a = 5
print(isinstance(a,str)) #  لمعرفة نوع المدخل"""
"""
a = 4+2j
print(type(a))# يمكننا طباعة الارقام المعقدة واللتي تحتوي على ارقام وحروف 

"""

""""
b = [1,2,3,4,'mo',4+3,6]
print(b[::]) # يطبعها كلها 
"""

""""
c = [1,2,3,4,5,'mf',6]
print(c[::-1])# يطبعها بالعكس
"""

"""
c = [1,2,3,4,5,'mf',6]
print(c[::-2]) #  يطبعها بالعكس ياخذ خانة ويلغي خانة 
"""




"""
a =[1,2,3,4,5,'mohammed', 4+3]
print(a) # طباعة قائمة حتى لوكانت انواع البيانات مختلفة

"""

"""

"""

"""
"""

"""
"""

"""

"""

"""
"""
"""

import tkinter
from tkinter import ttk
form = tkinter.Tk()
form.geometry('600x400')
lbl1 = ttk.Label(form , text = 'MOHAMMED')
lbl2 = ttk.Label(form , text = 'IBRAHIM')
lbl3 = ttk.Label(form , text = 'FALLATAH')
lbl3.config(background='navy',foreground='lightblue',font = ('impact',50),padding =20)
lbl2.config(background='yellow',foreground='lightblue',font = ('impact',30),padding =(10,20,30,40))

lbl1.pack()
lbl2.pack()
lbl3.pack()
form.mainloop()
input ('Press Enter')
"""
8:16