def gcf(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	factor = gcf(a, b)

	return a * (b // factor)

def main():
	n = int(input())

	for _ in range(n):
		w = int(input())
		nums = map(int, input().split())

		current_lcm = 1
		overflow = False

		for num in nums:
			current_lcm = lcm(num, current_lcm)

			if current_lcm > 10**9:
				print('More than a billion.')
				overflow = True
				break

		if not overflow:
			print(current_lcm)

if __name__ == '__main__':
	main()