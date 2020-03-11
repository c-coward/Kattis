nums = [int(i) for i in input().split(" ")]
nums.sort()
order = input()
for c in order:
	out = nums[0] if c == 'A' else nums[1] if c == 'B' else nums[2]
	print(out,end=' ')