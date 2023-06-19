#
# listcomprehensions.py
#



def main():

	numbers = [i + 1 for i in range(0,5)]
	mixlist = ['Yo', '1', '2', '5', 'what', '234', 'up']
	wordlist = ['is', 'this', 'working']

	tripled = triple(numbers)
	grabnumbers = numbersonly(mixlist)
	capitalfirst = capitals(wordlist)

	print(numbers)
	print(tripled)
	print(grabnumbers)
	print(capitalfirst)

def triple(inList):
	return [i*3 for i in inList]

def numbersonly(inList):
	return [i for i in inList if i.isdigit()]

def capitals(inList):
	return  [i[0].upper()+i[1::] for i in inList]

if __name__ == '__main__':
	main()	
