#!/usr/bin/python

class Substitute:
	def __init__(self):
		return None

	def getValue(self,key,code):
		answer = ""
		codem = list(key)
		mapped = {}
		for i in range(0,10):
			print codem[i]
			mapped[codem[i]] = i
		word = list(code)
		for k in word:
			if k in codem:
				if mapped[k] == 9:
					mapped[k] = -1
				answer += str(mapped[k]+1)
			else:
				answer += ""
		return int(answer)	

test = Substitute()
print test.getValue("CRYSTALBUM", "MMA")

