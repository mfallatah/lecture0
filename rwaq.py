def fact(x): # 
	if x == 1:
		return 1
	else:
		return (x * fact(x-1))
num = 3
print(fact(num)) 
# fact (3) = 3*fact(2)
# fact (2) = 2*fact(1)
# fact (1) = 1 وهنا تحقق الشرط اللي في ثاني سطر انه يوقف اذا كانت 