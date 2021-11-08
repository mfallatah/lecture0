from tkinter import *
from tkinter import ttk

class Benifit:
    # انشاء نافذة البرنامج
    def __init__(self,root):
        self.root= root
        self.root.geometry('1350x690+1+1')
        self.root.title('برنامج ادارة الوقف')
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title = Label(self.root, text="نظام تسجيل المستفيدين" , bg = '#1AAECB', font=('monospace',14), fg='white')
        title.pack(fill=X)


        #---------------- VARIABLES    المتغيرات ------------
        # هذه المتغيرات من اجل استدعائها في البرمجة
        self.id_var=StringVar() # مو لازم نكتب var   وممكن نكتب اي اسم
        self.name_var=StringVar()
        self.sname_var=StringVar()
        self.fname_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.se_var=StringVar() # حق البحث
        self.dell_var=StringVar() #










        # ------------ ادوات التحكم بالبرنامج ---------------
        Manage_Frame = Frame(self.root, bg='white')
        Manage_Frame.place(x=1137,y=30,width=210,height=400)

        lbl_ID = Label(Manage_Frame, text=' رقم الهوية', bg='white')
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame, textvariable=self.id_var, bd=2,justify='center')
        ID_Entry.pack()


        lbl_name = Label(Manage_Frame, bg='white', text='اسم المستفيد') # bg = لون الخلفية
        lbl_name.pack()
        name_entry = Entry(Manage_Frame, textvariable=self.name_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        name_entry.pack()

        lbl_sname = Label(Manage_Frame, bg='white', text='اسم الأب')
        lbl_sname.pack()
        sname_entry = Entry(Manage_Frame, textvariable=self.sname_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        sname_entry.pack()

        lbl_fname = Label(Manage_Frame, bg='white', text='اللقب')
        lbl_fname.pack()
        fname_entry = Entry(Manage_Frame, textvariable=self.fname_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        fname_entry.pack()

        lbl_mnum = Label(Manage_Frame, bg='white', text='رقم الجوال')
        lbl_mnum.pack()
        mnum_entry = Entry(Manage_Frame, textvariable=self.mobile_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        mnum_entry.pack()

        lbl_email = Label(Manage_Frame, bg='white', text='البريد الألكتروني')
        lbl_email.pack()
        email_entry = Entry(Manage_Frame, textvariable=self.email_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        email_entry.pack()

        lbl_gender = Label(Manage_Frame, bg='white', text=' الجنس')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var) # عمل صندوق اختيار
        combo_gender['value']=('ذكر','انثى') # قيم صندوق الاختيار
        combo_gender.pack()

        lbl_addres = Label(Manage_Frame, bg='white', text='عنوان المستفيد')
        lbl_addres.pack()
        addres_entry = Entry(Manage_Frame, textvariable=self.address_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        addres_entry.pack()

        # حذف المستفيد
        lbl_del = Label(Manage_Frame, bg='white', fg='red', text='حذف المستفيد')
        lbl_del.pack()
        del_entry = Entry(Manage_Frame, textvariable=self.dell_var, bd=2, justify='center')  # bd = سماكة الاطار خول الفريم
        del_entry.pack()





        # ------ الازرار  Buttons --------
        btn_Frame = Frame(self.root,bg='white')
        btn_Frame.place(x=1137,y=435,width=210, height=253) # عرض الفريم اخذنا نفس عرض الفريم الحاص بادخال المعلومات ونفس مسافة البعد  عشان يكونو  تحت بعض

        # اضافة عنوان للوحة التحكم
        title1 = Label(btn_Frame, text='لوحة التحكم', font=('Deco',14), fg='white', bg='#2980B9')
        title1.pack(fill=X)# x = يلون خلفية العنوان باللون اللي احطه فوق في الب جي

        # اضافة الازارير
        add_btn = Button(btn_Frame, text='اضافة المستفيد', bg='#85929E', fg='white')
        add_btn.place(x=33,y=44,width=150,height=30)

        delt_btn = Button(btn_Frame, text='حذف المستفيد', bg='#85929E', fg='white')
        delt_btn.place(x=33,y=80,width=150,height=30)

        update_btn = Button(btn_Frame, text='تعديل بيانات المستفيد', bg='#85929E', fg='white')
        update_btn.place(x=33,y=115,width=150,height=30)

        clear_btn = Button(btn_Frame, text='افراغ الحقول', bg='#85929E', fg='white')
        clear_btn.place(x=33,y=150,width=150,height=30)

        about_btn = Button(btn_Frame, text='المطور', bg='#85929E', fg='white')
        about_btn.place(x=33,y=185,width=150,height=30)

        exit_btn = Button(btn_Frame, text='اغلاق البرنامج', bg='#85929E', fg='white')
        exit_btn.place(x=33,y=220,width=150,height=30)



        # -------- نظام البحث  search manage ----------
        search_Frame = Frame(self.root, bg='white')
        search_Frame.place(x=1, y=31,width=1134,height=50)

        lbl_searsh = Label(search_Frame, text='البحث عن مستفيد', bg='white')
        lbl_searsh.place(x=1034,y=12)

        combo_search = ttk.Combobox(search_Frame, justify='right')
        combo_search['value']=('رقم الهوية','اسم المستفيد','اللقب','رقم الجوال','البريدالالكتروني')
        combo_search.place(x=880,y=12)

        search_entry = Entry(search_Frame, textvariable=self.se_var, justify='right', bd=2)
        search_entry.place(x=740,y=13)

        se_btn = Button(search_Frame, text='بحث',bg='#3498DB', fg='white')
        se_btn.place(x=630,y=12,width=100, height=25)




        # ---------- Detailes    عرض النتائج والبياناا -------
        Details_Frame = Frame(self.root, bg='#F2F4F4')
        Details_Frame.place(x=1, y=82, width=1134, height=605)

        # الان نقوم بانشاء سكرول عشان لو المدخلات كثيرة نقدر نوصلها
        scroll_x = Scrollbar(Details_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Details_Frame, orient=VERTICAL)
        # ----- tree View ----------
        self.benifit_table = ttk.Treeview(Details_Frame,
        columns=('address','gender','email','mobile','fname','ffname','name','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)   # هنا انشانا متغير العنوانجديد وهو متغير داخلي داخل المتغير استدعينا الاداة  Treeview وطلبنا منها تظهر في Details_Frame
        # الحقول  ل Treeview   هي اللي انشأنها لادخال بيانات المستفيدين
        # xscrollcomand and yscrollcomand = انشأناهم من السطرين  scroll_x = Scrollbar(Details_Frame, orient=HORIZONTAL)
        #scroll_y = Scrollbar(Details_Frame, orient=VERTICAL)
        self.benifit_table.place(x=18,y=1, width=1130,height=587) # 18-1134 = 1119
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.benifit_table.xview) # اذا ماظهر الاسكورول بالكود اللي فوق نكتب هذي السطرين بدالهم
        scroll_y.config(command=self.benifit_table.yview)

        # كتابة اسماء الحقول في TREE Treeview  واسمي الحقول اللي انشأتها
        self.benifit_table['show']='headings'
        self.benifit_table.heading('address', text='عنوان المستفيد') # هذا هو headings  اضافة العنواين في ال treewiew
        self.benifit_table.heading('gender', text='جنس المستفيد')
        self.benifit_table.heading('email', text='البريد الالكتروني')
        self.benifit_table.heading('mobile', text='رقم الجوال')
        self.benifit_table.heading('fname', text='اللقب')
        self.benifit_table.heading('ffname', text='اسم الأب')
        self.benifit_table.heading('name', text='اسم المستفيد')
        self.benifit_table.heading('id', text='رقم الهوية')
        # التحكم بحجم الاسكرول عشان لايظهر الشريط
        self.benifit_table.column('address', width=130)
        self.benifit_table.column('gender',width=30)
        self.benifit_table.column('email',width=70)
        self.benifit_table.column('mobile',width=65)
        self.benifit_table.column('fname',width=30)
        self.benifit_table.column('ffname',width=30)
        self.benifit_table.column('name',width=30)
        self.benifit_table.column('id',width=65)










root = Tk()
ob = Benifit(root)
root.mainloop()



# https://www.youtube.com/watch?v=y2JbutNRSQo
# ttk used for combobox , entry, label
# https://www.youtube.com/watch?v=4ygq2fJa4ig
