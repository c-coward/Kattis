from math import pi,e,log,floor
from sys import stdin

def f(n):
	if n > 2:
		return 1+log(2*pi*n,10)/2+n*log(n/e,10)
	else:
		return 1

for line in stdin:
	x = int(line)
	print(floor(f(x)))