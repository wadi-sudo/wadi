import time
import os
import os.path



current = time.time()

one_year = 1314000
 
limit = 1661015440	

if os.path.exists('static/test.txt'):
	print('yes')
	if current >= limit :
		os.remove("static/test.txt")

