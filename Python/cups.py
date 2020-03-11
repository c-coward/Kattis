def main():
	n = int(input())
	cups = {}
	for i in range(n):
		a,b = input().split()
		if a[0] in '0123456789':
			a,b = b,int(a)//2
		b = int(b)
		cups[b] = a
	for num in sorted(cups):
		print(cups[num])


main()