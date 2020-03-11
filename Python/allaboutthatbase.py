# Uses base and value converter from geeksforgeeks.org
# https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/

def main():
	bases = '0123456789abcdefghijklmnopqrstuvwxyz0'
	n = int(input())
	for _ in range(n):
		exp = input().split()
		l1,l2 = exp[0],exp[2]
		right = exp[-1]

		possible_bases = []
		for i in range(1,37):
			e1 = convert(l1,i)
			e2 = convert(l2,i)
			e3 = convert(right,i)

			if (e1 is not None and e2 is not None and e3 is not None):
				if eval(f'{e1} {exp[1]} {e2}') == e3:
					possible_bases.append(bases[i])

		if not possible_bases: possible_bases.append('invalid')
		print(''.join(possible_bases))

def convert(numstr,base):
	if base == 1:
		for char in numstr:
			if char != '1': return None
		return len(numstr)

	l = len(numstr)
	p = 1
	n = 0

	for i in range(l-1,-1,-1):
		if val(numstr[i]) >= base:
			return None

		n += val(numstr[i])*p
		p *= base

	return n

def val(char):
	if '0' <= char <= '9':
		return ord(char) - ord('0')
	else:
		return ord(char) - ord('a') + 10

main()