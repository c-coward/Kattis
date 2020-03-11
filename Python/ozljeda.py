from sys import stdin

def main():
	# Read in the given length and list
	n = int(stdin.readline()) + 1 # Add one for later
	xor = list(map(int,stdin.readline().split()))

	# Find the n+1th element, completing the cycle
	last = 0
	for e in xor:
		last = last ^ e
	xor.append(last)

	# Create running ^ sums from each end, allowing for quick queries
	left = [None for _ in range(n)]
	right = [None for _ in range(n)]
	l,r = 0,0
	for i in range(n):
		l ^= xor[i]
		r ^= xor[n-1-i]

		left[i] = l
		right[n-1-i] = r

	# Read queries and add to output queue
	outs = []
	for _ in range(int(stdin.readline())):
		a,b = map(int,stdin.readline().split())
		
		# Shift right 1 and find their index
		a,b = map(lambda x: (x-1) % n,(a,b))
		total = left[b] ^ right[a]

		outs.append(str(total))

	# Print outputs
	print('\n'.join(outs))

main()

"""

a,b,c,d,e
a^b^c^d = e
b^c^d^e = a (b,c,d cancel)

a^b = b^c^d^e ^ a^c^d^e = a^b
a^b^c^d^e^c^d^e = a^b = c^d^e
from a to b == from b+1 to 
ie: from 1,4 = from 4,1+5 (non inclusive of endpoints)

"""