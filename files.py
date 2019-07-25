'''from os import walk
f=[]
for (dirpath, dirnames,filenames) in walk('/var/www/html/python'):
	f.append(filenames)
print f'''

import os
dirname='second'
try:
	os.mkdir(dirname)
	print('Directory created')
except:
	print('Directory already exists')
	
