from tools import *

pad = 5
fnt = 'Tahoma 16'
bg  = 'lightblue'
fg  = 'navy'

# دالة عشان نبرمج الازارير اللي في الواجهة الرئيسية وضيفتها اني اعطيها اسم الفورم وهي تشغله
def opentop (name): 
    frm = None
    if name == 'emp' : frm = employee()
    if name == 'dept': frm = department()
    if name == 'item': frm = item()
    bgall(frm,bg)
    fgall(frm,fg)
    fontall(frm,fnt)
    frm.grab_set()

# هذا الفورم الاول ومن داخله نستطيع الانتقال الى القسام الاخرى 
# frm_main  = notfixed , form = fixed from tools , label.buttons,bgall,fgall,fontall are from tolls
def mainform ():
    frm_main = form('750x500','Company program')
    label(frm_main,'Company program').pack(pady=pad)

    label(frm_main,'_____________________').pack(pady=pad) # مجرد تنظيم مو مهم

    button(frm_main,'Employee',lambda:opentop('emp')).pack(pady=pad) # ينادي الدالة اوبن فخح في سطر 8 ويرسلها كلمة emp
    button(frm_main,'Department',lambda:opentop('dept')).pack(pady=pad)
    button(frm_main,'Item',lambda:opentop('item')).pack(pady=pad)
    button(frm_main,'Exit',frm_main.destroy).pack(pady=pad)

    label(frm_main,'_____________________').pack(pady=pad) # مجرد تنظيم مو مهم

    bgall(frm_main,bg)
    fgall(frm_main,fg)
    fontall(frm_main,fnt)

    return frm_main


def employee():
    frm_emp = toplevel('700x450','Employee Form') # tpo level لانها منبثقة وليست الفورم الرئيسة
    label(frm_emp,'Employee Form').pack(pady=pad)
    f1 = frame(frm_emp)
    f1.pack(pady=pad)
    f2 = frame(frm_emp)
    f2.pack(pady=pad)
    vnum   = strVar()
    vname  = strVar()
    vcity  = strVar()
    vphone = strVar()
    vemail = strVar()

    label   (f1,'Number').grid(row=0,column=0,pady=pad)
    textbox (f1,vnum)    .grid(row=0,column=1,pady=pad)

    label   (f1,'Name')  .grid(row=1,column=0,pady=pad)
    textbox (f1,vname)   .grid(row=1,column=1,pady=pad)

    label   (f1,'City')  .grid(row=2,column=0,pady=pad)
    textbox (f1,vcity)   .grid(row=2,column=1,pady=pad)

    label   (f1,'Phone').grid(row=3,column=0,pady=pad)
    textbox (f1,vphone)  .grid(row=3,column=1,pady=pad)

    label   (f1,'Email').grid(row=4,column=0,pady=pad)
    textbox (f1,vemail) .grid(row=4,column=1,pady=pad)
    
    def showdata(): # هذي الدالة تعرض البيانات
        msgbox([vnum.get(),vname.get(),vcity.get(),vphone.get(),vemail.get()])

    button(f2,'Add',showdata).grid(row=0,column=0,pady=pad)
    button(f2,'Edit',showdata).grid(row=0,column=1,pady=pad)
    button(f2,'Delete',showdata).grid(row=0,column=2,pady=pad)
    button(f2,'Find',showdata).grid(row=0,column=3,pady=pad)
    button(f2,'Close',frm_emp.destroy).grid(row=1,column=0,columnspan=4,pady=pad)

     
    return frm_emp

def department ():
    frm_dept = toplevel('700x300','Department Form')
    label(frm_dept,'Department Form').pack(pady=pad)
    #  نحتاج نسوي فريمين واحد للعناصر والثاني للازرار
    f1 = frame(frm_dept) # هذا الفريم الاول للعناصر 
    f1.pack(pady=pad)
    # الفريم الثاني لازارير 
    f2 = frame(frm_dept)
    f2.pack(pady=pad)
    # هذي مهمة لاي انتري بوكس كل صندوق ادخال يكون له واحد
    vnum  = strVar()
    vname = strVar()
    vloc = strVar()
    # نضيق الليبل اللي حانكتب عليها اسماء العناصر
    label(f1,'Department Number').grid(row=0,column=0,pady=pad)
    textbox (f1,vnum) .grid(row=0,column=1,pady=pad)

    label(f1,'Department Name').grid(row=1,column=0,pady=pad)
    textbox (f1,vname) .grid(row=1,column=1,pady=pad)

    label(f1,'Department Location').grid(row=2,column=0,pady=pad)
    textbox (f1,vloc) .grid(row=2,column=1,pady=pad)

    def showdata(): # هذي الدالة تعرض البيانات
        msgbox([vnum.get(),vname.get(),vloc.get()])
    
    button(f2,'Add',showdata).grid(row=0,column=0,pady=pad)
    button(f2,'Edit',showdata).grid(row=0,column=1,pady=pad)
    button(f2,'Delete',showdata).grid(row=0,column=2,pady=pad)
    button(f2,'Find',showdata).grid(row=0,column=3,pady=pad)
    button(f2,'Close',frm_dept.destroy).grid(row=1,column=0,columnspan=4,pady=pad)

    return frm_dept

def item ():
    frm_item = toplevel('700x400','Item Form')
    label(frm_item,'Item Form').pack(pady=pad)
    f1 = frame (frm_item)
    f1.pack(pady=pad)

    f2 = frame (frm_item)
    f2.pack(pady=pad)

    vnum   = strVar()
    vname  = strVar()
    vprice = strVar()

    label(f1,'Item Number').grid(row=0,column=0,pady=pad)
    textbox (f1,vnum) .grid(row=0,column=1,pady=pad)

    label(f1,'Item Name').grid(row=1,column=0,pady=pad)
    textbox (f1,vname) .grid(row=1,column=1,pady=pad)

    label(f1,'Item Price').grid(row=2,column=0,pady=pad)
    textbox (f1,vprice).grid(row=2,column=1,pady=pad)

    def showdata(): # هذي الدالة تعرض البيانات
        msgbox([vnum.get(),vname.get(),vprice.get()])
    
    button(f2,'Add',showdata).grid(row=0,column=0,pady=pad)
    button(f2,'Edit',showdata).grid(row=0,column=1,pady=pad)
    button(f2,'Delete',showdata).grid(row=0,column=2,pady=pad)
    button(f2,'Find',showdata).grid(row=0,column=3,pady=pad)
    button(f2,'Close',frm_item.destroy).grid(row=1,column=0,columnspan=4,pady=pad)


    return frm_item



