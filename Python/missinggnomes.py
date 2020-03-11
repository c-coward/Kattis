from sys import stdin

def main():
	outs = [] # List to hold output

	# Read in input
	n,m = map(int,stdin.readline().split())
	gnomes = [int(stdin.readline()) for _ in range(m)]

	# Find indices of missing gnomes and sort them
	missing = sorted(set(range(1,n+1)) - set(gnomes))

	i,j = 0,0

	# Merge the lists
	while i < m or j < n-m:
		if i == m:
			outs.append(str(missing[j]))
			j += 1
		elif j == n-m:
			outs.append(str(gnomes[i]))
			i += 1
		elif gnomes[i] < missing[j]:
			outs.append(str(gnomes[i]))
			i += 1
		else:
			outs.append(str(missing[j]))
			j += 1

	print('\n'.join(outs))

main()