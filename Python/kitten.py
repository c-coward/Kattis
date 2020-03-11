k = int(input())

line = input().split(" ")

branches = {}

while int(line[0]) != -1:
	first = int(line[0])

	rest = [int(line[i]) for i in range(1,len(line))]

	for i in rest:
		branches[i] = first

	line = input().split(" ")

curr = k

while curr in branches:
	print(curr, end = " ")
	curr = branches[curr]

print(curr)