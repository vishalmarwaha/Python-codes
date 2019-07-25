import mysql.connector #mysql driver for accesing MYSQL database
c=mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='ztech@44',
	database='Employee_DATA')

cur = c.cursor()
#cur.execute('create table employee_info(id INT AUTO_INCREMENT PRIMARY KEY,name varchar(255),department varchar(255),salary int(20))')
'''sql = "INSERT INTO employee_info(name,department,salary) VALUES (%s,%s,%s)"
val=[
('Vishal','Python',10000),
('Mark','PHP',5000),
('Daniel','Python',2000)
]
cur.executemany(sql,val)'''
'''cur.execute("SELECT * from employee_info")
result = cur.fetchone()
print(result)'''
'''cur.execute("SELECT * from employee_info where name='Vishal'")
result = cur.fetchall()
for r in result:
	print r'''

'''cur.execute("DELETE from employee_info where name = 'Daniel'")
c.commit()
print(cur.rowcount,'number of rows deleted')'''

'''cur.execute("UPDATE employee_info SET department = 'PHP' where department='PHaP'")
c.commit()
print(cur.rowcount, "Number of rows updated")'''

cur.execute("Select * from employee_info LIMIT 5 OFFSET 2")
result = cur.fetchall()
for r in result:
	print r
