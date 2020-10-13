from tkinter import *

frm = Tk()
frm.title('Menubar')
menuebar = Menu(frm)
filemenue = Menu(menuebar, tearoff=0)# المنيو متفرعة من المنيو بار اللي سويناها فوق تير اوف يمنع ظهور الخطوط فوق القائمة
filemenue.add_command(label='New',command=lambda:print('New'))
filemenue.add_command(label='Save',command=lambda:print('Save'))

editmenue = Menu(menuebar, tearoff=0)# المنيو متفرعة من المنيو بار اللي سويناها فوق تير اوف يمنع ظهور الخطوط فوق القائمة
editmenue.add_command(label='Copy',command=lambda:print('Copy'))
editmenue.add_command(label='Past',command=lambda:print('Past'))

menuebar.add_cascade (label='File',menu=filemenue) # كود الاضافة عشان تطلع القائمة
menuebar.add_cascade (label='Edit',menu=editmenue)
frm.config(menu=menuebar)



