b,d,c,l = map(int,input().split())

outs = []
for i in range(l//b+1):
	for j in range(l//d+1):
		for k in range(l//c+1):
			if i*b + j*d + k*c == l:
				outs.append("%s %s %s"%(i,j,k))
print('\n'.join(outs) if outs else 'impossible')