number = [1,12,14,21,25,27]
for x in number:
	index = number.index(x)
	var = index+1
	while(var<(len(number))-1):
		if number[index]+number[var]==26:
			print number[index], number[var]
		var+=1
	 
