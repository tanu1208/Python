from decimal import Decimal

cost = float(input())
iterations = int(input())

area = 0
for i in range(iterations):
    w,l = map(float,input().split())
    area+=(w*l)

print(round(area*cost,8))
