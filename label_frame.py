
from tkinter import *


ws = Tk()
ws.title(string='')
ws.geometry('400x900')




frame = LabelFrame(ws,text='PythonGuides',bg='#f0f0f0',font=(20))
frame.pack(expand=True, fill=BOTH)
Button(frame,text='Submit').pack()
lb = Listbox(frame)
lb.insert(1, "MADDINAH")
lb.insert(2, "MAKKAH")
lb.insert(3, "JEDDAH")
lb.pack()


framee = LabelFrame(ws,text='Mohammed', bg='#1E90FF', font=(20), bd= 8)
framee.pack(expand=True, fill=BOTH)
Button(framee,text='Submit').pack()
rd=Radiobutton(framee, text="Male")
rd1=Radiobutton(framee, text="Fmale")
rd.pack()
rd1.pack( anchor = W)   # anchor = للتحكم بمكان الايقونة يمين او يسار الطبيعي تكون في الوسط


frameee = LabelFrame(ws,text='FALLATAH', bg='#f0f0f0', font=(20))
frameee.pack(expand=True, fill=BOTH)
Button(frameee,text='Submit').pack()


scrbar= Scrollbar(frameee)
scrbar.pack(side = RIGHT, fill = Y)

mylist=Listbox(frameee, yscrollcommand = scrbar.set)
for line in range(100):
    mylist.insert(END, "This is line number" + str(line))

mylist.pack(side = LEFT, fill = BOTH)
scrbar.config(command = mylist.yview)





frame1 = LabelFrame(ws,text='Spinbox', bg='#f0f0f0', font=(20))
frame1.pack(expand=True, fill=BOTH)
Button(frame1,text='Submit').pack()
sb =Spinbox(frame1,text='N.of car', from_=0, to=10)
sb.pack()


# Tkinter Message
var1 = StringVar()
label = Message(frame1, textvariable=var1, relief=RAISED)
var1.set("alomost done")
label.pack()


# Entyr
label_entry = Label(frame1, text=('user name'))
label_entry.pack(side =LEFT)
E1 = Entry(frame1, bd =2) # سماكة الاطاار حول صندوق المدخلات
E1.pack(side = LEFT)


ws.mainloop()



# العناوين الرئيسية لا تظهر الا اذا اضفنا labeleframe
# bd = سماكة الاطار خل الفريم
# bg = لون خلفية الفريم






#_______________________________

# برمجة صندوق الاختيار في الفرييم الثاني

#def sel():
 #  selection = "You selected the option " + str(var.get())
  # label.config(text = selection)

#var=IntVar()
#rd=Radiobutton(framee, text="Male", variable=var, value=1, command=sel)
#rd1=Radiobutton(framee, text="Fmale", variable=var, value=2, command=sel)
#------------


# https://www.tutorialspoint.com/python/tk_button.htm
