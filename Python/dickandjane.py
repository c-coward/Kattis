from sys import stdin

def main():
	for line in stdin:
		s, p, y, j = map(int, line.split())
		
		found = False
		# a, b, c, d represent either 0 or 1 years to be added to each value
		for a in range(2):
			if found:
				break
			for b in range(2):
				if found:
					break
				for c in range(2):
					if found:
						break
					for d in range(2):
						if found:
							break

						# Naively get values from given and derived equations
						Y = (12 + j - y - p - b - c) // 3 + d
						P = Y + p + b
						S = Y + y + c

						# Ensure value for S matches both given equations
						if S != P + s + a:
							continue

						# Ensure the sums match
						if S + P + Y == 12 + j:
							found = True

		print(S, P, Y)

if __name__ == '__main__':
	main()

'''
known values:
	s, p, y, j
	d = 12

S = P + s + a
P = Y + p + b
S = Y + y + c
S + P + Y = 12 + j

Y + y + c + Y + p + b + Y = 12 + j
3Y = 12 + j - y - p - (b + c)
'''