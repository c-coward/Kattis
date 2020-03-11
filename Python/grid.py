from sys import stdin
from collections import deque

def main():
	n,m = map(int,stdin.readline().split())
	dirs = [(1,0),(0,1),(-1,0),(0,-1)]
	graph = [[int(i) for i in stdin.readline().strip()] for _ in range(n)]
	dists = [[-1 for _ in range(m)] for _ in range(n)]
	q = deque()
	q.append((0,0,0))

	while q:
		d,y,x = q.popleft()
		if (y,x) == (n-1,m-1): break
		mult = graph[y][x]

		for i,j in dirs:
			dy,dx = y+mult*i,x+mult*j
			if 0 <= dy < n and 0 <= dx < m and dists[dy][dx] == -1:
				q.append((d+1,dy,dx))
				dists[dy][dx] = d+1

	print(dists[n-1][m-1])

main()