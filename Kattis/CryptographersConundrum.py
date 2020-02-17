text = input().upper()
chiper = "PER"

days = 0
index = 0

for i in text:
	if index > 2:
		index = 0

	if chiper[index] != i:
		days += 1

	index += 1

print(days)