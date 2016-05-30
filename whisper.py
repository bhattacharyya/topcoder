#!/usr/bin/python
import re
class Whisper:
	def __init__(self):
		return None

	def toWhom(self,usernames,typed):
		user = "user is not logged in"
		names = list(usernames)
		names.sort(key=len, reverse=True)
		for i in names:
			i = i+" "
			if bool(re.search(i.lower(), typed.lower())) == True and bool(re.search(i+" ".lower(), typed.lower())) == False:
				user = i.strip()
				break
		if typed[0:5].lower() != "/msg ".lower():
			user = "not a whisper"
		if typed[0:6].lower() == "/msg  ".lower():
			user = "user is not logged in"
		return user

test = Whisper()

print test.toWhom({"me"}, "/msg  me hi")



