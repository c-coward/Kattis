ppl = int(input())
eve = int(input())

known = [0]*ppl
for i in range(eve):
	line = [int(i)-1 for i in input().split()][1:]

	if 0 in line:
		for l in line:
			known[l] += 1
		continue

	most = sorted(known)[-1]

	for l in line:
		known[l] = most

most = sorted(known)[-1]

print('\n'.join([str(i+1) for i in range(ppl) if known[i] == most]))