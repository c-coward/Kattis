line = input().split(" ")
n = int(line[0])
t = int(line[1])

line = input().split(" ")
times = [int(i) for i in line]

num = 0
for i in times:
	if t - i >= 0:
		t -= i
		num += 1
	else:
		break

print(num)