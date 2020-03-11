tests = int(input())
for t in range(tests):
	line = [int(i) for i in input().split()]
	decisions = [input() for i in range(line[0])]

	decide = ''
	for i in range(line[1]):
		sum1 = sum(int(d[i]) for d in decisions)
		sum0 = sum(not int(d[i]) for d in decisions)
		
		decide += str(int(sum1 > sum0))
	print(decide)