#
# growtharray.py - simulation of unconstrained growth then storing it in an array before plotting it.
#

import matplotlib.pyplot as plt
import numpy as np

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

plt.title('Prac3.1: Unconstrained Growth')
plt.plot(timearray, poparray, color='red')
plt.xlabel('in hours')
plt.show()
