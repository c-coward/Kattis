import math

n = int(input())
x = round(math.pow(n, 1/9))

def meow(m):
	if n % (m**9) == 0:
		return m
	else:
		return meow(m-1)

print(meow(x))