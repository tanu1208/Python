deck = {'A':[11,11], 'K':[4,4], 'Q':[3,3], 'J':[20,2],
       'T':[10,10], '9':[14,0], '8':[0,0], '7':[0,0]}

total = 0
n, b = input().split()

for i in range(4*int(n)):
    card = input()
    if card[1] == b:
        total+=deck.get(card[0])[0]
    else:
        total+=deck.get(card[0])[1]
        
print(total)