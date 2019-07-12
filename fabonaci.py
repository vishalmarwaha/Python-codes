

def fabonacci(a,b,n):
	print a
	print b
	for x in range(2,n):
		temp = a+b
		print temp
		a = b
		b = temp
		
a=0
b=1
num = int(input("Enter number of terms in the series:"))
fabonacci(a,b,num)
	
