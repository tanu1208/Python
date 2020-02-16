t = int(input())
for i in range(t):
	trips = {}
	n = int(input())
	for j in range (n):
		trips[input()] = 1
	print(len(trips))