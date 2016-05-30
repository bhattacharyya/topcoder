#!/usr/bin/python

number = raw_input("Enter an integer: ")
steps = 0
primeDetected = False

p = int(number)

def isPrime(n):
	"""Returns True if n is prime."""
	if n == 1:
		return False
	if n == 2:
		return True
	if n == 3:
		return True
	if n % 2 == 0 and n != 1:
		return False
	if n % 3 == 0 and n != 1:
		return False

	i = 5
	w = 2

	while i * i <= n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True

def sumOfSquareDigits(n):
	sum = 0
	for j in str(n):
		sum += (int(j) ** 2)
			
	return sum

for k in range(1, p+1):

	if isPrime(p) == True:
		steps += 1
		primeDetected = True
		break

	p = sumOfSquareDigits(p)
	if p != 1 :
		steps += 1


if steps == 0 or primeDetected == False:
	steps = -1
print "Steps = " , steps

