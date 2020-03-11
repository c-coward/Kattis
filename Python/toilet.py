def main():
	seats = input()
	first = seats[0]
	rest = seats[1:]
	f1,f2,f3 = 0,0,0
	
	# Case 1
	curr = first
	for s in rest:
		if curr != s:
			f1 += 1
		if s != 'U':
			f1 += 1
		curr = 'U'

	# Case 2
	curr = first
	for s in rest:
		if curr != s:
			f2 += 1
		if s != 'D':
			f2 += 1
		curr = 'D'

	# Case 3
	curr = first
	for s in rest:
		if curr != s:
			f3 += 1
		curr = s

	print(f1)
	print(f2)
	print(f3)

main()