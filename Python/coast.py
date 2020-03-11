from sys import stdin
from collections import deque

def main():
	n,m = map(int,stdin.readline().split())

	graph = ['0'*(m+2)]
	for _ in range(n):
		graph.append('0' + stdin.readline().strip() + '0')
	graph.append('0'*(m+2))

	visited = [[False for _ in range(m+2)] for _ in range(n+2)]
	visited[0][0] = True

	count = 0
	q = deque()
	q.append((0,0))
	dirs = [(0,1),(1,0),(0,-1),(-1,0)]

	while q:
		x,y = q.popleft()

		for i,j in dirs:
			if 0<=x+i<m+2 and 0<=y+j<n+2 and not visited[y+j][x+i]:
				if graph[y+j][x+i] == '0':
					q.append((x+i,y+j))
					visited[y+j][x+i] = True
				else:
					count += 1

	print(count)

main()