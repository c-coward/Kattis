line1 = input().split(" ")

n = int(line1[0])
m = int(line1[1])

lines = []
for i in range(n):
	lines.append(input())

count = 1
for i in range(m):
	found = True
	for l in lines:
		if l[i] != "_":
			found = False
	if found:
		count += 1

print(count)