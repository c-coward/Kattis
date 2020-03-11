n,w,h = map(int,input().split())
d = w**2+h**2
for i in range(n):
	m = int(input())
	if m**2 <= d:
		print('DA')
	else:
		print('NE')