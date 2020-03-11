from sys import stdin

def find(parents,child):
	if parents[child] == child: return child

	parents[child] = find(parents,parents[child])
	return parents[child]

def union(parents,x, y):
	parents[find(parents,x)] = find(parents,y)

def main():
	line1 = [int(i) for i in stdin.readline().split()]
	parents = list(range(line1[0]))

	lines = stdin.readlines()
	for line in lines:
		line = line.strip().split()
		union(parents,int(line[0])-1, int(line[1])-1)

	i,j = 0,line1[0]-1

	canSwap = 1
	while (i < j):
		if find(parents,i) != find(parents,j):
			canSwap = 0
			break
		i += 1
		j -= 1

	print("Yes" if canSwap else "No")

main()