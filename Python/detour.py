from heapq import heappop as pop, heappush as push
from collections import deque
from sys import stdin

def main():
	n,m = map(int,stdin.readline().split())
	
	# Read in all the edge data
	edges = {}
	for _ in range(m):
		u,v,w = map(int,stdin.readline().split())
		if u not in edges: edges[u] = set()
		if v not in edges: edges[v] = set()
		edges[u].add((v,w))
		edges[v].add((u,w))

	# Use Dijkstra's algorithm to find the best edges from each node to the end
	# Start from the last intersection (1) and essentially travel backwards
	q = []
	push(q,(0,1,-2))
	path_to = [-1 for _ in range(n)] # -1 will represent an unvisited point
	while q:
		d,c,f = pop(q) # Distance, Current, Following
		if path_to[c] != -1: continue # Node has been found more cheaply
		path_to[c] = f

		for e,w in edges[c]:
			if path_to[e] != -1: continue

			push(q,(d+w,e,c))

	# Use a DFS to find any path that does not take the edges found earlier
	path_from = [-1 for _ in range(n)]
	path_from[0] = -2
	s = deque()
	s.append((0,0))

	while s:
		d,c = s.pop() # Distance, Current position
		if c == 1: break
			
		for e,w in edges[c]:
			if (path_from[e] != -1
				 or path_to[c] == e): continue # This represents an edge found earlier, so ignore it
			path_from[e] = c
			s.append((d+w,e))

	
	if path_from[1] == -1: # No useable edges led to 1
		print('impossible')
	else:
		# Iterate backwards through the path, finding all edges used
		curr = 1
		outs = []
		while curr != -2:
			outs.append(str(curr))
			curr = path_from[curr]
		print(len(outs),' '.join(outs[::-1]))

main()