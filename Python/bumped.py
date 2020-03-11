from sys import stdin
from math import inf
from heapq import heappop,heappush

def main():
	c,r,f,s,e = map(int,input().split())
	edges = [set() for i in range(c)]

	inp = [tuple(map(int,line.strip().split())) for line in stdin]
	roads = inp[:r]
	flights = inp[r:]

	for ro in roads:
		start,stop,step = ro
		edges[start].add((stop,step))
		edges[stop].add((start,step))

	ds = dijkstra(s,c,edges)
	de = dijkstra(e,c,edges)

	mindist = ds[e]

	for fl in flights:
		start,stop = fl

		mindist = min(ds[start] + de[stop],mindist)

	print(mindist)

def dijkstra(start,c,edges):
	q = []
	dists = [inf for i in range(c)]
	heappush(q,(0,start))

	while q:
		d,i = heappop(q)
		if dists[i] != inf: continue

		dists[i] = d

		neighbs = edges[i]

		for n in neighbs:
			j,t = n
			if dists[j] == inf:
				heappush(q,(d+t,j))

	return dists

if __name__ == "__main__": main()