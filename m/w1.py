from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql



class Binifit:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1500x900+1+1')
        self.root.title('برنامج ادارة المسستفيدين')
        self.root.configure(background='silver')
        self.root.resizable(False,False)
        title=Label(self.root, text='نظام تسجيل وادارة المستفيدين', bg='#1AAECB', font=('monospace',14), fg='white')
        title.pack(fill=X)


        Data_frame = Frame(self.root, bg='white')
        Data_frame.place(x=1240,y=35,width=255,height=555)



        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1240,y=595,width=255,height=300)





        search_frame = Frame(self.root, bg = 'white')
        search_frame.place(x=5,y=35,width=1228,height=100)




root = Tk()
ob = Binifit(root)
root.mainloop()

