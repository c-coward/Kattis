coords = []

def determ(t1,t2):
	return t1[0]*t2[1]-t1[1]*t2[0]

n = int(input())
while n != 0:
	for i in range(n):
		x,y = map(int,input().split())
		coords.append((x,y))
	sum_ = 0
	for i in range(n-1):
		sum_ += determ(coords[i],coords[i+1])
	sum_ += determ(coords[-1],coords[0])
	dir_ = 'CCW'
	if sum_ < 0:
		dir_ = 'CW'
		sum_ *= -1
	print(dir_,sum_/2)
	n = int(input())
	coords = []