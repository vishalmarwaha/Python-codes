import sys

data={'name':'','eid':'','salary':'','dept_id':'','branch_name':''}
class employee():
	def __init__(self,data):
		self.data=data
	
	
	def add(self,ename,emid,esalary,edept_id,ebranch_name):
		self.data['name'] = ename
		self.data['eid'] = emid
		self.data['salary']= esalary
		self.data['dept_id']= edept_id
		self.data['branch_name']= ebranch_name
		
	def show(self):
		print(self.data)
		
	def update(self):
		key=raw_input('Enter the field for which value is to be updated:- ')
		value=raw_input('Enter value for field:- ')
		self.data[key]=value
	
	def delete(self):
		key=raw_input('Enter the key for which value is to be deleted:- ')
		del self.data[key]
		
def control():
	empl.cnt=int(raw_input("Enter 1 to perform any operatoin or 2 to Exit:-"))
	if empl.cnt==1:
		choice()
	elif empl.cnt==2:
		sys.exit(0);
	else:
		print("Wrong Choice Entered!!!!!!")
		
def choice():
	empl.choice=int(raw_input("Enter 1 to ADD data or 2 to SHOW data or 3 to UPDATE data or 4 to DELETE:- "))
	if empl.choice==1:
			name=str(raw_input('Enter name:-'))
			eid = str(raw_input('Enter eid:-'))
			salary = int(raw_input('Enter salary:-'))
			dept_id=int(raw_input('Enter deptid:-'))
			branch_name=str(raw_input('Enter branch name:-'))
			empl.add(name,eid,salary,dept_id,branch_name)
			
	elif empl.choice==2:
		empl.show()
	
	elif empl.choice==3:
		empl.update()
		
	elif empl.choice==4:
		empl.delete()

	else:
		print("Invalid Choice")
	control()
	

empl = employee(data)
choice()

	
	
		

