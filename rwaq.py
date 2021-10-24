n = int(input("Enter an Integer: "))

if n in range(100) and n % 2 != 0: 
        print ("weird")
if n in range(2-5) and n % 2 ==0:
		print("Not weird")
if n in range(6-20) and n % 2 == 0 :
	print("weird")
if n % 2 == 0 and n > 20 :
	print("Not weird")
else:
	pass

