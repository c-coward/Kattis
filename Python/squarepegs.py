from math import sqrt

def main():
	n, m, k = map(int, input().split())
	
	# Store plots in descending order
	plots = sorted(map(int, input().split()), reverse = True)

	circles = list(map(int, input().split()))
	# 'Radius' of a square = diaganol / 2 => side / sqrt(2)
	squares = list(map(lambda x : int(x) / sqrt(2), input().split()))

	# Store all houses together in descending order
	houses = sorted(circles + squares, reverse = True)

	# Match largest unfilled plot to largest house until either runs out
	plots_filled = 0
	for house in houses:
		if plots_filled == n:
			break

		if house < plots[plots_filled]:
			plots_filled += 1

	print(plots_filled)


if __name__ == "__main__":
	main()