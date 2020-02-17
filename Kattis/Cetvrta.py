def findPoint(p):
	occurance = [p.count(p[0]), p.count(p[1]), p.count(p[2])]
	odd = min(occurance)
	point = occurance.index(odd)
	return p[point]

def getPoints(x, y):
	point_x = findPoint(x)
	point_y = findPoint(y)
	return point_x, point_y

known_x = []
known_y = []

for i in range(3):
	x,y = map(int,input().split())
	known_x.append(x)
	known_y.append(y)

points = getPoints(known_x, known_y)

print(points[0], points[1])