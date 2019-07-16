
def wrapper(a):
	print (a)
	def inner(fun):
		print fun
		def inner2():
			print ("Using inner2 ",fun(num),"is displayed", "and",a,"received from outer block" )
			return 0
		return inner2
	return inner

@wrapper('python')
def display(n):
	print ('In display function',n)

num=4	
result = display()
print (result)
