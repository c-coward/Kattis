from math import floor
from sys import stdin

def sieve(n):
	primes = [True for _ in range(n)]
	primes[0], primes[1] = False, False

	i = 0
	while i * i <= n:
		if primes[i]:
			for j in range(i**2, n, i):
				primes[j] = False
		i += 1

	return primes


def main():
	n = int(input())
	primes = sieve(32001)

	for line in stdin:
		k = int(line)
		poss = []
		count = 0

		i = 0
		while i <= k//2:
			if primes[i] and primes[k - i]:
				poss.append(f'{i}+{k - i}')
			i += 1

		print(f'{k} has {len(poss)} representation(s)')
		print('\n'.join(poss))
		print()

if __name__ == '__main__':
	main()