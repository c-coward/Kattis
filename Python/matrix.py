from sys import stdin

def main():
	lines = stdin.readlines()

	for i in range((len(lines) + 1) // 3):
		a, b = map(int, lines[3 * i].split())
		c, d = map(int, lines[3 * i + 1].split())

		det = a * d - b * c

		print(f'Case {i + 1}:')
		print(f'{d // det} {-b // det}')
		print(f'{-c // det} {a // det}')

main()