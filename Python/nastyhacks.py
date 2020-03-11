n = int(input())
for i in range(n):
	r,e,c = map(int,input().split())
	d = e-c-r
	if d < 0:
		print('do not advertise')
	elif d > 0:
		print('advertise')
	else:
		print('does not matter')