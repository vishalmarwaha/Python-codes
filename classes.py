class Student:
	"""
	Student class definition
	"""
	
	no_of_students = 0
	def __init__(self,name,age):
		Student.no_of_students += 1
		self.name = name
		self.age = age
	
	def display(self):
		print self.name
		


std = Student('John',23)
std2 = Student('Mark',33)
"""print(std.age)
print(Student.__dict__)
print(std.__dict__)
print(Student.__doc__)
"""
print(Student.no_of_students)
std.display()

Student.display(std)

print std2.no_of_students
print(std2.__dict__)
