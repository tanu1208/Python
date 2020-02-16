x, y, n = map(int,input().split())

for i in range(1,n+1):
    if i%x==0 and i%y == 0:
        value = 'FizzBuzz'
    elif i%y==0:
        value = 'Buzz'
    elif i%x == 0:
        value = 'Fizz'
    else:
        value = i
    print(value)