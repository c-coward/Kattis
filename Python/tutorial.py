from math import log

def main():
	m,n,t = map(int,input().split())
	if m >= time(n,t,m):
		print('AC')
	else:
		print('TLE')

def time(n,k,m):
	if k == 1:
		return f(n,m)
	elif k == 2:
		return 2**n
	elif k == 3:
		return n**4
	elif k == 4:
		return n**3
	elif k == 5:
		return n**2
	elif k == 6:
		return n*log(n,2)
	elif k == 7:
		return n

def f(n,m):
	prod = 1
	for i in range(n,0,-1):
		prod *= i
		if prod > m:
			return prod
	return prod

main()