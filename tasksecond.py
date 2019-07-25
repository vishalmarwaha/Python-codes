val ={}
key = raw_input("Enter the key")
value = raw_input("Enter the value for the key")
val[key] = value
for key,value in val.items():
	print(key,value)
