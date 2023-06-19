def inputvalue(lower, upper, prompt):
	value = int(input(prompt))
	while value < lower or value > upper:
		print("Error - re-enter number (lower-upper)")
		value = int(input(prompt))
	return value

numJudges = 7
numCompetitors = inputvalue(3,16,"Enter number of competitors (between 3 and 16) ") 

for comp in range(numCompetitors):
	totalC = 0
	print("input scores between 0 and 10 for each judge")
	
	for j in range(0, int(numJudges), 1):
		scoreJ = inputvalue(0,10,"Score for judge %s: " % j)
		totalC = float(totalC) + float(scoreJ)

	scoreC = float(totalC) / float(numJudges)
	print("Score for competitor " ,comp, "is ", scoreC)


