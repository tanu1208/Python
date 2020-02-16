a = int(input())
count = 0
temp = input().split()

for i in temp:
    if int(i) < 0:
    	count += 1

print(count)