worlds = int(input())

worldList = [int(i) for i in input().split(" ")]
deaths = 0
deadThan = False

for i in range(worlds-2,-1,-1):
	if worldList[i] >= worldList[i+1]:
		temp = worldList[i+1] - 1
		deaths += (worldList[i] - temp)
		worldList[i] = temp

for w in worldList:
	if w < 0:
		deadThan = True

if deadThan:
	print(1)
else:
	print(deaths)