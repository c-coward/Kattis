line = input()
pl1 = 'Player 1 wins.'
pl2 = 'Player 2 wins.'
while line != '0 0 0 0':
	rolls = [i for i in line.split(" ")]
	p1 = ''.join(reversed(sorted(rolls[:2])))
	p2 = ''.join(reversed(sorted(rolls[2:])))
	if p1 == p2:
		print('Tie.')
	elif p1 == '21' or p2 == '21':
		print(pl1) if p1 == '21' else print(pl2)
	elif p1[0] == p1[1]:
		if p2[0] == p2[1]:
			print(pl1) if int(p1) > int(p2) else print(pl2)
		else:
			print(pl1)
	elif p2[0] == p2[1]:
		print(pl2)
	else:
		print(pl1) if int(p1) > int(p2) else print(pl2)
	line = input()