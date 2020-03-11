def main():
	tnum,wood = map(int,input().split())
	trees = list(map(int,input().split()))
	trees = sorted(trees,reverse=True)

	diff = 0
	for i in range(1,tnum):
		diff += i*(trees[i-1]-trees[i])
		if diff >= wood: break

	lower = trees[i]
	if lower == trees[-1]: i += 1

	lower += (diff-wood)//i

	print(lower)

if __name__ == "__main__": main()