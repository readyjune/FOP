from animals import *

pets = []

with open("animals.csv","r") as document:
	for line in document:
		animal = line.strip("\n").split(",")

		if animal[0] == "dog":
			pets.append(dog(animal[1],animal[2],animal[3],animal[4]))

		elif animal[0] == "cat":
			pets.append(dog(animal[1],animal[2],animal[3],animal[4]))

		elif animal[0] == "bird":
			pets.append(dog(animal[1],animal[2],animal[3],animal[4]))

for pet in pets:
	pet.printit()
	print()
