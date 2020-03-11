line = input().split(" ")

cards = {}
for l in line:
	if l[0] in cards:
		cards[l[0]] += 1
	else:
		cards[l[0]] = 1

greatest = 0
for c in cards:
	if cards[c] > greatest:
		greatest = cards[c]

print(greatest)