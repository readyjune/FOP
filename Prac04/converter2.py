#
# Converter2.py - converting between out temperature formats.
#

print('\nConverting between temperature formats\n')

from conversions import *

while True:
	choice = input('Enter selection: (A)Exit, (B)fahr2cel, (C)fahr2kel, (D)cel2fahr, (E)cel2kel, (F)kel2cel, (G)kel2fahr...\n')
	choice = choice.upper()
	if choice[0] == 'B':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = fahr2cel(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = fahr2cel(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = fahr2cel(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = fahr2cel(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break	

	else:
		break

#################################################################




	if choice[0] == 'C':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = fahr2kel(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = fahr2kel(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = fahr2kel(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = fahr2kel(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break	

	else:
		break
#################################################

	if choice[0] == 'D':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = cel2fahr(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = cel2fahr(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = cel2fahr(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = cel2fahr(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break	

	else:
		break
#############################################

	if choice[0] == 'E':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = cel2kel(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = cel2kel(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = cel2kel(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = cel2kel(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break	

	else:
		break
################################################



	if choice[0] == 'F':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = kel2cel(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = kel2cel(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = kel2cel(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = kel2cel(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break

	else:
		break	
###############################################




	if choice[0] == 'G':
		print('Enter temperature ')
		temp = str(input())
		if(temp.isalpha()):
			print("Error please Type digit")
			temp = str(input())
			temp = float(temp)
			testC  = kel2fahr(temp)
			print(testC, " (If you want keep to do another conversion? 'Y' , No 'N)'")
			choose = str(input())
			if choose=='Y':
				continue
			else:
				print("Bye, See you soon\n")
				break

		else:
			temp = float(temp)
			testC = kel2fahr(temp)

			print(testC, " put the next value one more time ")
			temp = str(input())
			if(temp.isalpha()):
				print("Error please Type digit")
				temp = str(input())
				temp = float(temp)
				testC  = kel2fahr(temp)
				print(testC, " (If you want keep to do another converswion? 'Y' , No 'N'")
				choose = str(input())
				if choose=='Y':
					continue
				else:
					print("Bye, See you soon\n")
					break


			else:
				temp = float(temp)
				testC = kel2fahr(temp)
				print(testC, " (If you want keep to do another conversion? 'Y' or 'N)'")
				choose = str(input())

				if choose=='Y':
					continue
				else:
					print("Bye, see you soon\n")
					break	

	else:
		break

###############################################3
    
	if choice[0]=='A':
		print("Bye, See you soon\n")
		break
       

