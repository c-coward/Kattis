from sys import stdin
from heapq import heappop,heappush

def main():
	outs = []
	while 1:
		n,m,qu,s = map(int,stdin.readline().split())
		if n==m==qu==s==0: break

		dists = ['Impossible' for i in range(n)]
		edges = [set() for i in range(n)]

		for i in range(m):
			u,v,t,p,d = map(int,stdin.readline().split())
			edges[u].add((v,t,p,d))

		q = []
		heappush(q,(0,s))

		while q:
			dist,index = heappop(q)
			if dists[index] != 'Impossible': continue
			
			dists[index] = dist

			for v,t,p,d in edges[index]:
				if dists[v] != 'Impossible': continue

				if dist <= t:
					heappush(q,(t+d,v))

				else:
					if p == 0: continue

					extra = ((dist-t)%-p)
					heappush(q,(dist-extra+d,v))

		for i in range(qu):
			outs.append(str(dists[int(stdin.readline())]))

		outs.append('')
	print('\n'.join(outs))

if __name__ == "__main__": main()