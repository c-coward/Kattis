from sys import stdin
from collections import deque

def main():
	n = int(input())
	blocked = []
	for j in range(n):
		line = stdin.readline()
		for i in range(n):
			if line[i] == 'K': start = (j,i,0)
			if line[i] == '#': blocked.append((j,i))

	dirs = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
	visited = set()
	visited.add(start)

	q = deque()
	q.append((start))
	found = False
	while q:
		y,x,t = q.popleft()
		if y == 0 and x == 0:
			found = True
			break
		for d in dirs:
			i,j = d
			if not (0 <= y+i < n and 0 <= x+j < n and (y+i,x+j) not in blocked and (y+i,x+j) not in visited): continue
			q.append((y+i,x+j,t+1))
			visited.add((y+i,x+j))
	print(t if found else -1)

main()