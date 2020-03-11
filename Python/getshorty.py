from sys import stdin
from math import inf
from heapq import heappop,heappush

def main():
	while 1:
		line = stdin.readline().strip()

		if line == '0 0': break

		inter,corr = map(int,line.split())
		rinter = range(inter)
		edges = [set() for i in rinter]
		visited = [False for i in rinter]

		for i in range(corr):
			l = stdin.readline().split()
			s,e,f = int(l[0]),int(l[1]),float(l[2])
			edges[s].add((e,f))
			edges[e].add((s,f))

		q = []
		heappush(q,(0,0))

		while q:
			h,i = heappop(q)
			h = 1 - h
			visited[i] = True

			if i == inter-1: break

			neighbs = edges[i]
			for n in neighbs:
				j,m = n
				if not visited[j]:
					heappush(q,(1-h*m,j))

		print('%.4f' % h)

if __name__ == "__main__": main()