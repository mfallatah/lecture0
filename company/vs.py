from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox # عشان الكومبو بوكس في السؤال الامني

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Window")
        self.root.geometry('1350x700+0+0')
        self.root.config(bg="black")
        
        # لاضافة صورة رمزية في اعلى طرف النموذج
        #self.root.iconbitmap('c:/Users/DAR-S19021/Desktop/company/images/te.ico')
        
        # === Bg image ==
        # هنا اضفنا الخلفية ولاضافتها اضفنا السطر الثاني اللي يستدعي الصور من المكتبة
        # x = المسافة من بداية الصفحة في اليمين
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


        # === Left image ==
        self.left=ImageTk.PhotoImage(file="images/b3.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        # == نموذج التسجيل ==
        frame1=Frame(self.root,bg="white")# الاطار اللي نضع فيه ليبل المدخلات
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1, text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=30,y=30)
        
        
        f_name=Label(frame1, text="First Name",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=30,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=33,y=130,width=250)

        l_name=Label(frame1, text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        # رقم الجوال والايميل نسخنا الاثنين اللي فوق وعدلنا عليها        

        contact=Label(frame1, text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=30,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=33,y=200,width=250)

        email=Label(frame1, text="Email",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)



        # الصف الثالث من المدخلات السؤال الامني هنا اضفنا كومبو بوكس ولازم نضيفه من التكينتر
      
        question=Label(frame1, text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=30,y=240)
        #صندوق الاختيار  
        self.cmp_ques=ttk.Combobox(frame1,font=("times new roman",12),state='readonly',justify=CENTER) # ريد اونلي وجست فاي ماتخلي المستخدم يكتب في الصندوق وتخلي الخط في النص
        self.cmp_ques['values']=("Select","Your Middel Name","Your Birth Place","Your First Car","your best frind name")
        self.cmp_ques.place(x=33,y=270,width=250)
        self.cmp_ques.current(0) # تثبت اول قيمة في الفاليو في مربع الاختيار

        answer=Label(frame1, text="Answer",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        # الصف الرابع للباسورد
        password=Label(frame1, text="Password",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=30,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=33,y=340,width=250)

        cpassword=Label(frame1, text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="silver").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #--Terms  checkbox
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",10)).place(x=30,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/reg.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=30,y=420)
        
        btn_login=Button(self.root,text="Sign in",font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=150)
        
        copyright=Label(frame1, text="Designed By Mohammed Fallatah",font=("times new roman",8,"bold"),bg="white",fg="black").place(x=30,y=480)

    
    # سوينا ديف واضفنا هذه الاسطر ليطبع القيمة التي في المدخلات بعد مانضغط زر التسجيل
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmp_ques.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" :
            messagebox.showerror("Error","All Filed Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password And Cpassword Not Matching",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Plase agree Terms And Conditions",parent=self.root)
        else:
            messagebox.showinfo("success","Register Successful",parent=self.root)

        """
        هنا لو نبغى نطبع المدخلات نشيل كلمة اف  وكل الشروط
        self.txt_lname.get(),
        self.txt_contact.get(),
        self.txt_email.get(),
        self.cmp_ques.get(),
        self.txt_answer.get(),
        self.txt_password.get(),
        self.txt_cpassword.get())
        """
root=Tk()
obj = Register(root)
root.mainloop()

#https://www.youtube.com/watch?v=quSM7kHEy9k
