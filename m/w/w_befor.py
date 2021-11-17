from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

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
        self.se_txt=StringVar() # حق البحث
        self.se_by=StringVar()
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
        add_btn = Button(btn_Frame, text='اضافة المستفيد', bg='#85929E', fg='white', command=self.add_binifit)
        add_btn.place(x=33,y=44,width=150,height=30)

        delt_btn = Button(btn_Frame, text='حذف المستفيد', bg='#85929E', fg='white',command=self.delete)
        delt_btn.place(x=33,y=80,width=150,height=30)

        update_btn = Button(btn_Frame, text='تعديل بيانات المستفيد', bg='#85929E', fg='white', command=self.update)
        update_btn.place(x=33,y=115,width=150,height=30)

        clear_btn = Button(btn_Frame, text='افراغ الحقول', bg='#85929E', fg='white',command=self.clear)
        clear_btn.place(x=33,y=150,width=150,height=30)

        about_btn = Button(btn_Frame, text='المطور', bg='#85929E', fg='white',command=self.about)
        about_btn.place(x=33,y=185,width=150,height=30)

        exit_btn = Button(btn_Frame, text='اغلاق البرنامج', bg='#85929E', fg='white', command=root.quit)
        exit_btn.place(x=33,y=220,width=150,height=30)



        # -------- نظام البحث  search manage ----------
        search_Frame = Frame(self.root, bg='white')
        search_Frame.place(x=1, y=31,width=1134,height=50)

        lbl_searsh = Label(search_Frame, text='البحث عن مستفيد', bg='white')
        lbl_searsh.place(x=1034,y=12)

        combo_search = ttk.Combobox(search_Frame, justify='right',textvariable=self.se_by)
        combo_search['value']=("id","name","mobile","email")
        combo_search.place(x=880,y=12)

        search_entry = Entry(search_Frame, textvariable=self.se_txt, justify='right', bd=2)
        search_entry.place(x=740,y=13)

        se_btn = Button(search_Frame, text='بحث',bg='#3498DB', fg='white', command=self.search)
        se_btn.place(x=630,y=12,width=100, height=25)




        # ---------- Detailes    عرض النتائج والبياناا -------
        Details_Frame = Frame(self.root, bg='#F2F4F4')
        Details_Frame.place(x=1, y=82, width=1134, height=605)

        # الان نقوم بانشاء سكرول عشان لو المدخلات كثيرة نقدر نوصلها
        scroll_x = Scrollbar(Details_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Details_Frame, orient=VERTICAL)
        # ----- tree View ----------
        self.benifit_table = ttk.Treeview(Details_Frame,
        columns=('address','gender','email','mobile','fname','sname','name','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)   # هنا انشانا متغير العنوانجديد وهو متغير داخلي داخل المتغير استدعينا الاداة  Treeview وطلبنا منها تظهر في Details_Frame
        # الحقول  ل Treeview   هي اللي انشأنها لادخال بيانات المستفيدين
        # xscrollcomand and yscrollcomand = انشأناهم من السطرين
        #scroll_x = Scrollbar(Details_Frame, orient=HORIZONTAL)
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
        self.benifit_table.heading('sname', text='اسم الأب')
        self.benifit_table.heading('name', text='اسم المستفيد')
        self.benifit_table.heading('id', text='رقم الهوية')

        # التحكم بحجم الاسكرول عشان لايظهر الشريط

        self.benifit_table.column('address', width=130)
        self.benifit_table.column('gender',width=30)
        self.benifit_table.column('email',width=70)
        self.benifit_table.column('mobile',width=65)
        self.benifit_table.column('fname',width=30)
        self.benifit_table.column('sname',width=30)
        self.benifit_table.column('name',width=30)
        self.benifit_table.column('id',width=65)
        self.benifit_table.bind("<ButtonRelease-1>",self.get_cursor)






        #------ con + add  الاتصال مع قاعدة البيانات واضافتها  --------
        # انشأنا دالة اسمها (بينفيت) وسط هذه الدالة كتبنا سلف اي تقوم بتمرير البيانات من تلقاء نفسها وانشانا متغير اسمه (كون ) نستطيع تغيير اسمه , داخل هذه اللمتغير استدعينا مكتبة اسمها (باي اس كيو ال ) من هذه المكتبة هناك دالة اسمها كنكت للاتصال مع الهوست اللي هو المضيف

        self.fetch_data() # لازم نضيفها عشان تطلع البيانات في البرنامج وتمت اضافتها بعد اضافة قواعد البيانات
    def add_binifit(self): # self = تمرير البيانات من تلقاء نفسها
            con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'bini') # bini  = database name   binfit = table name  ضرورية للاتصال بقاعدة البيانات
            cur = con.cursor() # للاتصال بقاعدة البيانات
            cur.execute("insert into binfit values(%s,%s,%s,%s,%s,%s,%s,%s)",(




                                                      self.address_var.get(),
                                                      self.gender_var.get(),
                                                      self.email_var.get(),
                                                      self.mobile_var.get(),
                                                      self.fname_var.get(),
                                                      self.sname_var.get(),
                                                      self.name_var.get(),
                                                      self.id_var.get()





                                         ))
            con.commit()
            self.fetch_data() # لما تضيف طالب جديد اعرض بيانته قبل اغلاق الاتصال مع قاعدة البيانات في تري فيو
            self.clear() # تفرغ الحقول بعد اضافة المستفيد
            con.close()

    # لاظهار البيانات المضافة في نفس صفحة بالبرنامج

    def fetch_data(self):
              con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'bini')
              cur = con.cursor()
              # معنى السطر اللي تحت اختر الكل من جدول binfit
              cur.execute('select * from binfit')
              # ننشئ متغير باي اسمه
              rows = cur.fetchall() # اجلب كل البيانات
              if len (rows) !=0:
                  self.benifit_table.delete(*self.benifit_table.get_children())
                  # row = متغير نسميه اي اسمه
                  for row in rows:
                      self.benifit_table.insert("",END,values=row) # End must be cabital leters
                      # END معناها اعرض كل البيانات اللي ااضيفها في الهاية
                  con.commit()
              con.close()

    # ننشْ دالة لحذف المستفيد
    def delete(self):
        con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'bini')
        cur = con.cursor()
        cur.execute('delete from binfit where name=%s',self.dell_var.get())
        con.commit()
        self.fetch_data() # لما المستخدم يحذف ينحذف من البرنامج مباشرة مو لازم يغلق بالبرنامج
        con.close()


    # دالة افراغ الحقول
    def clear(self): # لازم نضيف اسم الدالة في امر الزر عشان تتنفذ
        self.id_var.set('')
        self.name_var.set('')
        self.sname_var.set('')
        self.fname_var.set('')
        self.mobile_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.address_var.set('')

    # دالة بمجرد ان اضغط على بيانات اي مستفيد يعرض بياناته في الحقول  13
    def get_cursor(self,ev):
        cursor_row=self.benifit_table.focus() # انشأنا متغير بهذا الاسم واستتدعيناها في منطقة تري فيو فوكس معناها لما انقر على هذه البيانات
        contents = self.benifit_table.item(cursor_row) #لا واحفظها داخل المتغير كونتنتس زايتمز العناصر اللي حددها الفوكس
        row=contents['values'] # هما انشأنا متغير اسمه رو لما المستخد ضغط على البيانات تم حفظها داخل كورسور_رو والكورسور موجود داخل الكونتنت ومهمة الرو جلب القيم في الكونتنت
        self.id_var.set(row[7]) # حسب الرقم التسلسلي في قاعدة البيانات ولما تكون بالعربي نعكسها عشان تطلع صحيحة
        self.name_var.set(row[6]) # أنشأنا متغير اسمه رو مهمته معناها يارو تاخذ القيمة اللي في الحقل 7 وتحطها في نيم _فار
        self.sname_var.set(row[5])
        self.fname_var.set(row[4])
        self.mobile_var.set(row[3])
        self.email_var.set(row[2])
        self.gender_var.set(row[1])
        self.address_var.set(row[0])



    # تعديل بيانات المستفيد من نفس الحقول بعد مانضغط على اسمه في شاشة عرض البيانات
    # نسخنا نفس دالة الاتصال بقواعد البيانات الخاصة باضافة مستفيد
    # اتصلنا بقاعدة بيانات السيرفر وقلنا له سوف نري عملية وهي تحديث بيانات المستفيدين التي ساكتبها في الحقول حسب الاي دي
    def update(self):
        con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'bini') # bini  = database name   binfit = table name  ضرورية للاتصال بقاعدة البيانات
        cur = con.cursor() # للاتصال بقاعدة البيانات
        cur.execute("update binfit set address=%s, gender=%s, email=%s, mobile=%s, fname=%s, sname=%s, name=%s where id=%s",(




                                                      self.address_var.get(),
                                                      self.gender_var.get(),
                                                      self.email_var.get(),
                                                      self.mobile_var.get(),
                                                      self.fname_var.get(),
                                                      self.sname_var.get(),
                                                      self.name_var.get(),
                                                      self.id_var.get()





                                         ))
        con.commit()
        self.fetch_data() # لما تضيف طالب جديد اعرض بيانته قبل اغلاق الاتصال مع قاعدة البيانات في تري فيو
        self.clear() # تفرغ الحقول بعد اضافة المستفيد
        con.close()




    def search(self): # نسخنا دالة fttch all
            con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'bini')
            cur = con.cursor()
            # معنى السطر اللي تحت اختر الكل من جدول binfit
            cur.execute("select * from binfit where " +
            str(self.se_by.get()) +" LIKE '%"+str(self.se_txt.get())+"%'")

            # ننشئ متغير باي اسمه
            rows = cur.fetchall() # اجلب كل البيانات
            if len (rows) !=0:
                  self.benifit_table.delete(*self.benifit_table.get_children())
            # row = متغير نسميه اي اسمه
                  for row in rows:
                      self.benifit_table.insert("",END,values=row) # End must be cabital leters
            # END معناها اعرض كل البيانات اللي ااضيفها في الهاية
                  con.commit()
            con.close()


    def about(self):
        messagebox.showinfo("Developed By Mohammed Fallaatah","برنامج ادارة المستفيدين")



root = Tk()
ob = Benifit(root)
root.mainloop()

# https://www.youtube.com/watch?v=y2JbutNRSQo
# ttk used for combobox , entry, label
# https://www.youtube.com/watch?v=4ygq2fJa4ig
