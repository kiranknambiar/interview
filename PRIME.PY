number=int(input("enter the number"))
for i in range (2,num):
	if number % i == 0:
		print("not a prime")
		break
else:
    print("prime")
