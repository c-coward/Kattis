import math
try:
	while True:
		line = input().split(" ")
		x = int(line[0])
		y = int(line[1])
		print(math.abs(x-y))
except:
	pass