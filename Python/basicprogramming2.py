def main():
	n,t = map(int,input().split())
	a = list(map(int,input().split()))

	if t == 1:
		complements = set()
		for e in a:
			if e in complements:
				print('Yes')
				return
			c_of_a = 7777-e
			complements.add(c_of_a)
		print('No')

	elif t == 2:
		dupes = set()
		for e in a:
			if e in dupes:
				print('Contains duplicate')
				return
			dupes.add(e)
		print('Unique')

	elif t == 3:
		count = {}
		for e in a:
			if e not in count: count[e] = 0
			count[e] += 1
		for c in count:
			if count[c] > n/2:
				print(c)
				return
		print(-1)

	elif t == 4:
		a.sort()
		if n % 2 == 1:
			print(a[n//2])
		else:
			print(a[n//2-1],a[n//2])
	else:
		print(' '.join([str(x) for x in sorted(a) if 100<=x<=999]))

main()