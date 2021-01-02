from tkinter import*
from PIL import Image,ImageTk

root =Tk()
root.title("Image Teast")
root.geometry("800x500")

my_pic = ImageTk.PhotoImage(file="images/wa.JPG")

root.mainloop()