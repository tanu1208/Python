at_bats = int(input())
plays = input().split()
total = 0

for i in plays:
    if int(i) < 0:
        at_bats+=int(i)
    else:
        total+= int(i)

print(total/at_bats)
