import math

iterations = int(input())

for i in range(iterations):
	number = int(input())
	if number >= 1 & number <= 10:
		print(math.factorial(number)%10)
	else:
		break