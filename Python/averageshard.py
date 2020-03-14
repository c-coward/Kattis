def main():
	t = int(input())
	for _ in range(t):
		input()
		num_cs,num_econ = map(int,input().split())
		
		cs_students = list(map(int,input().split()))
		econ_students = list(map(int,input().split()))

		cs_intel = sum(cs_students)/num_cs
		econ_intel = sum(econ_students)/num_econ

		cs_students.sort()

		total = 0
		for student in cs_students:
			if econ_intel < student < cs_intel:
				total += 1
		print(total)

main()
