
def sum(a,b):
	def sub(a,b):
		def mul(a,b):
			return a+b,a-b,a*b 
		return mul(a,b) 	
	return sub(a,b)
	#mul(a,b)	

def operation(fun,a,b):
	return fun(a,b)
	
result = operation(sum,10,20)
print(result)
