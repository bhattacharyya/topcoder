#!/usr/bin/python

class StreetParking:
	def __init__(self):
		return None

	def freeParks(self,street):
		counter = 0
		total = 0
		spaces = list(street)
		k = len(spaces)
		for i in range(0, k):
			j = "".join(spaces[i:i+3])
			if j in ["--B","-S-"]:
				del spaces[i:i+3]
				spaces.insert(i,"X")
		l = len(spaces)
		for i in range(0, l):
			j = "".join(spaces[i:i+2])
			if j in ["-B","-S","S-"]:
				del spaces[i:i+3]
				spaces.insert(i,"X")
		m = len(spaces)
		for i in range(0, m):
			if spaces[i] in ["D", "B", "S", "X"]:
				counter += 1
				total = len(spaces) - counter
		return total

test = StreetParking()
print test.freeParks("---B--S-D--S--")
