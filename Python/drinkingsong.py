def main():
	n = int(input())
	b = input()

	for i in range(n,0,-1):
		if i == 2:
			print(f'{i} bottles of {b} on the wall, {i} bottles of {b}.')
			print(f'Take one down, pass it around, {i-1} bottle of {b} on the wall.')
			print()
		elif i == 1:
			print(f'{i} bottle of {b} on the wall, {i} bottle of {b}.')
			print(f'Take it down, pass it around, no more bottles of {b}.')
		else:
			print(f'{i} bottles of {b} on the wall, {i} bottles of {b}.')
			print(f'Take one down, pass it around, {i-1} bottles of {b} on the wall.')
			print()

main()