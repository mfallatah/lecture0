
name = 'Mohammed'
age = 38
is_employee = True

#--------------
# القوائم قابلة للتعديل والالاضافة الوالحذف
names=['mohammed','ahmed', 'omar']
names.append('kemo') # لاضافة عنصر للقائمة في اخر القائمة
names.insert(0,'saeed') # اضافة عنصر في اي مكان نباه باضافة رقم الاندكس ثم القيمة
#names.remove('mohammed')# تحذف عنصر بتحديد القيمة
#names.clear()# تخذف القائمة كاملة
print(names[2]) # يطبع حسب الاندكس
print(names)
#-------------


# Tubles  غير قابلة للتغيير
chiled_one =('amr','maddinah', '1-1-2022') # في Tuples   نقدر نستغني عن الاقواس
print(type(chiled_one))


# Dictionary  نسند اسم وفيمة بينهم علامة تنصيص نوصل للعنصر عن طريق المفتاح وهو ماقبل علامة التنصيص
chiled_tow ={'name': 'ahmed', 'birth_city':'Maddainah','Birth_date':'2022'}
print(type(chiled_tow))
print(chiled_tow['name']) # نوصل للعنصر عن طريق المفتاح
print(chiled_tow.values())# To print all values in dictionary
print(chiled_tow.keys())# Toprint all keys in dictionary


# if , elif  and else : if we change the value of path result well be chnge
path = ''
if path =='ios':
    print("Swift")
elif path == 'Web Development':
    print('javaScript')
elif path == 'Android':
    print('hotlin')
else:
    print('Some thing else')


# Loop
i = 1
while i <= 5:
    print(i)
    i +=1

# For loop with Range
for n in range(10):
    print(n)

# FUNCTIONS
fname= input("Enter Your name:")
ftime= input('Enter the time of the day:')
print("Good "+ftime+","+fname+"!")


# Function parameter
def print_number(to):
    for i in range(to):
        print(i)
print_number(2)
print_number(3)
print_number(5)

# EXxample 3  we can add any number of parameter , passes more thhan parameter trough the function
def add(first_num, seconed_num):
    print(first_num + seconed_num)
add(3, 3)




------
names = []
phone_numbers = []
num = 3


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else:
    print("Name Not Found")
