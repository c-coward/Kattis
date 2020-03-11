from sys import stdin
while 1:
	h,k = map(int,stdin.readline().split())
	if h==k==0: break
	heads = [int(stdin.readline()) for i in range(h)]
	knights = [int(stdin.readline()) for i in range(k)]

	heads.sort()
	knights.sort()

	sum_ = 0
	i = 0
	j = 0
	while i < k and j < h:
		if knights[i] >= heads[j]:
			j += 1
			sum_ += knights[i]
		i += 1

	if i==j and k >= h:
		print(sum_)
	else:
		print('Loowater is doomed!')