import mysql.connector

c = mysql.connector.connect(host='localhost',user='root',passwd='ztech@44')
print(c)


cur = c.cursor()

cur.execute('SHOW DATABASES')






for db in cur:
	print(db)
