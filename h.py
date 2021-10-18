'''
a= ['Apple','Mango','orange']# list
b = (91,2,3) # tuple
fow = {'a', 'b', 'c', 'd'} #set
abl = {'a' : 'Apple', 'b' : 'Mango', 'c' :'Orang'} #dectonary

print(a)
print(b)
print(fow)
print(abl)
'''
'''

'''

'''
x = "moahmmed"
print(x.upper())

يحول الحروف كلها الى حروف كبيرة
'''

'''
s = {1,2,3,4,5,6,6,6} 
print(type(s)) # نوع القوس بريسس ويطبع مجموعات
print(s) # يطبع العناصر اللي داخل s وما يطبع العناصر المتكررة 
'''






''''
x = "moahmmed"
print(x.lower())
يحول الحروف الى صغيرة
'''

"""
for x in range (30):
    print(x)
else:
    print("Your have tow days of")
"""

"""
a = 5
print(type(a)) # لمعرفة نوع المدخل

"""


"""
a = 5
print(isinstance(a,str)) #  لمعرفة نوع المدخل"""
"""
a = 4+2j
print(type(a))# يمكننا طباعة الارقام المعقدة واللتي تحتوي على ارقام وحروف 

"""

""""
b = [1,2,3,4,'mo',4+3,6]
print(b[::]) # يطبعها كلها 
"""

"""
s = {'Hello', 'welcome', 3} # هذه الاقواس معناها ان البيانات تكون مجموعة 
print(type(s))
# tuble and list are order 
# we can't make change in tuble
# In set we can make change by add or change or remove
"""

"""
s = {'A':5,'B':'Hello'} # في الست نقدر قيمة عنطر معين بذكر اسمه ولا نستطيع طباعة قيمته عن طريق الاندكس
print(s['A'])

"""

"""
Data structure Order Multible  Construction      Example
List           yes    yes   []  or list   0 ()   [1,2,3,4,5]
Tuble          Yes    No    ()  or tuple()       (1,2,3,4,5)
Set            No     Yes   {}  or set ()        {1,2,3,4,5}
Dictionary     No     No    {}  or dict()        {'dec':14, 'Apr': 15}
"""





"""
s = {'Hello', 'welcome', 3}
s |={'mohammed', 'fallatah'} # | يدمج بين المجموعتين مع ان لها نفس الاسم
print(s)
"""

"""
s = {'Hello', 'welcome', 3}
s.add('course') # للاضافة على القائمة السابقة
print(s)

"""
"""
c = [1,2,3,4,5,'mf',6]
print(c[::-1])# يطبعها بالعكس
"""

"""
استخدام الدوال الحسابية 
10**2  = ten power 2
3/ float
3/ / integer

Implicit  =  ضمني  تكون متضمنة في العمليات ليست صريحة ماينفع تتنفذ على طول

"""
"""
number1 = 10
number2 = 10.0
print(type(number1))
print(type(number2))
result = number1 + number2
print(result)
"""

"""

print("Hello world", "Mohammed", "madinah", sep='****')
كلمة sep  تضع لي ماضعه بين القوسين بعد كل فاصلة


"""

"""
print("Hello world", "Mohammed", "madinah", sep='****', end ="FALLATAH")

x = 10
y = 100
print("The result {1} {0} ".format(x,y))
"""
"""



number = 10.222222222
print("The result of number is %.4f"%number)
#يطبع فقط 4 ارقام بعد الفاصلة او حسب مانحدد 
"""

"""

number = 10.222222222
print("The result of number is %10.4f"%number)
# الرقم 10 قبل الفاصة يحط مسافة بادئة ونقدر نغيرها 
"""



"""
c = [1,2,3,4,5,'mf',6]
print(c[::-2]) #  يطبعها بالعكس ياخذ خانة ويلغي خانة 
"""




"""
a =[1,2,3,4,5,'mohammed', 4+3]
print(a) # طباعة قائمة حتى لوكانت انواع البيانات مختلفة

"""
"""
# مربع ادخال
x = input("inter Your Name")# ماداخل القوسين ممكن نغيره او نخليه فاضي العادة تكون من نوع string
print (x) 

"""

"""

# لو نبغى نغير نوع الداتا في المدخل من نص الى ارقام او اي شيئ اخر
x= input()
print(type(int(x)))

"""

"""
eval('10+20') #الدالة (veal) تاخذ العمليات من داخل النص وتنفذها 


"""
"""
x = 10
y  = 20
if x > 10:
  print(" x is bigger")
else:
  print("x is smaller")

"""
"""
x = 10
y = 20
if x < y and x > 5:
  print("true")
else:
  print("False")

"""
"""
x = 10
y = 20
if x < y or x > 5:
  print("true")
else:
  print("False")

"""

"""
x = 10
y = 20
if not x < y: # not  تعكس الجملة اذا كانت صحيحة تصبح خاطئة والعكس
  print("true")
else:
  print("False")
"""
"""
x = 10
x+= 10
print(x) # it is equal to x = x + 10 for all oprations / * - +

"""
"""
x = 10
y = 10
print(id(x),id(y))
print(x is y) # نسال هل القيميتين لهمانفس المكان في الميموري ويعطينا انها صحيحة ويمكن نكتب x is noy y
"""

"""
x = [10,20,30]
y = [10,20,30]
print(id(x),id(y))
print(x is y) # هنا يعطينا انها خاطئة 
"""
"""
x = "hello"
'h' in x

"""
"""
# if and else statment
x = 10
if x <10:
    print("yes")
else:
  print("No")
"""
"""
"""
import tkinter
from tkinter import ttk
form = tkinter.Tk()
form.geometry('600x400')
lbl1 = ttk.Label(form , text = 'MOHAMMED')
x1 = ttk.Entry(form, text = 'ENTER YOUR NAME' )
lbl2 = ttk.Label(form , text = 'IBRAHIM')
lbl3 = ttk.Label(form , text = 'FALLATAH')
lbl3.config(background='navy',foreground='lightblue',font = ('impact',50),padding =20)
lbl2.config(background='yellow',foreground='lightblue',font = ('impact',30),padding =(10,20,30,40))
x1.config(background='black', text='ENTER YOUR NAME', foreground='lightblue',font =('impact',30))

lbl1.pack()
x1.pack()
lbl2.pack()
lbl3.pack()


form.mainloop()

input ('Press Enter')
"""
"""