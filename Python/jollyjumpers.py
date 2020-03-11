from math import fabs

try:
	while True:
		line = input().split(" ")
		n = list(range(1,len(line)-1))

		diffs = []
		for i in n:
			diff = fabs(int(line[i]) - int(line[i+1]))
			diffs.append(int(diff))
		diffs = sorted(diffs)

		if diffs == n:
			print("Jolly")
		else:
			print("Not Jolly")
except:
	pass