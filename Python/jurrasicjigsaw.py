from sys import stdin
from math import inf

def main():
	n,k = map(int,input().split())
	samples = [line.strip() for line in stdin]
	parents = list(range(n))
	edges = []

	for i in range(n-1):
		for j in range(i+1,n):
			diff = finddiff(samples[i],samples[j])
			edges.append((diff,i,j))

	mst,sum_ = kruskal(parents,edges)
	print(sum_)
	for a,b in mst: print(a,b)

def finddiff(str1,str2):
	diff = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]: diff += 1
	return diff

def union(parents,u,v):
	parents[find(parents,v)] = find(parents,u)

def find(parents,n):
	if parents[n] != n:
		parents[n] = find(parents,parents[n])
	return parents[n]

def kruskal(parents,edges):
	mst = []
	edges.sort()
	sum_ = 0

	for w,u,v in edges:
		if find(parents,u) != find(parents,v):
			union(parents,u,v)
			mst.append((u,v))
			sum_ += w

	return mst,sum_

if __name__ == "__main__": main()