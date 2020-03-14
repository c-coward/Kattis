def main():
	p = int(input())

	for _ in range(p):
		k,n = map(int,input().split())
		nums = []
		while len(nums) != n:
			for num in map(int,input().split()):
				nums.append(num)
		sorted_nums = sorted(nums)

		i = 0
		for num in nums:
			if num == sorted_nums[i]:
				i += 1

		print(k,n-i)

main()