#!/usr/bin/python

def longest(values) :
	getval = sorted(list(values))
	print getval
	counter = 1
	prevdiff = getval[1] - getval[0]
	diff = 0
	score = 0
	maxscore = 0

	for i in range(0, len(getval)-2):
		counter += 1
		diff = getval[counter] - getval[counter-1]
		print diff, prevdiff, maxscore
		if diff == prevdiff:
			score += 1
			if score > maxscore:
				maxscore = score

		if diff != prevdiff:
			score = 0

		prevdiff = diff

	return maxscore+2


print longest((-10,-20,-10,-10))
