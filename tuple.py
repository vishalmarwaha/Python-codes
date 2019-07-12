cars = ("BMW","Hyundai","Figo","Mercedes","BMW")
print(cars)

print(type(cars))

print(cars[1])#to access specific items
for x in cars:
	 print x
	 
if "Figo" in cars:
	print 'Figo is present in cars'
	
print(len(cars))

print(cars.count("BMW"))
	
print(cars.index("BMW"))
