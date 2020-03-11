from sys import stdin
from heapq import heappop,heappush

def main():
	r,c = map(int,input().split())
	graph = []
	for line in stdin:
		graph.append(list(map(int, line.split())))

	q = []
	for i in range(r): heappush(q,(graph[i][0],i,0))

	visited = [0 for i in range(r*c)]
	md = -1
	while q:
		d,y,x = heappop(q)
		
		if md < d: md = d
		if x == c-1: break
		if x < c-1 and not visited[y*c+x+1]:
			heappush(q, (graph[y][x+1],y,x+1))
			visited[y*c+x+1] = 1
		if y < r-1 and not visited[y*c+c+x]:
			heappush(q, (graph[y+1][x],y+1,x))
			visited[y*c+c+x] = 1
		if y > 0 and not visited[y*c-c+x]:
			heappush(q, (graph[y-1][x],y-1,x))
			visited[y*c-c+x] = 1
		if x > 0 and not visited[y*c+x-1]:
			heappush(q, (graph[y][x-1],y,x-1))
			visited[y*c+x-1] = 1
	print(md)

if __name__ == "__main__": main()