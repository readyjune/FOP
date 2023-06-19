#
# weather.py: Pritn min and max temps from a file
#		 (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt



fileobj = open('marchweather.csv','r')

#[line 1, line 2]

data = fileobj.readlines()
print("data ", data)

# add file reading code here

fileobj.close()

print("data 0", data[0])
print("data 1", data[1])
mins = data[0].split(',')
print("mins" , mins)
maxs = data[1].split(',')
print("maxs", maxs)
dates = range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()

