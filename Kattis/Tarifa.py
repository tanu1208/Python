tarif = int(input())
month = int(input())
total = 0

for i in range(month):
    total+=(tarif-int(input()))
    
print(total+tarif)