
def factorial(n):
	 if n==1:
		 return 1
	 else:
		return n*factorial(n-1)

num = int(input("Enter the number:"))
if num == 0:
	print "Factorial does not exist"
elif num == 1:
	print ("Factorial is 1")
else:
	print("Factorial of the number is:{}".format(factorial(num)))
