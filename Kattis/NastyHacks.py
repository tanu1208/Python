iterations = int(input())
for i in range(iterations):
    numbers = list(map(int,input().split()))
    diff = numbers[1]-numbers[2]
    revenue = numbers[0]
    if diff > revenue:
        output = "advertise"
    elif diff == revenue:
        output = "does not matter"
    elif diff < revenue:
        output = "do not advertise"
    print(output)