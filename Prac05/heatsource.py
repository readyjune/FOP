#
# Name : <jinwookim>
# ID   : <90021907>
#
# heatsource.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

def calcheat(r,c):
	calc = 0.1 * (b2[r-1:r+2,c-1:c+2].sum() + b2[r,c])
	return calc


size = 10 

# create heat source
hlist = []
fileobj = open('heatsource.csv','r')
for line in fileobj:
	line_s = line.strip()
	ints = [int(x) for x in line_s.split(',')]
	hlist.append(ints)
fileobj.close()

h = np.array(hlist, dtype=int)
b = h.copy()

b2 = np.zeros((size,size))

# Calculate heat diffusion

for timestep in range(100): 
	for r in range(1, size-1): 
		for c in range (1, size- 1): 
			b2[r,c]=calcheat(r,c)

	for i in range(size): 
		for c in range(size):
			if h[r,c]>b2[r,c]:
				b2[r,c] = h[r,c]
	b2 = np.where(h>b2, h, b2)
	b=b2.copy() 



plt.imshow(b, cmap=plt.cm.hot) 
plt.show()


