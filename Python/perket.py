from itertools import combinations
from math import inf

n = int(input())
ingredients = [tuple(map(int, input().split())) for i in range(n)]

combos = []
for i in range(1,n+1):
	for c in combinations(ingredients,i):
		combos.append(list(c))

mdiff = inf
for combo in combos:
	prod = 1
	s = 0
	for c in combo:
		prod *= c[0]
		s += c[1]
	if abs(prod-s) < mdiff: mdiff = abs(prod-s)

print(mdiff)