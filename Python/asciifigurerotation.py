translate = {
	'+': '+', '-': '|', '|': '-', ' ': ' '
}

first = True
while 1:
	n = int(input())

	if not n: break
	
	if not first: print()

	if first:
		first = False
	
	shape = []
	longest = 0

	for i in range(n):
		l = list(input())
		longest = max(longest,len(l))
		shape.append(l)

	for s in shape:
		s += [' ' for j in range(longest-len(s))]

	revshape = []

	for j in range(longest):
		temp = []
		for i in range(n-1,-1,-1):
			temp.append(translate[shape[i][j]])
		temp = ''.join(temp)
		temp = temp.rstrip()
		revshape.append(temp)

	for r in revshape: print(''.join(r))
