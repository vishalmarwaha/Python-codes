'''Arguments and keyword arguments in java'''
def myFun(*data):
	for arg in data:
		print (arg)
		
myFun("My",'name','is', 2)


def myArgFun(**kwargs):
	for key,value in kwargs.items():
		print(key,value)

myArgFun(fname="vishal",lname="marwaha")
