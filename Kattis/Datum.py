import datetime

d,m = map(int,input().split())

day = datetime.datetime(2009, m, d).weekday()
days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Saturday', 'Sunday']

print(days[day])