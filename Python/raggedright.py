lines = []
n = -1
try:
	while 1:
		line = input()
		if len(line) > n:
			n = len(line)
		lines.append(line)
except:
	tot = 0
	for i in range(len(lines) - 1):
		m = len(lines[i])
		tot += (n-m)**2
	print(tot)