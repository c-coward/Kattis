queens = []
for i in range(8):
	line = input()
	for j in range(8):
		if line[j] == '*':
			queens.append((i,j))

valid = True
if len(queens) != 8: valid = False
for i in range(8):
	if not valid: break
	d = 1
	y,x = queens[i]
	while d < 8:
		if (y,x+d) in queens: valid = False
		if (y+d,x) in queens: valid = False
		if (y+d,x+d) in queens: valid = False
		if (y+d,x-d) in queens: valid = False
		if not valid: break
		d += 1

print('valid' if valid else 'invalid')