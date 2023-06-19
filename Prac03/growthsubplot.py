#
# growtharray.py - simulation of unconstrained growth then storing it in an array before plotting it.
#

import matplotlib.pyplot as plt
import numpy as np

march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])
dates = range(1, len(march2017)+1)


print("\nSIMULATION - Unconstrained Growth\n")

length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

timearray = np.zeros(int(num_iter)+1) #creates an empty array for time thats num_iter elements long.
poparray = np.zeros(int(num_iter)+1) #creates an empty array for population thats num_iter elements long.

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num interations (sim length * time step per hour): ", num_iter)
print("Growthh step (growth rate per time step): ", growth_step)

print("\nRESULTS:n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)

times=[0]
pops=[100]


for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    times.append(time)
    pops.append(population)
    timearray[i] = time
    poparray[i] = population
    print("Time: ", time, " \tGrowth: ", growth, " \tPopulation: ", population)

print("\nPROCESSING COMPLETE.\n")

plt.figure(1)

plt.subplot(221)
plt.plot(dates, march2017, '--')
plt.title('March Temperatures')
plt.ylabel('Temperature')


plt.subplot(222)
plt.plot(dates, march2017, 'ro')
plt.ylabel('Temperature')
plt.xlabel('Date')


plt.subplot(223)
plt.plot(dates, march2017, 'g^')
plt.ylabel('Temperature')
plt.xlabel('Date')


plt.subplot(224)
plt.plot(dates, march2017, 'bs')
plt.ylabel('Temperature')
plt.xlabel('Date')


plt.show()

plt.savefig('growthsubplot')
