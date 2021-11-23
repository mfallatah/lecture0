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
        Data_frame.place(x=1220,y=35,width=270,height=510)

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
        
        
        
        
        
        l_idn =Label(Data_frame, text='رقــم الهـويـة', font=('monospace',13))
        l_idn.place(x=190,y=175)
        b_idn = Entry(Data_frame,bd=2, justify='center')
        b_idn.place(x=60,y=175)



        l_idexdate =Label(Data_frame, text='تاريخ الانتهاء', font=('monospace',13))
        l_idexdate.place(x=190,y=210)
        l_idexdate = Entry(Data_frame,bd=2, justify='center')
        l_idexdate.place(x=60,y=210)
        
        
        
        
        l_ssname =Label(Data_frame, text='رقم الجـوال', font=('monospace',13))
        l_ssname.place(x=190,y=245)
        b_ssname = Entry(Data_frame,bd=2, justify='center')
        b_ssname.place(x=60,y=245)
        

        l_acount =Label(Data_frame, text='رقم الحساب', font=('monospace',13))
        l_acount.place(x=190,y=280)
        b_acount = Entry(Data_frame,bd=2, justify='center')
        b_acount.place(x=60,y=280)



        l_fname =Label(Data_frame, text='اسم العـــائلة ', font=('monospace',13))
        l_fname.place(x=190,y=315)
        b_fname = Entry(Data_frame,bd=2, justify='center')
        b_fname.place(x=60,y=315)
        
        
        
        l_nat = Label(Data_frame, bg='white', text=' الجنــــسية',font=('monospace',13))
        l_nat.place(x=190,y=350)
        combo_gender = ttk.Combobox(Data_frame,width=17) # عمل صندوق اختيار
        combo_gender['value']=('سعودي','غير سعودي') # قيم صندوق الاختيار
        combo_gender.place(x=60,y=350)



        
        
        
        
        l_gender = Label(Data_frame, bg='white', text=' الجنــــــس',font=('monospace',13))
        l_gender.place(x=190,y=385)
        r_m= Radiobutton(Data_frame,text='ذكر',bg='white',value=1)
        r_m.place(x=140,y=385)

        r_f= Radiobutton(Data_frame,text='انثى', bg='white',value=2)
        r_f.place(x=70,y=385)

        
        #----------------------------------------------------------------------------------------------------------------


        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1220,y=550,width=270,height=300)

        title1 =Label(manage_frame, text="التـــــابعين",bg='#1AAECB',font=('monospace',14), fg ='white')
        title1.pack(fill=X)

        l_tmen =Label(manage_frame, text="الذكور",font=('monospace',14))
        l_tmen.place(x=137,y=30,width=133)

        l_twomen =Label(manage_frame,bd=2, text="الانـــاث",font=('monospace',14))
        l_twomen.place(x=0,y=30,width=135)


        t1=Entry(manage_frame,bd=2, justify='center')
        t1.place(x=137,y=60,width=133)

        t2=Entry(manage_frame,bd=2, justify='center')
        t2.place(x=137,y=80,width=133)

        t3=Entry(manage_frame,bd=2, justify='center')
        t3.place(x=137,y=100,width=133)

        t4=Entry(manage_frame,bd=2, justify='center')
        t4.place(x=137,y=120,width=133)

        t5=Entry(manage_frame,bd=2, justify='center')
        t5.place(x=137,y=140,width=133)

        t6=Entry(manage_frame,bd=2, justify='center')
        t6.place(x=137,y=160,width=133)

        t7=Entry(manage_frame,bd=2, justify='center')
        t7.place(x=137,y=180,width=133)

        t8=Entry(manage_frame,bd=2, justify='center')
        t8.place(x=137,y=200,width=133)

        t9=Entry(manage_frame,bd=2, justify='center')
        t9.place(x=137,y=220,width=133)

        t10=Entry(manage_frame,bd=2, justify='center')
        t10.place(x=137,y=240,width=133)

        t10=Entry(manage_frame,bd=2, justify='center')
        t10.place(x=2,y=60,width=133)

        t11=Entry(manage_frame,bd=2, justify='center')
        t11.place(x=2,y=80,width=133)

        t12=Entry(manage_frame,bd=2, justify='center')
        t12.place(x=2,y=100,width=133)

        t13=Entry(manage_frame,bd=2, justify='center')
        t13.place(x=2,y=120,width=133)

        t14=Entry(manage_frame,bd=2, justify='center')
        t14.place(x=2,y=140,width=133)

        t15=Entry(manage_frame,bd=2, justify='center')
        t15.place(x=2,y=160,width=133)

        t16=Entry(manage_frame,bd=2, justify='center')
        t16.place(x=2,y=180,width=133)

        t17=Entry(manage_frame,bd=2, justify='center')
        t17.place(x=2,y=200,width=133)

        t18=Entry(manage_frame,bd=2, justify='center')
        t18.place(x=2,y=220,width=133)

        t19=Entry(manage_frame,bd=2, justify='center')
        t19.place(x=2,y=240,width=133)

        t20=Entry(manage_frame,bd=2, justify='center')
        t20.place(x=2,y=240,width=133)



        #---------------------------------------------------------
        #TREE VIEW


        tree_v1 = Frame(self.root, bg='white')
        tree_v1.place(x=10, y=100 ,width=1200, height=750)

        scroll_x = Scrollbar(tree_v1, orient=HORIZONTAL)
        scroll_y = Scrollbar(tree_v1, orient=VERTICAL)

        self.binifit_tabel= ttk.Treeview(tree_v1,
        columns=('t20','t19','t18','t17','t16','t15','t14','t13','t12','t11','t10','t8','t9','t8','t7','t6','t5','t4','t3','t2','t1','gender','nationality','acountn','mobile','iddate','idnum','name','fname','sname','name','filen'),
                 xscrollcommand=scroll_x.set,
                 yscrollcommand=scroll_y.set)

        self.binifit_tabel.place(x=18,y=1,width=1180  ,height=700)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.binifit_tabel.xview) # اذا ماظهر الاسكورول بالكود اللي فوق نكتب هذي السطرين بدالهم
        scroll_y.config(command=self.binifit_tabel.yview)
        
        
        self.binifit_tabel['show']='headings'
        self.binifit_tabel.heading('filen', text='رقم الملف')
        self.binifit_tabel.heading('name', text='الاسم')
        self.binifit_tabel.heading('sname', text='اسم الاب')
        self.binifit_tabel.heading('fname', text='اللقب')



        # التحكم بحجم الاسكرول عشان لايظهر الشريط

        self.binifit_tabel.column('filen', width=60)

         
        











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

# https://www.pythontutorial.net/tkinter/tkinter-treeview/
