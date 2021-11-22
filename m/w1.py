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
        Data_frame.place(x=1220,y=35,width=270,height=555)

        title =Label(Data_frame, text="ادخال بيانات المستفيد",bg='#1AAECB',font=('monospace',14), fg ='white')
        title.pack(fill=X)
        
        
        l_filen =Label(Data_frame, text='رقم الملـــف', font=('monospace',13))
        l_filen.place(x=190,y=35)
        b_filen = Entry(Data_frame,bd=2, justify='center')
        b_filen.place(x=60,y=35)
        
        
        
        
        l_name =Label(Data_frame, text='اسم المستفيد ', font=('monospace',13))
        l_name.place(x=190,y=70)        
        b_name = Entry(Data_frame,bd=2, justify='center')
        b_name.place(x=60,y=70)
        
        
        
        
        l_sname =Label(Data_frame, text='اســـــم الأب', font=('monospace',13))
        l_sname.place(x=190,y=105)
        b_sname = Entry(Data_frame,bd=2, justify='center')
        b_sname.place(x=60,y=105)
        
        
        
        l_fname =Label(Data_frame, text='اسم العـــائلة ', font=('monospace',13))
        l_fname.place(x=190,y=140)
        b_fname = Entry(Data_frame,bd=2, justify='center')
        b_fname.place(x=60,y=140)
        
        
        
        l_fname =Label(Data_frame, text='اسم العـــائلة ', font=('monospace',13))
        l_fname.place(x=190,y=175)
        b_fname = Entry(Data_frame,bd=2, justify='center')
        b_fname.place(x=60,y=175)
        
        
        l_idn =Label(Data_frame, text='رقــم الهـويـة', font=('monospace',13))
        l_idn.place(x=190,y=210)
        b_idn = Entry(Data_frame,bd=2, justify='center')
        b_idn.place(x=60,y=210)
        
        
        
        
        l_ssname =Label(Data_frame, text='رقم الجـوال', font=('monospace',13))
        l_ssname.place(x=190,y=245)
        b_ssname = Entry(Data_frame,bd=2, justify='center')
        b_ssname.place(x=60,y=245)
        
        
        
        l_nat = Label(Data_frame, bg='white', text=' الجنــــسية',font=('monospace',13))
        l_nat.place(x=190,y=280)
        combo_gender = ttk.Combobox(Data_frame,width=17) # عمل صندوق اختيار
        combo_gender['value']=('سعودي','غير سعودي') # قيم صندوق الاختيار
        combo_gender.place(x=60,y=280)
        
        
      
        
        
        
        l_gender = Label(Data_frame, bg='white', text=' الجنــــــس',font=('monospace',13))
        l_gender.place(x=190,y=315)
        r_m= Radiobutton(Data_frame,text='ذكر',bg='white',value=1)
        r_m.place(x=140,y=315)

        r_f= Radiobutton(Data_frame,text='انثى', bg='white',value=2)
        r_f.place(x=70,y=315)

        
      


        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1200,y=595,width=255,height=300)


        tree_v1 = Frame(self.root, bg='white')
        tree_v1.place(x=935, y=100 ,width=250, height=700)

        





        search_frame = Frame(self.root, bg = 'white')
        search_frame.place(x=5,y=35,width=1180,height=50)




root = Tk()
ob = Binifit(root)
root.mainloop()





""""
        l_nat = Label(Data_frame, bg='white', text=' الجنــــسية',font=('monospace',13))
        l_nat.place(x=190,y=210)
        r_ns= Radiobutton(Data_frame,text='سعودي',bg='white',value=1)
        r_ns.place(x=125,y=210)

        r_nn= Radiobutton(Data_frame,text='غير سعودي', bg='white',value=2)
        r_nn.place(x=50,y=210)
        
        ---------------------------------------------------------
        v = IntVar() # عشان يشيل الاختيار عن اخيارين ويخلينا احنا نختار

        rdom= Radiobutton(frm,text='Male',value=1,variable=v)
        rdom.pack()

        rdof= Radiobutton(frm,text='Fmale',value=2,variable=v)
        rdof.pack()

        # اذا ما حطينا كلمة فاليو الاختيار يكون على الاثنين
        # نسوي الدالة والزر اللي ترجع القيمة
        def f ():
        print (v.get())
    
        Button(frm,text='OK',command=f).pack()

"""
