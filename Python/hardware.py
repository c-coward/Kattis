tests = int(input())
outs = []
for t in range(tests):
	address = input()
	nadd = input()
	na = nadd.split()
	digs = ''
	addresses = 0
	while addresses < int(na[0]):
		line = input().split()
		if line[0] == '+':
			for num in range(int(line[1]),int(line[2])+1,int(line[3])):
				digs += str(num)
				addresses += 1
		else:
			digs += line[0]
			addresses += 1
	outs.append(address)
	outs.append(nadd)
	totsum = 0
	for i in range(10):
		digsum = sum(j == str(i) for j in digs)
		totsum += digsum
		outs.append('Make '+ str(digsum) + ' digit '+ str(i))
	outs.append("In total " + str(totsum) + (' digits' if totsum > 1 else ' digit'))
print('\n'.join(outs))