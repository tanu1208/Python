from decimal import Decimal

iterations = int(input())

for i in range(iterations):
	b,p = map(float,input().split())
	bpm = Decimal(60 * b / p)
	var = Decimal(60 / p)
	print(round(bpm-var,4), round(bpm,4), round(bpm+var,4))