from sys import stdin
from heapq import heappush,heappop

def main():
	n,s,d = map(int, input().split())
	graph = [list(map(int, line.split())) for line in stdin]
	visited = [False for i in range(n)]

	q = []
	heappush(q,(0,s))

	while q:
		t,i = heappop(q)
		visited[i] = True
		if i == d: break
		
		for j in range(n):
			if i == j or visited[j]: continue
			heappush(q,(t+graph[i][j],j))

	print(t)

if __name__ == "__main__": main()