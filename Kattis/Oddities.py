iterations = int(input())

for i in range(iterations):
	number = int(input())
	if number%2 == 0:
		print(number, "is even")
	else:
		print(number, "is odd")