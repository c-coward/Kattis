n = int(input())

for i in range(n):
	print("Case #" + str(i+1) + ":", end = " ")

	line = input().split(" ")

	num = line[0]
	source = line[1]
	target = line[2]

	baseS = len(source)
	baseT = len(target)

	number = 0
	for i in range(len(num)):
		number += source.index(num[i]) * (baseS**(len(num)-1-i))

	newNum = ""
	n = number
	nums = []

	while n >= baseT:
		nums.append(n%baseT)
		n = int(n/baseT)
	nums.append(n)

	for i in range(len(nums)-1, -1, -1):
		newNum += target[nums[i]]

	print(newNum)