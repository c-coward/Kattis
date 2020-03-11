def main():
	months1 = [31,28,31,30,31,30,31,31,30,31,30,31]
	months2 = [31,29,31,30,31,30,31,31,30,31,30,31]
	days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
	months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

	d,m = input().split()
	first = input()
	d = int(d)

	fd,lm = 0,0
	for i in range(7):
		if days[i] == first:
			fd = i
			break
	for i in range(12):
		if months[i] == m:
			lm = i
			break
	d1 = fd - 1
	d2 = fd - 1
	for i in range(lm):
		d1 += months1[i]
		d2 += months2[i]

	d1 += d
	d2 += d

	day1 = days[d1%7]
	day2 = days[d2%7]

	if day1 == day2 == 'FRI':
		print('TGIF')
	elif day1 == 'FRI' or day2 == 'FRI':
		print('not sure')
	else:
		print(':(')

main()