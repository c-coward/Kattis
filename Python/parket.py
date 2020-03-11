from math import floor
r,b = [int(i) for i in input().split()]

def factor(n):
	arr = []
	for i in range(1,floor(n**.5)+1):
		if n % i == 0:
			arr.append(i)
	return arr

factors = factor(b)

for f in factors:
	cof = b//f
	height, width = f+2, cof+2
	if r == 2*height + 2*width - 4:
		print(width,height)
		break