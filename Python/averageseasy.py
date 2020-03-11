tests = int(input())

for t in range(tests):
	input()
	Ncs,Ne = [int(i) for i in input().split()]
	cs = [int(i) for i in input().split()]
	e = [int(i) for i in input().split()]
	cs.sort()
	e.sort()
	csA = sum(cs)/Ncs
	eA = sum(e)/Ne

	i = 0
	for c in cs:
		if eA < c < csA:
			i += 1
	print(i)