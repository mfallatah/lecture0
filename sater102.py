
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
print(fname + '' + sname) # بوجود مسافة بين الاسمين
