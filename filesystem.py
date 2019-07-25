with open('test.txt','r') as t:
	data = t.readlines()
	for lines in data:
		word=lines.split()
		print word
