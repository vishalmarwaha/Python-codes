import mysql.connector


class connection(object):
	"""
	singlton class
	"""
	def __init__(self,**kwargs):
		self.connect_options = {}
		self.connect_options['host']='localhost'
		self.connect_options['user']='root'
		self.connect_options['passwd']='ztech@44'
		self.connect_options['database']='Employee_DATA'
		self.connection=mysql.connector.connect(**self.connect_options)
			
	def get_cursor(self):
		return self.connection.cursor()
		
		


class database_operations:
	
	def insert(self,table,data):
		pass
		
	def update(self,table,where,data):
		pass
		
	
	def delete(self):
			
	
	join
	
	
	union`
	
	
	
	
	
	pass
		

class employees:
	pass	
		



class student:
	
	
class operations(connection):
	def __init__(self):
		super(operations, self).__init__()
		self.operation()

	def operation(self):
		cur = self.get_cursor()
		cur.execute("SELECT name from employee_info")
		result=cur.fetchall()
		for r in result:
			print r
	

conn = operations()

