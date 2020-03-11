problems = {}
tot = 0
right = 0

while 1:
	line = input()
	if line == '-1':
		break

	prob = line.split()
	time,num,corr = int(prob[0]),prob[1],prob[2]

	if num not in problems:
		problems[num] = 0

	if corr == 'wrong':
		problems[num] += 20
	if corr == 'right':
		problems[num] += time
		tot += problems[num]
		right += 1


print(right,tot)