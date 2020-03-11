def main():
	C,n = map(int,input().split())

	stations = []
	for _ in range(n):
		a,b,c = map(int,input().split())
		stations.append((a,b,c))

	flag = True
	total = 0
	for l,e,s in stations:
		total -= l
		if total < 0:
			flag = False
			break
		total += e
		if total > C:
			flag = False
			break
		if s and total < C:
			flag = False
			break
	if total > 0: flag = False

	print('possible' if flag else 'impossible')

main()