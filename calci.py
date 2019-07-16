class operation:
	result=0
	def __init__(self,var1,var2):
		self.var1=var1
		self.var2=var2
		
	def __sum__(self):
		operation.result = self.var1+self.var2
		print self.result
		
	def __sub__(self):
		operation.result = self.var1-self.var2
		print self.result
	
	def __mul__(self):
		operation.result = self.var1*self.var2
		print self.result
	
	def __div__(self):
		operation.result = self.var1/self.var2
		print self.result
		
		

ope=operation(10,20)

print("Sum of two numbers is: ")
ope.__sum__()
print("Difference of two numbers is: ")
ope.__sub__()
print("Product of two numbers is: ")
ope.__mul__()
print("Quotient of two numbers is: ")
ope.__div__()	
