from sys import stdin
input()

for line in stdin:
	p,r,f = map(int,line.split())
	t = 0
	while p <= f:
		p *= r
		t += 1
	print(t)