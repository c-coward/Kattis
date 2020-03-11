tests = int(input())
for t in range(tests):
	input()
	mg = [int(i) for i in input().split(' ')]
	gSize = mg[0]
	mSize = mg[1]
	gArmy = [int(i) for i in input().split(' ')]
	gArmy.sort()
	mArmy = [int(i) for i in input().split(' ')]
	mArmy.sort()
	gC = 0
	mC = 0
	while (gC < len(gArmy) and mC < len(mArmy)):
		if (mArmy[mC] > gArmy[gC]):
			gC += 1
		else:
			mC += 1
	if (mC == len(mArmy) and gC == len(gArmy)):
		print('uncertain')
	elif mC == len(mArmy):
		print('Godzilla')
	else:
		print('MechaGodzilla')