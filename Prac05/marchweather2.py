#
# marchweather2.py
#

import matplotlib.pyplot as plt


fileobj = open('marchweatherfull.csv', 'r')
data = fileobj.readlines()
fileobj.close()

mins = [] 
maxs = []
nines = []
threes = []

for line in data:
	splitline = line.split(',')
	mins.append(splitline[2])
	maxs.append(splitline[3])
	nines.append(splitline[10])
	threes.append(splitline[16])

dates = range(1, 26)

plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.show()

#writing to CSV file`

file2 = open('marchout.csv', 'w')
for i in range(len(mins)):
	file2.write(mins[i] + ',' + maxs[i] + ',' + nines[i] + ',' + threes[i] + '\n')
file2.close()
