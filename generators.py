'''Iterators using generator function and generator expresssion'''

def square(numbers):
	for n in numbers:
		yield n**2
		#return n**3 

num=[1,2,3,4,5]
squares=square(num)
print(next(squares))


squares = (n**2 for n in num)
print(next(squares))


