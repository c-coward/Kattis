line = input()
combos = ['RLB','RBL','BLR','BRL','LRB','LBR']

i = 0
while i < len(line)-2:
	new = line[i:i+3]
	if new in combos:
		print('C',end='')
		i += 3
	else:
		if line[i] == 'R':
			print('S',end='')
		if line[i] == 'B':
			print('K',end='')
		if line[i] == 'L':
			print('H',end='')
		i += 1
for l in line[i:]:
	if l == 'R':
		print('S',end='')
	if l == 'B':
		print('K',end='')
	if l == 'L':
		print('H',end='')
