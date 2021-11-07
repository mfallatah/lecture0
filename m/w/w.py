from tkinter import *

class student:
    # انشاء نافذة البرنامج
    def __init__(self,root):
        self.root= root
        self.root.geometry('1350x690+1+1')
        self.root.title('برنامج ادارة الوقف')
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title = Label(self.root, text="نظام تسجيل المستفيدين" , bg = '#1AAECB', font=('monospace',14), fg='white')
        title.pack(fill=X)


    # ادوات التحكم بالبرنامج
        Manage_Frame = Frame(self.root, bg='white')
        Manage_Frame.place(x=1137,y=30,width=210,height=400)
        lbl_ID = Label(Manage_Frame, text='الرقم التسلسلي', bg='white')
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame, bd=2)
        ID_Entry.pack()
        lbl_name = Label(Manage_Frame, bg='white', text='اسم الطالب')
        lbl_name.pack()
        name_entry = Entry(Manage_Frame, bd=2)
        name_entry.pack()

root = Tk()
ob = student(root)
root.mainloop()



# https://www.youtube.com/watch?v=y2JbutNRSQo
