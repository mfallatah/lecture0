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
        Data_frame.place(x=1200,y=35,width=295,height=555)

        title =Label(Data_frame, text="ادخال بيانات المستفيد",bg='#1AAECB',font=('monospace',14), fg ='red')
        title.pack(fill=X)



        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1200,y=595,width=255,height=300)


        tree_v1 = Frame(self.root, bg='white')
        tree_v1.place(x=935, y=100 ,width=250, height=700)

        





        search_frame = Frame(self.root, bg = 'white')
        search_frame.place(x=5,y=35,width=1180,height=50)




root = Tk()
ob = Binifit(root)
root.mainloop()
