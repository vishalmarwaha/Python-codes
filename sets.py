cars = {'BMW','toyota','Hyundai','Mahindra'}
cars2 = {'toyota','hyundai'}
print(cars)
 
for x in cars: #to traverse elements in set
	print x

print('BMW'in cars)
print('Mercedes' in cars)

cars.add('Marcedes') #to add one element we use add function
print(cars)

cars.update(['porsh','jaguar'])
print(cars)

print(len(cars))

cars.discard('Gwagon')#this will not raise error that the particular item is not present

cars.remove('BMW')

x=cars.pop()
print(x)
 
cars3 = cars.union(cars2)
print(cars3)




