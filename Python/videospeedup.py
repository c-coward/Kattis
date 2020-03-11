line = [int(i) for i in input().split(" ")]
stamps = [int(i) for i in input().split(" ")]

mult = 1
time = 0
curr = 0
for s in stamps:
	time += (s-curr)*mult
	mult += (line[1]/100)
	curr = s
time += (line[2]-curr)*mult
print(time)