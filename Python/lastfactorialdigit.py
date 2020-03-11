from math import factorial as f

t = int(input())

for i in range(t):
	x = str(f(int(input())))
	print(x[len(x)-1])