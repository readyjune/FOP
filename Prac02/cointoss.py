#
# cointoss.py - simulate tossing a coin multiple times
#

import random

n=int(input("Enter the number of toss?:"))

coin = ['heads','tails']
heads = 0
tails = 0
trials = n

print('\nCOIN TOSS\n')

for index in range(n):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1

print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')

