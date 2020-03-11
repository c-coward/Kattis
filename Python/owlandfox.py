tests = int(input())
for i in range(tests):
	num = input()
	numarr = [c for c in num]
	for j in range(len(num)-1,-1,-1):
		if num[j] != '0':
			numarr[j] = str(int(num[j]) - 1)
			break
	print(int(''.join(numarr)))