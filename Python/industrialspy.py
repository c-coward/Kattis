from itertools import permutations
from math import floor
from sys import stdin

def sieve(n):
	primes = [1]*n
	primes[0],primes[1] = 0,0

	for i in range(2,floor(n**.5)+1):
		if not primes[i]: continue
		for j in range(i**2,n,i):
			primes[j] = 0
	return primes

n = int(input())
primes = sieve(10000000)
for i in range(n):
	l = input()
	count = 0
	ints = []
	seen = set()
	for j in range(1,len(l)+1):
		perm = permutations(l,j)
		for p in perm:
			ints.append(int(''.join(list(p))))
	for j in ints:
		if j in seen: continue
		if primes[j]: count += 1
		seen.add(j)
	print(count)