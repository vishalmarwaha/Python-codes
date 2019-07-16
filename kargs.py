
def myFun(*args):
	for arg in args:
		print(arg)

myFun('Vishal','Python','Developer')

def kFun(**args):
	for key,value in args.items():
		print(key,value)

kFun(name="Vishal",department="Python developer")

def aFun(arg1,arg2,arg3):
	print("Argument 1:",arg1)
	print("Argument 2:",arg2)
	print("Argument 3:",arg3)

args=('Vishal','Python','Developer')
aFun(*args)
	
kwargs = {'arg1':'Vishal','arg2':'Python','arg3':'Developer'}
aFun(**kwargs)
