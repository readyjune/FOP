import re
from people import *

#List of People
peopleList = []

try:
	with open('people.csv', 'r') as f:
		lines = f.readlines()
except OSError as err:
	print('Error with file open: ',err)
except:
	print('Unexpected error: ', err)

with open('people.csv', 'r') as f:
	lines = f.readlines()

# Lets create a pattern and extract some information with it
reg = re.compile(r'''(
				 (\d+[a-zA-Z]?)  # (2) house number
				 (\s+)
				 (\w+\s\w+)      # (4) street name and type
				 (,\s+)
				 (\w+)			 # (6) suburb
				 (,\s+)
				 (\d{4})		 # (8) postcode
				 )''', re.VERBOSE)

for line in lines:
	splitline = line.strip().split(':')
	myclass = splitline[0]
	name = splitline[1]
	dob = splitline[2]
	inaddress = splitline[3]
	result = reg.match(inaddress) # returns the matching groups
	if result:
		num = result.group(2)
		street = result.group(4)
		suburb = result.group(6)
		postcode = result.group(8)
		print(myclass,'|',name,'|',dob,'|',num,'|',street,'|',suburb,'|',postcode)

		#make the address
		tempAddr = Address(num,street,suburb,postcode)

		#making the class
		if myclass == 'Staff':
			peopleList.append(Staff(name,dob,tempAddr,1))
		elif myclass == 'Undergrad':
			peopleList.append(Undergrad(name,dob,tempAddr,1))
		elif myclass == 'Postgrad':
			peopleList.append(Postgrad(name,dob,tempAddr,1))
	else:
		print('Address not matched: ', inaddress)

for p in peopleList:
	p.displayPerson()
	print()
