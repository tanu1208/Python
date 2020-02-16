import math
nwh = list(map(int,input().split()))
diagnol = math.sqrt(nwh[1]**2+nwh[2]**2)

for i in range(nwh[0]):
    length = int(input())
    if length <= diagnol:
        print('DA')
    else:
        print('NE')