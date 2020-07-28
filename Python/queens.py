def main():
	n = int(input())
	queens = [tuple(map(int, input().split())) for _ in range(n)]

	valid = True
	for i in range(n - 1):
		
		for j in range(i + 1, n):
			q1, q2 = queens[i], queens[j]

			if q1[0] == q2[0] or q1[1] == q2[1]:
				valid = False
			elif abs( q1[1] - q2[1] ) == abs( q1[0] - q2[0] ):
				valid = False

			if not valid:
				break

		if not valid:
			break

	print("CORRECT" if valid else "INCORRECT")

if __name__ == "__main__":
	main()