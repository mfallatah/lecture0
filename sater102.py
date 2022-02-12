number = -999
print(abs(number)) # To print abslute value

number1 =  53.366
print(round(number1, 2)) # number 2 means take seconed digit after coma

num = 3
print(pow(num, 2))# To power of number

print( pow(3,3)) # another way

num4= (100,200,333,444) # To print maximmum value
print(max(num4))

num5= (100,200,333,444) # To print minimmum value
print(min(num5))

print(min(100,200,333,444))# another way

import math
num6=144
print(math.sqrt(num6)) # to print squre root we must invite math librarry
print(math.sqrt(144))# another way

print(math.remainder(9, 4)) # devsion remining

import random
print(random.randint(1, 100)) # To print Random number

import datetime
date = datetime.date(2022, 2, 8)
print(date) # to print all date

import datetime
date = datetime.date(2022, 2, 8)
print(date.year) # To print only year

import datetime
date = datetime.date(2022, 2, 8)
print(date.day)# To print only day


time = datetime.time(10, 12, 50)
print(time)


now = datetime.datetime.today()
print(now)

# Convert date and time to string

print(date.strftime('%A %B %Y'))
print(time.strftime('%I %M %S'))

#-------------------------
#indexing
# the indexinf for leters start from 0-25 or from -26 to -1 since -1 =z
alphabet = 'abcdz'
the_list = [1, 2, 3]
the_tuple = (4, 5, 6)
print(alphabet[-1])
print(the_list[-1])
print(the_tuple[-1])

# Slicing = reach to specific group of item instead of one item
# Closed Range
# open range  we have tow choise [from:] and [to:]
text = 'This Is Python Course'
print(text[8:14])
print(text[-6:])
print(text[:4])
print(text[0:7:2])# يطبع من النطاق من 1 الى 7 كل خانتين

# index function تبحث عن العنصر في حال تواجده ترجع الاندكس تبعه
text1 = "Lorem ipsum doloar sit amet consectetur adipiscing elit sed do"
the_list1 = [1, 2, 3]
the_tuple1 = (4, 5, 6)
print(text1.index('do'))
print(the_list1.index(2))
print(the_tuple1.index(6))

# len function
print(len(text1))

# count function
# عشان نعرف العنصر كم كرة اتكرر في القائمة او الحرف كم مرة تكرر
sstring = 'This si studend sozan'
llist = [1, 2, 3, 3, 3, 3]
ttpule = (1, 1, 1, 1, 4, 4, 4)
print(sstring.count('s'))
print(llist.count(3))
print(ttpule.count(4))

# in function return thru or false
# البحث عن ننصر معين في تسلسل معين
ttxet = (' welcome to python world ')
print('to' in ttxet)

# الدمج والتكرار
fname = 'Mohammed'
sname =  'Fallatah'
print(fname + sname) #بدون مسافة بين الاسمين
print(fname + ' ' + sname) # بوجود مسافة بين الاسمين

# RePLACE
vva ='1\n2\n3\n4\n5\n6'
print(vva)
print(vva.replace('\n',','))

#STRIP
#  لللتخلص من المسافات الزائدة في بداية ونهاية الجملة
txxt ='     python course     '
print(txxt)
print(txxt.strip()) # without space   lstrip delete space befor rstrip delete space after



str = 'This is python Course'
print(str.lower()) # make all letters small
print(str.upper()) # make all letters capital
print(str.swapcase())# chnge capital letters to small and oposit
print(str.title())# convert first letter in each word to capital


# Format function

names = 'mohammed'
family = 'fallatah'
agee = 38
print('My Name is {} {}, and I am {} years old..format'.format(names, family, agee))


txtt = "My name is {1}, and I'm {0} years old".format(30, 'Reem')
print(txtt)


# الدالة فلتر يمكن اختصار اللوب اللي سوناه في القسم الاول بالكود في القسم الثاني
# الدالة فلتر تستتقبل مدخلين الاول يحتوي لى شرط معين والثاني  قائمة
#ages = [30, 9, 15, 32, 17, 44, 26, 5]
adult = []
#def filtered_ages(ages):
#    for age in ages:
#        if age >= 18:
#            adult.append(age)
#   return adult
#print(filtered_ages(ages))
# نمرر الدالة ثم القائمة

ages = [30, 9, 15, 32, 17, 44, 26, 5]
def filtered_ages(age):
    return age >=18
print(list(filter(filtered_ages, ages))) # نمرر الدالة ثم القائمة  والدالة فلتر راه تقوم بتمرير عنصر واحد واختباره اذا اجتاز الشرط راح تاخذه واذا ما اجتازه تتجاهله


# map
# الدالة ماب  تستقبل دالة وقائمة وتقود الدالة بالمرور على الائمة عنصر عنر  وتطبيق الدالة المررة على هذه العناصروراخ ترجعلنا قائمة جديدة بالقيم الجديدة بعد تطبيق الدالة الممرة عليها
# List[m,n,p] function,f() ===> if (m==condition)===> New list [f(m),f(n),f(p)]
'''
numbers = [5,10,20,25,50]
sq_numbers =[] # هنا تحفظ القيم الجديدة

def square(numbers):
    for num in numbers:
        sq_numbers.append(num**2) # عشان نرفعها للاس 2
    return sq_numbers
print(square(numbers))
'''

numbers = [5,10,20,25,50]
def square(num):
    return num ** 2
print(list(map(square,numbers)))


# sort
#الدالة سورت تقوم بترتيب االقوئم تصاعديا او تنازليا
list1 =['mohammed','ahmed', 'khaled']
list2 =[3,5,7,9]
list1.sort() # الترتيب يكون تصاعدي وابجدي
list2.sort(reverse=True) # مابين القوسين يجعل الترتيب تنازلي
print(list1)
print(list2)


'''
# List Comprehension
# انشاء قائمة  على قائمة موجودة مسبقا  تخت شروط معينة
lst =[1,2,3,4,5]
multiplied_list = []
for num in lst:
    if (num > 3 ) and num % 5 == 0:
        multiplied_list.append(num*2)
print(multiplied_list)
'''

lst =[1,2,3,4,5]
multiplied_list = [num*2 for num in lst if num > 3 and num % 5 == 0] # اختصرنا الاسطر البرمجية في العلى بهذه السطرين
print(multiplied_list)


# positional arguments
#number of argument must be equal to number of parameter
# لازم عدد المدخلات يساوي عدد المخرجات 
def info(name, age):
    print('My name is',name, 'and I am', age , 'years old')
info('Mohammed', 30)


