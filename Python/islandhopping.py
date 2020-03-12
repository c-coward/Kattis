from sys import stdin
from heapq import heappop as pop,heappush as push

def main():
	t = int(stdin.readline())

	for _ in range(t):
		n = int(stdin.readline())
		islands = []
		for _ in range(n):
			a,b = map(float,stdin.readline().split())
			islands.append((a,b))

		print(prims(islands,n))

def prims(islands,n):
	cost = 0
	visited = [False for _ in range(n)]
	q = []
	push(q,(0,0))
	nodes = 0

	while nodes < n and q:
		d,c = pop(q)

		if visited[c]: continue
		visited[c] = True
		cost += d
		nodes += 1

		for i in range(n):
			if visited[i]: continue

			new_dist = dist(islands[i],islands[c])
			push(q,(new_dist,i))

	return cost

def dist(a,b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5

main()