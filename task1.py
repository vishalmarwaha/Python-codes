numbers = []
ran = 10
for num in range(ran):
	if num>1:
		for n in range(2,num):
			if (num%n==0):
				break
		else:
			numbers.append(num)
print(numbers)

