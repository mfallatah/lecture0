from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

# هذا  كله متعلق بالنافذة الرئيسية
win = Tk() # النافذة الرئيسية
win.geometry('1200x800')
win.resizable(False,False) # لمنع التحكم في حجم الشاشة
win.title("صفحة تسجيل البيانات")

T1 = Label(win, text='صفحة تسجيل مستحق ', fg ='gold', bg='black', font=('tajwal', 16,'bold') )
T1.pack(fill ='x') # fill = x  تجعل خلفية النص كلها باللون المحدد اذا شللناها يتكون الخلفية بحدود النص فقط



# الان نضيف الفريم الاول ويحتوي على المعلومات الاساسية
F1 = Frame(win, width= 1190, height=250, bg='#00bfff')
F1.pack()

# نص الاسم
lb1 = Label(F1, text='الإسم الأول', bg='#00bfff', fg='white',font=('tajwal',12,'bold'))
lb1.place(x=1110 ,y= 10)

E1 = Entry(F1, font=('tajwal', 12))
E1.place(x=920, y=10)

# نص الاسم
lb2 = Label(F1, text='الإسم الثاني', bg='#00bfff', fg='white',font=('tajwal',12,'bold'))
lb2.place(x=850 ,y= 10)


# نص الاسم
lb3 = Label(F1, text='الإسم الثالث', bg='#00bfff', fg='white',font=('tajwal',12,'bold'))
lb3.place(x=700 ,y= 10)

# نص الاسم
lb4 = Label(F1, text='اللقب', bg='#00bfff', fg='white',font=('tajwal',12,'bold'))
lb4.place(x=500 ,y= 10)

b1 = Button(F1, )




# الان نضيف الفريم الاول ويحتوي على المعلومات الاساسية
F2 = Frame(win, width= 1190, height=250, bg='#0080ff')
F2.pack()



# الان نضيف الفريم الاول ويحتوي على المعلومات الاساسية
F3 = Frame(win, width= 1190, height=250, bg='#00bfff')
F3.pack()




win.mainloop()


# https://www.youtube.com/watch?v=FBa8EWgUDBc
