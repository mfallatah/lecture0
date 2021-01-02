from tkinter import*
from PIL import Image,ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('نموذج تسجيل مستحق')
        self.root.geometry("1400x800+0+0")
        
        # add backgroungd image
        self.bg=ImageTk.PhotoImage(file="images/wa.jpg")
        bg=Label(self.root,image=self.bg).place(x=10,y=50,relwidth=.5,relheight=.5)

        


root=Tk()
obj = Register(root)
root.mainloop()