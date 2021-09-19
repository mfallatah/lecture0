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
