from math import log

def factor(n):
	factors = []

	for i in range(1,int((n**.5))+1):
		if n % i == 0:
			factors.append(i)

	for fac in factors[::-1]:
		if n//fac == factors[-1]: continue
		factors.append(n//fac)

	return factors

def main():
	n = int(input())
	factors = factor(n)

	if n == 1:
		print('no')
		return
	
	prime = factors[1]
	total = 1
	for i in range(len(factors)-1):
		if total != factors[i]:
			print('no')
			return

		total *= prime

	print('yes')

main()