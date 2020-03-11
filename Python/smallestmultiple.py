from math import gcd
from sys import stdin

for line in stdin:
	nums = list(map(int,line.split()))

	prod = 1
	for num in nums:
		num = num//gcd(prod,num)
		prod *= num
	print(prod)