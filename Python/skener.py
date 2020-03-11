r,c,zr,zc = map(int,input().split())
article = [input() for i in range(r)]

output = []

for l in article:
	s = ''
	for ch in l:
		s += ch*zc
	for i in range(zr): output.append(s)

for o in output: print(o)