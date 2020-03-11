n = int(input())
for i in range(n):
	line = input().replace('.','')
	complete = True
	backpack = []
	for l in line:
		if l in '$|*':
			backpack.append(l)
		if l in 'btj':
			if not backpack:
				complete = False
				break
			curr = backpack.pop()
			if (((l == 'b') and (curr in '|*'))
			 or ((l == 't') and (curr in '$*'))
			 or ((l == 'j') and (curr in '$|'))):
				complete = False
				break
	if backpack:
		complete = False
	print('YES' if complete else 'NO')