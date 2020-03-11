from sys import stdin
n = int(stdin.readline())
while n != -1:
	connections = []
	for i in range(n):
		row = stdin.readline().split()
		connections.append({j for j in range(n) if int(row[j])})

	weak = []
	for r in range(n):
		isWeak = True

		for num in connections[r]:
			if bool(connections[num] & connections[r]):
				isWeak = False
				break
				
		if isWeak:
			weak.append(str(r))

	print(' '.join(weak))

	n = int(stdin.readline())