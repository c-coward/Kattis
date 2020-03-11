nums = [int(i) for i in input().split(" ")]
obs = set()
for i in range(nums[1]):
	l = int(input())
	if l < nums[0]:
		obs.add(l)
for i in range(nums[0]):
	if i not in obs:
		print(i)

print('Mario got',str(len(obs)),'of the dangerous obstacles.')