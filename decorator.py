"""def wrapper(fun):
	def inner():
		return "<h1>" + fun() + "</h1>"
	return inner
		


def display():
	return "I am in display function"
	
	
result = wrapper(display)()

print(result)
"""
'''Passing argument to the function'''
"""def decorate(fun,n):
	def inner():
		return 'Using Decorators ' ,fun(n) ,' displayed'
	return inner
	
def display(n):
	return n*3

num = 3
result = decorate(display,num)()
print(result)
"""
'''Passing argument to the function'''
def decorate(fun):
	def inner():
		return 'Using Decorators ' ,fun(num) ,'is displayed'
	return inner

@decorate	
def display(n):
	return n*3

num = 4
result = display()
print(result)


'''Use of multiple decorators'''
def decorate(fun):
	def inner():
		return 'Using Decorators ' ,fun(num) ,'is displayed'
	return inner

def moredecorate(fun):
	
	def inn():
		print("in inn()")
		print num
		return 'Using decorator2',fun(num),'is displayed'
	return inn

@decorate	
@moredecorate
def display(n):
	return n*3

num = 4
result = display()
print(result)
