
def sum(a,b):
	return a+b
	
def sub(a,b):
	return a-b

#result = sum
#print(result(4,8))

def operation(fun,a,b):
	return fun(a,b)
	
result = operation
print(result(sub,4,5))


