def main():
	num = input()
	n = len(num)
	print(n,end=' ')

	x,y = 0,0
	for c in num:
		if c in '13':
			x += 2**(n-1)
		if c in '23':
			y += 2**(n-1)
		n -= 1

	print(x,y)

main()