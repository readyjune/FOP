#
# ConversionMachine.py - converting between out temperature formats.
#

print('\nConverting between temperature formats\n')

from conversions import *


choice = input('Enter selection: (A)Exit, (B)fahr2cel, (C)fahr2kel, (D)cel2fahr, (E)cel2kel, (F)kel2cel, (G)kel2fahr...')

while choice[0] != 'A':
	if choice[0] == 'B':
		print('Enter temperature ')
		temp = float(input())
		testC  = fahr2cel(temp)
		print(testC)
	elif choice[0] == 'C':
		print('Enter temperature ')
		temp = float(input())
		testC = fahr2kel(temp)
		print(testC)
	elif choice[0] == 'D':
		print('Enter temperature ')
		temp = float(input())
		testC = cel2fahr(temp)
		print(testC)
	elif choice[0] == 'E':
		print('Enter temperature ')
		temp = float(input())
		testC = cel2kel(temp)
		print(testC)
	elif choice[0] == 'F':
		print('Enter temperature ')
		temp = float(input())
		testC = kel2cel(temp)
		print(testC)
	elif choice[0] == 'G':
		print('Enter temperature ')
		temp = float(input())
		testC = kel2fahr(temp)
		print(testC)
	else:print('\nSee you later\n')

print('\nSee you later\n")
