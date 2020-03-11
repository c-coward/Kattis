def main():
	n = int(input())
	days = list(map(int,input().split()))

	m = 0

	for i in range(1,n):
		if days[i] < days[m]: m = i

	print(m)

main()