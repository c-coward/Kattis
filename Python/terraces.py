from sys import stdin

def main():
	x,y = map(int,stdin.readline().split()) # Bounds of graph
	graph = [list(map(int,stdin.readline().split())) for _ in range(y)] # Height map
	parents = list(range(x*y)) # Parent array for union-find
	size = [1 for _ in range(x*y)]

	for i in range(y):
		for j in range(x):
			# Union all nodes of the same height
			if j+1<x and graph[i][j] == graph[i][j+1]:
				union(size,parents,i*x+j,i*x+j+1)
			if i+1<y and graph[i][j] == graph[i+1][j]:
				union(size,parents,i*x+j,i*x+j+x)

	# Keep track of good nodes and add their sizes
	# Uses union by size
	top_nodes = set(find(parents,x) for x in range(x*y))
	dirs = [(1,0),(0,1),(-1,0),(0,-1)]
	for i in range(y):
		for j in range(x):
			if find(parents,i*x+j) not in top_nodes: continue
			for dy,dx in dirs:
				if 0<=i+dy<y and 0<=j+dx<x and graph[i][j] > graph[i+dy][j+dx]:
					top_nodes.remove(find(parents,i*x+j))
					break

	count = sum(size[x] for x in top_nodes)

	# # Keep track of sets that leak into smaller sets
	# bad_parents = set()

	# dirs = [(1,0),(0,1),(-1,0),(0,-1)] # Check all four directions in graph
	# for i in range(y):
	# 	for j in range(x):
	# 		for dy,dx in dirs:
	# 			if not (0<=j+dx<x and 0<=i+dy<y): continue

	# 			if graph[i+dy][j+dx] < graph[i][j]: # Set can leak
	# 				bad_parents.add(find(parents,i*x+j))

	# # Count all nodes that aren't bad
	# count = 0
	# for i in range(x*y):
	# 	if find(parents,i) not in bad_parents:
	# 		count += 1

	print(count)

def union(size,parents,a,b):
	fa = find(parents,a)
	fb = find(parents,b)

	if fa == fb: return
	if size[fa] < size[fb]: fa,fb = fb,fa

	size[fa] += size[fb]
	parents[fb] = fa

def find(parents,a):
	if a == parents[a]:
		return a
	parents[a] = find(parents,parents[a])
	return parents[a]

main()