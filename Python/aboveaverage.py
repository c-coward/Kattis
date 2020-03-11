n = int(input())

for i in range(n):
	line = input().split(" ")
	sums = 0
	grades = []
	for n in range(1,len(line)):
		sums += int(line[n])
		grades.append(int(line[n]))
	average = sums/len(grades)

	over = 0
	for g in grades:
		if g > average:
			over += 1

	percent = over/len(grades)
	print(format(percent, '.3%'))