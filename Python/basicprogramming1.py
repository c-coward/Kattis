def main():
	n,t = map(int,input().split())
	a = list(map(int,input().split()))

	if t == 1:
		print(7)
	elif t == 2:
		if a[0] > a[1]:
			print('Bigger')
		elif a[0] < a[1]:
			print('Smaller')
		elif a[0] == a[1]:
			print('Equal')

	elif t == 3:
		print(sorted(a[0:3])[1])

	elif t == 4:
		print(sum(a))

	elif t == 5:
		print(sum([x for x in a if x%2 == 0]))

	elif t == 6:
		letters = [chr(e%26 + 97) for e in a]
		print(''.join(letters))

	else:
		i = 0
		seen = set()
		while i != n-1:
			if i in seen:
				print('Cyclic')
				return
			if not (0 <= i < n):
				print('Out')
				return

			seen.add(i)
			i = a[i]
		print('Done')

main()