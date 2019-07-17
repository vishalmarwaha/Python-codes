'''Using decoratos inside classes'''
class decorate:
	def __init__(self,function):
		self.function=function
	
	def __call__(self,*args,**kwargs):
		result=self.function(*args,**kwargs)
		return result

@decorate
def function(name,message):
	print(name,message)

function('python',message='Programming Language')


