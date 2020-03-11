from math import gcd
from sys import stdin

def main():
	n = int(input())
	outs = []

	for line in stdin:
		n1,d1,op,n2,d2 = line.split()
		n1,d1,n2,d2 = int(n1),int(d1),int(n2),int(d2)

		if op == '-':
			n2 = -1*n2
			op = '+'
		if op == '+':
			n3 = n1*d2 + n2*d1
			d3 = d1*d2
		if op == '/':
			n2,d2 = d2,n2
			op = '*'
		if op == '*':
			n3 = n1*n2
			d3 = d1*d2

		if d3 < 0:
			n3 *= -1
			d3 *= -1

		gcf = gcd(n3,d3)
		n3,d3 = n3//gcf,d3//gcf
		outs.append('%d / %d' % (n3,d3))

	print('\n'.join(outs))

if __name__ == "__main__": main()