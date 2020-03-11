shares = 0
cost = 0

line = input().split(" ")
while True:
	if line[0] == "buy":
		x = int(line[1])
		y = int(line[2])
		cost = (shares*cost + x*y)/(shares+x)
		shares += x
	elif line[0] == "sell":
		x = int(line[1])
		shares -= x
	elif line[0] == "split":
		x = int(line[1])
		shares *= x
		cost /= x
	elif line[0] == "merge":
		x = int(line[1])
		shares = int(shares/x)
		cost *= x
	elif line[0] == "die":
		y = int(line[1])
		if y > cost:
			print(shares*(y - 0.3*(y - cost)))
		else:
			print(shares*y)
		break
	line = input().split(" ")
