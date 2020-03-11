tests,target = [int(i) for i in input().split()]
scores = sum([int(i) for i in input().split()])

extra = 0
if target == 100 and scores/tests < 100:
	print("impossible")
else:
	while scores < target*(tests + extra):
		scores += 100
		extra += 1

	print(extra)