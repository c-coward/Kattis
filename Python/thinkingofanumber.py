def main():
	n = int(input())

	while n:
		lower = 0
		upper = float("inf")
		divs = []

		for _ in range(n):
			rule, helper, num = input().split()
			num = int(num)

			if rule == "greater":
				lower = max(lower, num)
			elif rule == "less":
				upper = min(upper, num)
			elif num != 1:
				divs.append(num)

		n = int(input())
		
		if upper == float("inf"):
			print("infinite")
			continue

		divs.sort(reverse = True)
		vals = list(range(lower + 1, upper))
		for div in divs:
			vals = [v for v in vals if not (v % div)]

		if vals:
			print(" ".join(map(str, vals)))
		else:
			print("none")

if __name__ == "__main__":
	main()