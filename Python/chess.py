from collections import deque

def main():
	t = int(input())
	for _ in range(t):
		c1, r1, c2, r2 = input().split()
		c1, c2 = map(lambda x : ord(x) - ord('A'), (c1, c2))
		r1, r2 = map(lambda x: 8 - int(x), (r1, r2))

		if (c1 + r1) % 2 != (c2 + r2) % 2: # start and end on different colored squares
			print('Impossible')
			continue

		if c1 == c2 and r1 == r2: # start and end on the same square
			print(0, toChar(c1), 8 - r1)
			continue

		# All points are 2 diagonal moves away from each other
		# Find the intersection of diagonal lines through the start and end points
		x_diags = getDiags(r1, c1)

		if (c2, r2) in x_diags: # move along a diagonal to the end point
			print(1, toChar(c1), 8 - r1, toChar(c2), 8 - r2)
			continue

		y_diags = getDiags(r2, c2)

		for c, r in x_diags:
			if (c, r) in y_diags:
				# Move to an intersection of the diagonals of the start and end, then to the end point
				print(2, toChar(c1), 8 - r1, toChar(c), 8 - r, toChar(c2), 8 - r2)
				break

def toChar(a):
	return chr(a + ord('A'))

def getDiags(a, b):
	diags = set()

	dirs = ((1, 1), (1, -1), (-1, -1), (-1, 1))
	for r, c in dirs:
		curr_r, curr_c = a, b
		while (0 <= curr_r + r < 8 and 0 <= curr_c + c < 8):
			diags.add((curr_c + c, curr_r + r))
			curr_r += r
			curr_c += c

	return diags

if __name__ == '__main__':
	main()