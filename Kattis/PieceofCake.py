n, h, v = input().split()
n = int(n)
h = int(h)
v = int(v)

result = max(h, n - h) * max(v, n - v) * 4

print(result)
