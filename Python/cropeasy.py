from math import hypot


def main():
	cases = int(input())
	for t in range(cases):
		n, A, B, C, D, X, Y, M = map(int, input().split())

		trees = [(X, Y)]
		for _ in range(n - 1):
			X = (A * X + B) % M
			Y = (C * Y + D) % M
			trees.append((X, Y))

		# print(trees)

		valid = 0
		for i in range(n - 2):
			for j in range(i + 1, n - 1):
				for k in range(j + 1, n):
					p1, p2, p3 = trees[i], trees[j], trees[k]
					# d1 = hypot(p1[0] - p2[0], p1[1] - p2[1])
					# d2 = hypot(p2[0] - p3[0], p2[1] - p3[1])
					# d3 = hypot(p3[0] - p1[0], p3[1] - p1[1])

					mid = (p1[0] + p2[0] + p3[0], p1[1] + p2[1] + p3[1])

					# dists = sorted([d1, d2, d3])
					if mid[0] % 3 == mid[1] % 3 == 0:
						valid += 1
						# print(p1, p2, p3)

		print(f'Case #{t + 1}: {valid}')

if __name__ == "__main__":
	main()