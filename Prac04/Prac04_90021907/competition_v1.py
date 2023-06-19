def main():
	numJudges = 7
	numCompetitors = input("Enter number of competitors (between 3 and 16 inc)")

	for comp in range(0, int(numCompetitors), 1):
		totalC = 0
		print("input scores between 0 and 10 for each Judge")
		for j in range(0, int(numJudges), 1):
			scoreJ = input("Score for judge %s: " % j)
			totalC = float(totalC) + float(scoreJ)

		scoreC = float(totalC) / float(numJudges)
		print("Score for competitor %s is %s" % (comp, scoreC))

if __name__ == "__main__":
	main()
