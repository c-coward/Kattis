def main():
	n = int(input())

	for i in range(1,n+1):
		s = int(input())

		lengths = input().split()
		blue = []
		red = []

		for l in lengths:
			if l[-1] == 'B':
				blue.append(int(l[:-1])-1)
			else:
				red.append(int(l[:-1])-1)

		blue.sort(reverse=True)
		red.sort(reverse=True)

		usable = min(len(blue), len(red))

		length = sum(red[:usable]) + sum(blue[:usable])

		print(f'Case #{i}: {length}')

main()