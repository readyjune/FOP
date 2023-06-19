def main():
	numJudges = 7
	numCompetitors = input("Enter number of competitors (between 3 and 16 inc)")

	while int(numCompetitors) < 3 or int(numCompetitors) > 16:
		numCompetitors = input("Error - Re-enter number of competitiors(between 3 and 16 inc)")

	for comp in range(0, int(numCompetitors), 1):
		totalC = 0
		print("input scores between 0 and 10 for each Judge")
		for j in range(0, int(numJudges), 1):
			scoreJ = input("Score for judge %s: " % j)
			while float(scoreJ) < 0 or float(scoreJ) > 10:
				scoreJ = input("Error - Re-enter score (0-10): ")
			totalC = float(totalC) + float(scoreJ)

		scoreC = float(totalC) / float(numJudges)
		print("Score for competitors %s is %s" % (comp, scoreC))

if __name__ == "__main__":
	main()
