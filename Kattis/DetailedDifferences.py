iterations = int(input())

for i in range(iterations):
	diff = []
	txt = input()
	txt2 = input()

	for x,y in zip(txt, txt2):
		if x == y:
			diff.append(".")
		else:
			diff.append("*")

	print(txt)
	print(txt2)

	print(*diff, "\n", sep="")
