# Procedure Orianted Programming البرمجة الاجرائية
class Student: # اول اسم في الكلاس لازم يكون حرف كبير
    def __init__(self, name, age, id, grade): # This is Object
        self.name = name
        self.age = age
        self.id = id
        self.grade =grade
    def talk(self): # This is Method
        print('My name is :', self.name)
# عشان ننشؤ اوبجكت من الكلاس اول شي نعرف اسمه
# بعدين نكتب اسم الكلاس اللي نبغى ننشئ الاوبجكت منه ونمرر له قيم الخصائص

std1 = Student('Moayad', 7, 'xx10', 100) # this is object from Student class
print(std1.name)
std1.talk()
