from sys import stdin
from math import inf

def find(p,a):
	if a != p[a]:
		p[a] = find(p,p[a])
	return p[a]

def union(p,a,b):
	p[find(p,a)] = find(p,b)

def kruskal(parents,edges):
	mst = set()
	edges.sort()

	for e in edges:
		weight,start,stop = e
		if find(parents,start) != find(parents,stop):
			union(parents,start,stop)
			mst.add(e)
	return mst

def main():
	while 1:
		n,e = map(int,stdin.readline().split())
		if n == 0: break

		parents = [i for i in range(n)]
		edges = []

		for i in range(e):
			start,stop,step = map(int,stdin.readline().split())
			if start > stop: start,stop = stop,start
			edges.append((step,start,stop))

		mst = kruskal(parents,edges)

		sum_ = sum(m[0] for m in mst)
		tree = sorted((a,b) for _,a,b in mst)

		if len(tree) == n-1:
			print(sum_)
			for a,b in tree: print(a,b)
		else:
			print("Impossible")

if __name__ == "__main__": main()