from tkinter import Button, Tk
from tkinter import Toplevel# لاضافة عناصر ادخال 
from tkinter import ttk # اضفناها عشان عناصر ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Listbox
from tkinter import Frame


def strVar():
    return StringVar()

def intVar():
    return IntVar()

def boolVar ():
    return BooleanVar()

# دالة لعمل فورم
def form (geometry='350x200',title='', is_center=True): # we adde tkinter Tk for this
    f= Tk()
    f.geometry(geometry)
    f.title(title) # لاضافة العنوان عن طريق نفس سطر الجيومتري نعرفه فوق في الجيومتري وهنا
    if is_center:tkcenter(f)
    return f

def toplevel (geometry='350x200',title='', is_center=True): # we adde tkinter Tk for this
    f= Toplevel()
    f.geometry(geometry)
    f.title(title) # لاضافة العنوان عن طريق نفس سطر الجيومتري نعرفه فوق في الجيومتري وهنا
    if is_center:tkcenter(f)
    return f

# دالة لعل فريم
def frame (form,bg=None) :
    if bg != None: 
        return Frame(form,bg=bg)
    else: 
        return Frame(form)


# انشاء زر سهل 
def button (form,text='Button',command=None):
    btn= ttk.Button(form,text=text)
    btn.config(command=command)
    return btn

# انشاء ليبل
def label (form,text='Label'):# الاشياء الاساسية اللي في الليبل انه يكون في الفورم والنص اللي يظهر فيه اذا ما حددناه 
    return ttk.Label(form,text=text)
# انشاء انتري او مربع ادخال
def textbox (form,is_number_only=False):
    
    def number_only (text):
         if str.isdigit(text):# fixed
             return True
         elif text is '': # يمسح اخر رقم
              return True
         else:
              return False
    reg_fun = form.register(number_only) #reg_fun not fixed
    txt = ttk.Entry(form)
    if is_number_only:

        txt.config(validate='key',validatecommand=(reg_fun, '%P'))
    return txt


# راديو تستقبل مني الفورم اللي حاتنضاف عليه والنص اللي حاينكتب عليها لو ماعينته يعين الديفولت
# اي شي في الاقواس اللي بعد الدالة لو انا ما عينته حايعين هوا اللي بين القوسين
def radio (form, text='Radio',value =0, variable=None):
    rdo = ttk.Radiobutton(form,text=text,value=value)
    if variable != None :
        rdo.config(variable=variable)
    return rdo

#دالة لعمل صندوق اختيار
def checkbox(form,text='CheckBox',variable=None):
    cbx = ttk.Checkbutton(form,text=text)
    if variable != None:
        cbx.config(variable=variable)
    return cbx

# دالة قائمة منسدلة
def combobox (form,values=None,readonly=False):
    cbx= ttk.Combobox(form)
    if values != None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly')
    return cbx

# صندوق قائمة يضاف في التولز مع استدعاء
#from tkinter import Listbox

def listbox (form,values=None) :
    lbx = Listbox(form) # لو القيم اترسلت 
    if values != None:
        i = 0
        for x in values:
            lbx.insert(i,x)# حانسوي لوب عشان الاندكس
            i+=1 # نزود واحد على الاندكس
    return lbx


    

# دالة لتوسيط الفورم في منصف الصفحة 
def tkcenter (form):
    form.update()
    fw = form.winfo_width()          #عرض الفورم    
    fh = form.winfo_height()         #طول الفورم
    sw = form.winfo_screenwidth()    #عرض الشاشة
    sh = form.winfo_screenheight()   #طول الشاشة
    x  = (sw - fw )/2
    y  = (sh-fh)/2 - 45
    form.geometry( '%dx%d+%d+%d' % ( fw, fh, x, y ))
    
# يخلي كل الادوات في الخلفية لها نفس الخصائص بالنسبة لادوات تكينتر
#درس 176
# ctrls = كل الادوزات اللي في الفورم

# دالة للتحكم بالوانالخلفية 
def bgall (form,bg):
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    my = ttk.Style() # my not fixed
    my.configure('TRadiobutton',background=bg)
    my.configure('TCheckbutton',background=bg)
    for c in ctrls: # ctls is fixed
        if c.winfo_class()=='Frame' : bgall(c,bg)
        try:                     # تراي واكسبت معناها اذا لقيت الخاصية طبقها اذا  مالقيتهااتجاهلها
            c['background']=bg
        except:
            pass


def fgall (form,fg):
    form.update
    ctrls = form.winfo_children()
    my = ttk.Style()
    my.configure('TButton',foreground=fg)
    my.configure('TRadiobutton',foreground=fg)
    my.configure('TCheckbutton',foreground=fg)
    for c in ctrls:
        if c.winfo_class()=='Frame' : fgall(c,fg)
        try:
            c['foreground']=fg
        except:
            pass
            

# هذي دالة للخطوط
def fontall (form,font): # font all not fixed
    form.update()
    ctrls = form.winfo_children() #ctrls collect all elemnt in the form not fixed
    my = ttk.Style()
    my.configure('TButton',font=font)
    my.configure('TRadiobutton',font=font)
    my.configure('TCheckbutton',font=font)
    
    for c in ctrls: # c  اختصار لكنترولز وهو يلف على الدالة
        if c.winfo_class()=='Frame' : fontall(c,font) # مهمة فقط اا كان شغلنا على اكثر من فريم شرحها فيديو 211
        try:
            c['font']=font
        except:
            pass
             

        
def msgbox(text):
       messagebox.showinfo('',text)

# اختصار ل يس او نو  اول شي اسوي استدعاء فوق للمسج بوكس
# ثم اكتب الدالة
def msgask (text):
    return messagebox.askyesno('',text)

def inbox (text,is_number_only=False):
    f = Toplevel()
    f.title(text)
    f.geometry('400x150')
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f,text=text,font='None 15').pack(pady=10)
    sv = StringVar()
    
    def number_only (text):
         if str.isdigit(text):# fixed
             return True
         elif text is '': # يمسح اخر رقم
              return True
         else:
              return False
    reg_fun = f.register(number_only) #reg_fun not fixed

     
    txt = ttk.Entry(f,font='None 15',width=35,textvariable=sv)
    if is_number_only:

        txt.config(validate='key',validatecommand=(reg_fun, '%P'))
    txt.pack(pady=10)
    txt.bind('<Return>',lambda my:f.destroy())
    ttk.Style().configure('inbox.TButton',font='None 15') 
    ttk.Button(f,text='OK',command=lambda:f.destroy(),style='inbox.TButton').pack(pady=10)
    f.grab_set()
    txt.focus()# عشان يركز على النص اول مايغتح الشاشة
    f.wait_window()# استنى الشاشة لما تقفل
    return sv.get()#مايرجع القيمة الا بعد ما الشاشة تقفل
    
    
    
    

