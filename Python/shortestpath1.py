from heapq import heappop,heappush
from sys import stdin

def main():
	outs = []
	while 1:
		n,e,q,s = map(int,stdin.readline().split())
		if n==e==q==s==0:
			break

		dists = ['Impossible' for i in range(n)]
		edges = [set() for i in range(n)]

		for i in range(e):
			u,v,w = map(int,stdin.readline().split())
			edges[u].add((v,w))

		pq = []
		heappush(pq,(0,s))

		while pq:
			d,i = heappop(pq)
			if dists[i] != 'Impossible': continue
			dists[i] = d

			for j,w in edges[i]:
				if dists[j] == 'Impossible':
					heappush(pq,(d+w,j))

		for i in range(q):
			outs.append(str(dists[int(stdin.readline())]))
		outs.append('')

	print('\n'.join(outs))

if __name__ == "__main__": main()