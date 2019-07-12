import sys
a = sys.argv[1]
b = sys.argv[2]
if a>b:
	print "a is greater than b"
elif b>a:
	print "b is greater than a"
else:
	print "a and b are equal"


i = 1
while i<6:
	print i
	i+=1
	
i = 1
while i<4:
	i+=1
	if i == 3:
		continue
	print(i)

