pos = 1
moves = input()
for m in moves:
	if m == 'A':
		pos = 2 if pos == 1 else 1 if pos == 2 else pos
	elif m == 'B':
		pos = 3 if pos == 2 else 2 if pos == 3 else pos
	else:
		pos = 3 if pos == 1 else 1 if pos == 3 else pos
print(pos)