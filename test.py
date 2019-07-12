'''list=[]
x = 0
while x<10:
	num = random.randrange(1,11)
	if num not in list:
		x = x+1
		list.insert(x,num)

print list'''

import random
numbers = set(())
x = 0
while len(numbers)<10:
	num = random.randrange(1,11)
	numbers.add(num)
print numbers

