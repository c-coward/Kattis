from sys import stdin
for line in stdin:
	n = int(line)
	if n == 0: break
	bin_ = bin(n-1)[2:]
	nums = []

	i = 0
	for l in bin_[::-1]:
		if l == '1':
			nums.append(str(3**i))
		i += 1

	ans = '{ ' + ', '.join(nums) + ' }'
	if ans == '{  }': ans = '{ }'
	print(ans)