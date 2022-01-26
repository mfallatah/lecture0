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
