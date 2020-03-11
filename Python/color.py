line = [int(i) for i in input().split(" ")]

socks = [int(i) for i in input().split(" ")]	
socks.sort()

curr = 0
start = 0
loads = 0

while curr <= line[0]:
	if curr == line[0]:
		if (curr - start) > 0:
			loads += 1
		break
	if (curr - start) == (line[1]):
		start = curr
		loads += 1

	if (socks[curr] - socks[start]) <= line[2]:
		curr += 1
	else:
		start = curr
		loads += 1

print(loads)