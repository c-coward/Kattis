def main():
	n = int(input())
	for _ in range(n):
		w,g,h,r = map(int,input().split())

		Min = ((g-h)**2 + w**2)**.5
		Max = ((g+h-2*r)**2 + w**2)**.5

		print(Min,Max)

main()