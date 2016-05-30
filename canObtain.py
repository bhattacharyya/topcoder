#!/usr/bin/python

class ABBA:

	def __init__(self):
		return None
	def canObtain(self, initial, target):

		index1 = 0	
		possibleSet = [initial]
		decision = "Impossible"
		lenInitial = len(list(initial))
		lenTarget = len(list(target))
		lenDif = int(lenTarget) - int(lenInitial)
		while index1 < lenDif : 
			for k in range(0,2**index1):
				possibleSet.append(possibleSet[k] + "A")
				temp = possibleSet[k][::-1]
				temp2 = temp + "B"
				possibleSet.append(temp2)
			possibleSet = possibleSet[2**index1:]
			index1 += 1
			if target in possibleSet :
				decision = "Possible"
				break

		return decision



test = ABBA()

print test.canObtain("A", "BABA")
