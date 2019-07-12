#zap.jatinder

fruits = ['pineapple','cherry','banana','popaya'] #creating list
print(fruits)

print(fruits[2])#to print a specific element

fruits[3]='watermelon'#changing item valus
print(fruits)

for x in fruits:#Traversing the list
	print x

if "cherry" in fruits:#checking for a particular vslue
	print "Cherry is in fruits list"
	
print("Length of list is:{}".format(len(fruits)))#getting length of list

fruits.append("apples")#appending the list
print(fruits)

fruits.insert(1,"oranges")#inserting a new item at a specified index
print(fruits)

fruits.remove('pineapple')#removes a particular item
print(fruits)

fruits.pop(2)#remove elements from given index
print(fruits)

fruits.pop()#this will remove last item
print(fruits)

del fruits[0]
print(fruits)

#del fruits this will delete the entire list

'''fruits2 = fruits.copy()
print(fruits2)'''

fruits2 = list(fruits)
print(fruits2)

list2 = list((1,40,5,10,2))
list2.sort()
print list2

fruits.sort()
print(fruits)

