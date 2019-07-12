def fab(n):
	a,b = 0,1
	while a<n:
		yield a
		a,b = b,a+b

for x in fab(6):
	print x
