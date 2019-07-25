import mysql.connector
class connect1:
	"""
	singleton class
	"""
	connection = None 
	connect_options = {}
	def __init__(self,*args,**kwargs):
		print('inin')
		'''self.connect_options = {}
		self.connect_options['host']='localhost'
		self.connect_options['user']='root'
		self.connect_options['passwd']='ztech@44'
		self.connect_options['database']='Employee_DATA'
		#self.connection=mysql.connector.connect(**self.connect_options)'''
		self.get_connection()
	
	'''@staticmethod
	def get_connection(self, new = False):
		if new or not  self.connection:
			self.connection = mysql.connector.connect(**self.connect_options)
		return self.connection'''
		
	@staticmethod
	def get_connection(self):
		#connect_options = {}
		self.connect_options['host']='localhost'
		self.connect_options['user']='root'
		self.connect_options['passwd']='ztech@44'
		self.connect_options['database']='Employee_DATA'
		if  not  self.connection:
			self.connection = mysql.connector.connect(**self.connect_options)
		return self.connection
	
	'''def create_connection(self):
		self.connection=mysql.connector.connect(**self.connect_options)
		return self.connection.cursor()'''
		
	'''def __call__(self):
		print('init')
		print(self.__init__())'''
		
		
#c = connect.get_connection()


#@connect1
class database_operations(connect1):
	#__metaclass__= connect
	def __init__(self,*args,**kwargs):
		'''self.connect_options = {}
		self.connect_options['host']='localhost'
		self.connect_options['user']='root'
		self.connect_options['passwd']='ztech@44'
		self.connect_options['database']='Employee_DATA' '''
		self.insert()
	
	def insert(self):
		c = connect1.get_connection(self)
		cur = c.cursor()
		cur.execute("Select name from employee_info")
		result = cur.fetchall()
		for r in result:
			print r
		
conn = database_operations()






'''class a:
	pass
	
	
class b:
	pass
	
	
class c(b,a):
	super(c,self).__init__()
	a.__init__(self)'''
	
	
	
	
	



