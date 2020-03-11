def main():
	n,m = map(int,input().split())
	graph = [list(input()) for _ in range(n)]
	dirs = [(1,0),(0,1),(-1,0),(0,-1)]

	for i in range(n):
		for j in range(m):
			if graph[i][j] == '#': continue # Water

			adj = set()
			for y,x in dirs:
				if 0 <= y+i < n and 0 <= x+j < m:
					adj.add(graph[y+i][x+j])

			if 'E' not in adj:
				graph[i][j] = 'E'

	for g in graph: print(''.join(g))

main()