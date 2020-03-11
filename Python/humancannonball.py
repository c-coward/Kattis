from math import hypot
from heapq import heappush,heappop
ax,ay = map(float,input().split())
bx,by = map(float,input().split())

n = int(input())
graph = [tuple(map(float,input().split())) for i in range(n)]
graph.append((bx,by))
visited = set()

q = []

first = True
heappush(q,(0,ax,ay))
while q:
	t,x,y = heappop(q)
	visited.add((x,y))
	if (x,y) == (bx,by):
		break
	if first:
		first = False
		for c in graph:
			xc,yc = c
			ctime = hypot(x-xc,y-yc)/5
			heappush(q,(ctime,xc,yc))
	else:
		for c in graph:
			if c in visited: continue
			xc,yc = c
			cdist = hypot(x-xc,y-yc)
			t1 = cdist/5
			t2 = abs(50-cdist)/5 + 2
			time = t1 if t1 < t2 else t2

			heappush(q,(t+time,xc,yc))
print(t)