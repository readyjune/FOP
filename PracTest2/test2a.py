#resultarray,
# Student Name: <your name>
# Student ID  : <your ID>
#
# test2a.py: Simulate spread of disease through a population 
#            using SIR model 
# 
# Based on SIR model:
#    Shiflet&Shiflet Module 4.3 Modeling the Spread of SARS
#    and https://www.youtube.com/watch?v=k6nLfCbAzgo
#

import matplotlib.pyplot as plt
import numpy as np

Scur = 762   # number of people susceptible
Icur = 1     # number of people infected
Rcur = 0     # number of people recovered

trans_cost = 0.00218   # infectiousness of disease r = kb/N
recov_rate = 0.5        # recovery rate a = 1/(# days infected)
simlength = 14          # number of days in simulati

resultarray = np.zeros((simlength+1,3)) # using floats as % of popn
resultarray[0,:] = Scur, Icur, Rcur     # record initial values

for i in range(1, simlength+2):
	new_infected = trans_cost * Scur * Icur   # = rSI
	new_recovered = recov_rate * Icur          # = aI

	Scur = Scur - new_infected
	Icur = Icur + new_infected - new_recovered
	Rcur = Rcur + new_recovered

	resultarray[i:] = Scur, Icur, Rcur

plt.figure("SIR Model r = <rvalue>, a = <avalue>")
plt.xlabel("Day")
plt.ylabel("Number of People")
plt.plot(resultarray[:,0], 'b', resultarray[:,1], 'r-', resultarray[:,2], 'g^')

plt.savefig('graph1.png')
plt.show()



plt.subplot(221)
plt.plot(resultarray[:,1], 'r--') 
plt.xlabel("Day")
plt.ylabel("Number of People")

plt.subplot(222)
plt.plot(resultarray[:,0], 'b')
plt.xlabel("Day")
plt.ylabel("Number of People")

plt.subplot(223)
plt.plot(resultarray[:,2], 'g^')
plt.xlabel("Day")
plt.ylabel("Number of People")


plt.subplot(224)
plt.plot(resultarray[:,1], 'r-', resultarray[:,0], 'b', resultarray[:,2], 'g^')
plt.xlabel("Day")
plt.ylabel("Number of People")

plt.savefig('graph2.png')
plt.show()

