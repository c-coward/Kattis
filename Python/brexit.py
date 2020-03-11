from sys import stdin
from queue import SimpleQueue as sq

c,t,me,f = [int(i) for i in input().split()]
me,f = me-1,f-1
partners = [set() for i in range(c)]
sizes = [0]*c

for line in stdin:
	a,b = [int(i)-1 for i in line.strip().split()]
	partners[a].add(b)
	partners[b].add(a)
	sizes[a] += 1
	sizes[b] += 1

q = sq()
sizes[f] *= 2
left = [0]*c
q.put(f)

while not q.empty():
	curr = q.get()
	if left[curr]: continue
	if len(partners[curr]) <= sizes[curr]//2:
		left[curr] = 1
		for p in partners[curr]:
			if left[p]: continue
			partners[p].remove(curr)
			q.put(p)
	if len(partners[me]) <= sizes[me]//2: break

print(['stay','leave'][len(partners[me]) <= sizes[me]//2])