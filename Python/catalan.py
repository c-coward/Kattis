from sys import stdin
from math import factorial

outs = []
stdin.readline()
for line in stdin:
	x = int(line)
	catalan = factorial(2*x) // (factorial(x+1) * factorial(x))
	outs.append(str(catalan))

print('\n'.join(outs))